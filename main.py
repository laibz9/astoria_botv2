import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv("config/.env")

intents = discord.Intents.all()

class astoria_bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.TOKEN = os.getenv("TOKEN")
        super().__init__(command_prefix=commands.when_mentioned_or('!'), 
                         intents = intents,
                         *args,
                         **kwargs
                         )

bot = astoria_bot(owner_id=1209844348099764245, case_insensitive=True)

@bot.event
async def on_ready():
    print(f'✅ Bot {bot.user} is ready!')

# โหลด cogs จากโฟลเดอร์ cogs/
if __name__ == "__main__":
    for file in os.listdir('./cogs'):
        if file.endswith('.py') and not file.startswith('_'):
            try:
                bot.load_extension(f'cogs.{file[:-3]}')
            except Exception as e:
                print(f"❌ Failed to load {file}: {e}")

    bot.run(bot.TOKEN)