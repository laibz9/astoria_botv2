import discord
from discord.ext import commands
from discord.commands import slash_command, Option, user_command, message_command

class message_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"📁 Loaded ({self.__class__.__name__}) Succeed.")

    @message_command(guild_ids=[1338195130699612276])
    async def copy_message(self, ctx, message:discord.Message):
        await ctx.respond(f'copy - {message.content}')

def setup(bot):
    bot.add_cog(message_commands(bot))