import discord
from discord.ext import commands
from discord.commands import slash_command, Option, user_command, message_command

class reference(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"📁 Loaded ({self.__class__.__name__}) Succeed.")

def setup(bot):
    bot.add_cog(reference(bot))