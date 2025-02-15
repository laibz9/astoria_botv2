import discord
from discord.ext import commands
from discord.commands import slash_command

# 🔹 กำหนดค่าตัวแปรช่องและ Role ที่ต้องการให้
CHANNEL_ID = 1338377084212609186        # 🔹 ใส่ ID ของห้องที่จะส่งข้อความ
ROLE_ID = 1338377142563508266           # 🔹 ใส่ ID ของ Role ที่ต้องการให้
RULES_CHANNEL_ID = 1338224430219919380  # 🔹 ใส่ ID ห้อง Rule ที่ต้องการให้

class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"📁 Loaded ({self.__class__.__name__}) Succeed.")

    @slash_command(name="sendverify",
                   description="ส่งข้อความยืนยันตัวตนไปยังห้องที่กำหนด (Admin only)",
                   guild_ids=[1338195130699612276],    # 🔹 ใส่ ID ของ Guild ที่ต้องการให้
                   default_permissions=False
                   )
    async def sendverify(self, ctx):

        guild = ctx.guild
        channel = guild.get_channel(CHANNEL_ID)
        role = guild.get_role(ROLE_ID)
        rules_channel = guild.get_channel(RULES_CHANNEL_ID)

        is_admin = ctx.author.guild_permissions.administrator   # ตรวจสอบว่าเป็น Admin หรือไม่
        is_owner = ctx.author.id == ctx.guild.owner_id   # ตรวจสอบว่าเป็น Owner หรือไม่

        if not is_owner and not is_admin:
            await ctx.respond("❌ คุณไม่มีสิทธิ์ใช้คำสั่งนี้!", ephemeral=True)
            return
        if not channel:
            return await ctx.respond("❌ ไม่พบห้องที่กำหนด ตรวจสอบ `CHANNEL_ID` ในโค้ด!", ephemeral=True)
        if not role:
            return await ctx.respond("❌ ไม่พบ Role ที่กำหนด ตรวจสอบ `ROLE_ID` ในโค้ด!", ephemeral=True)
        if not rules_channel:
            return await ctx.respond("❌ ไม่พบห้องกฎ! ตรวจสอบ `RULES_CHANNEL_ID` ในโค้ด!", ephemeral=True)
        
        verify_button = discord.ui.Button(
            label="✅ Verify Me!",
            style=discord.ButtonStyle.success
        )

        async def button_callback(interaction: discord.Interaction):
            member = interaction.user
            if role in member.roles:
                return await interaction.response.send_message("⚠️ คุณได้รับ Role นี้ไปแล้ว!", ephemeral=True)

            await member.add_roles(role)
            await interaction.response.send_message("✅ คุณได้รับ Role Verified แล้ว! ยินดีต้อนรับ!", ephemeral=True)

        verify_button.callback = button_callback

        view = discord.ui.View()
        view.add_item(verify_button)

        embed = discord.Embed(
            title="🔹 ยินดีต้อนรับสู่เซิร์ฟเวอร์!",
            description="เพื่อเข้าถึงเนื้อหาและห้องแชททั้งหมด กรุณากดยืนยันตัวตนด้านล่าง",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=ctx.guild.icon.url if ctx.guild.icon else None)
        embed.add_field(name="📜 กฎของเซิร์ฟเวอร์", value=f"โปรดปฏิบัติตามกฎของเรา {rules_channel.mention}", inline=False)
        embed.add_field(name="🎉 สิทธิพิเศษ", value="เมื่อยืนยันตัวตนแล้ว คุณจะสามารถเข้าถึงเนื้อหาและกิจกรรมต่างๆ ได้เต็มที่!", inline=False)
        embed.set_footer(text="หากมีปัญหา โปรดติดต่อแอดมิน 👨‍💻")

        await channel.send(embed=embed, view=view)
        await ctx.respond(f"✅ ส่งข้อความยืนยันตัวตนไปยัง {channel.mention} เรียบร้อย!", ephemeral=True)

def setup(bot):
    bot.add_cog(Verify(bot))