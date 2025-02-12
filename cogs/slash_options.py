import discord
from discord.ext import commands
from discord.commands import slash_command, Option

server_guild = [1338195130699612276]   # ใส่ Server ID ของคุณ

class slash_options(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"📁 Loaded ({self.__class__.__name__}) Succeed.")




    @slash_command(guild_ids=server_guild)
    async def hello_slash(self, ctx):
        embed = discord.Embed(title='GGEZ',
                              color=0x48ff00
                              )
        await ctx.respond(embed=embed)

    @slash_command(guild_ids=server_guild,
                   description="Check bot latency."
                   )
    async def ping_everyone(self, ctx):
        latency = round(ctx.bot.latency * 1000)
        await ctx.respond(f"🏓 Pong! Latency: `{latency}ms`")




def setup(bot):
    bot.add_cog(slash_options(bot))