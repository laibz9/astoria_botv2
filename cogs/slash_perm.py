import discord
from discord.ext import commands
from discord.commands import slash_command, permissions, Option

server_guild = [1338195130699612276]   # ใส่ Server ID ของคุณ

class slash_perm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"📁 Loaded ({self.__class__.__name__}) Succeed.")

# //////////////////// ONLY USER COMMANDS ////////////////////

    @slash_command(guild_ids=server_guild,
                   default_permissions=False,
                   description="Check bot latency For Only User."
                   )

    async def ping_user(self, ctx):
        # ตรวจสอบว่าผู้ใช้มี ID ตรงตามที่กำหนดหรือไม่
        if ctx.author.id != ctx.guild.owner_id and ctx.author.id != 1209844348099764245:   # กำหนด user_id ที่อนุญาตให้ใช้คำสั่งนี้
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
                   description="Check bot latency For Only Role."
                   )
    
    async def ping_role(self, ctx):
        # ตรวจสอบว่าผู้ใช้มี Role ID นี้หรือไม่
        has_role = discord.utils.get(ctx.author.roles, id=1338756413521924109)   # ใส่ Role ID ที่ต้องการอนุญาตให้ใช้คำสั่ง
        if not has_role and ctx.author.id != ctx.guild.owner_id:
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
                   description="Purges a channel's message."
                   )
    
    async def purge(self, ctx, number: int):
        # ตรวจสอบว่าผู้ใช้มี Role ID นี้หรือไม่
        has_role = discord.utils.get(ctx.author.roles, id=1338756413521924109)   # ใส่ Role ID ที่ต้องการอนุญาตให้ใช้คำสั่ง
        # ถ้าไม่มีให้ทำสิ่งนี้
        if not has_role and ctx.author.id != ctx.guild.owner_id:
            await ctx.respond("❌ คุณไม่มีสิทธิ์ใช้คำสั่งนี้!", ephemeral=True)
            return
        
        # ถ้ามีให้ทำสิ่งนี้
        z = await ctx.channel.purge(limit=number)
        await ctx.respond(f"✅ ลบข้อความไปแล้ว {len(z)} ข้อความ!", ephemeral=True)

def setup(bot):
    bot.add_cog(slash_perm(bot))