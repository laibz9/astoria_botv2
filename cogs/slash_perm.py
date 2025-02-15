import discord
from discord.ext import commands
from discord.commands import slash_command, permissions, Option

server_guild = [1338195130699612276]   # ใส่ Server ID ของคุณ

class SlashPerm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"📁 Loaded ({self.__class__.__name__}) Succeed.")

# //////////////////// ONLY USER COMMANDS ////////////////////
# Owner Command
    @slash_command(guild_ids=server_guild,
                   default_permissions=False,
                   description="Check bot latency.  (Owner only)"
                   )

    async def owner_command(self, ctx):
        # ตรวจสอบว่าผู้ใช้มี ID ตรงตามที่กำหนดหรือไม่
        is_owner = ctx.author.id == ctx.guild.owner_id   # ตรวจสอบว่าเป็น Owner หรือไม่

        if not is_owner:   # กำหนด user_id ที่อนุญาตให้ใช้คำสั่งนี้
        # ถ้าไม่มีให้ทำสิ่งนี้
            await ctx.respond("❌ คุณไม่มีสิทธิ์ใช้คำสั่งนี้!", ephemeral=True)
            return

        # ถ้ามีให้ทำสิ่งนี้
        latency = round(ctx.bot.latency * 1000)
        await ctx.respond(f"🏓 Pong! Latency: `{latency}ms`")


    @slash_command(guild_ids=server_guild,
                   default_permissions=False,
                   description="Check bot latency.  (Admin only)"
                   )

# Admin Command
    async def admin_command(self, ctx):
        # ตรวจสอบว่าผู้ใช้มี ID ตรงตามที่กำหนดหรือไม่
        is_owner = ctx.author.id == ctx.guild.owner_id   # ตรวจสอบว่าเป็น Owner หรือไม่
        is_admin = ctx.author.guild_permissions.administrator   # ตรวจสอบว่าเป็น Admin หรือไม่

        if not is_owner and not is_admin:
        # ถ้าไม่มีให้ทำสิ่งนี้
            await ctx.respond("❌ คุณไม่มีสิทธิ์ใช้คำสั่งนี้!", ephemeral=True)
            return

        # ถ้ามีให้ทำสิ่งนี้
        latency = round(ctx.bot.latency * 1000)
        await ctx.respond(f"🏓 Pong! Latency: `{latency}ms`")

# //////////////////// ROLE COMMANDS ////////////////////
# Check bot latency
    @slash_command(guild_ids=server_guild,
                   default_permissions=False,
                   description="Check bot latency. (Role only)"
                   )
    
    async def role_command(self, ctx):
        # ตรวจสอบว่าผู้ใช้มี Role ID นี้หรือไม่
        has_role = discord.utils.get(ctx.author.roles, id=1338377142563508266)   # ใส่ Role ID (Member)
        is_admin = ctx.author.guild_permissions.administrator   # ตรวจสอบว่าเป็น Admin หรือไม่
        is_owner = ctx.author.id == ctx.guild.owner_id   # ตรวจสอบว่าเป็น Owner หรือไม่

        if not has_role and not is_admin and not is_owner:
        # ถ้าไม่มีให้ทำสิ่งนี้
            await ctx.respond("❌ คุณไม่มีสิทธิ์ใช้คำสั่งนี้!", ephemeral=True)
            return
        
        # ถ้ามีให้ทำสิ่งนี้
        latency = round(ctx.bot.latency * 1000)
        await ctx.respond(f"🏓 Pong! Latency: `{latency}ms`")

# Purge messages
    @slash_command(guild_ids=server_guild,
                   default_permissions=True,
                   name="purge",
                   description="คำสั่งสำหรับลบข้อความในช่องแชทจำนวนที่ระบุ (Admin only)"
                   )
    
    async def purge(self, ctx, number: int):
        # ตรวจสอบว่าผู้ใช้มี Role ID นี้หรือไม่
        has_role = discord.utils.get(ctx.author.roles, id=1340397775166242816)   # ใส่ Role ID ที่ต้องการอนุญาตให้ใช้คำสั่ง
        is_admin = ctx.author.guild_permissions.administrator   # ตรวจสอบว่าเป็น Admin หรือไม่
        is_owner = ctx.author.id == ctx.guild.owner_id   # ตรวจสอบว่าเป็น Owner หรือไม่

        # ถ้าไม่มีให้ทำสิ่งนี้
        if not has_role and not is_admin and not is_owner:
            await ctx.respond("❌ คุณไม่มีสิทธิ์ใช้คำสั่งนี้!", ephemeral=True)
            return
        
        # ถ้ามีให้ทำสิ่งนี้
        del_messages = await ctx.channel.purge(limit=number)
        await ctx.respond(f"✅ ลบข้อความไปแล้ว {len(del_messages)} ข้อความ!", ephemeral=True)

def setup(bot):
    bot.add_cog(SlashPerm(bot))