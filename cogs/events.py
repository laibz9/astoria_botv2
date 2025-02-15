import discord
from discord.ext import tasks, commands
from discord.commands import slash_command, Option, user_command, message_command
import datetime

RULES_CHANNEL_ID = 1338224430219919380
WELCOME_CHANNEL_ID = 1338376280428773397
LEAVE_CHANNEL_ID = 1338376280428773397


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"📁 Loaded ({self.__class__.__name__}) Succeed.")


# Join
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = self.bot.get_channel(WELCOME_CHANNEL_ID)
        rules_channel = self.bot.get_channel(RULES_CHANNEL_ID)
        if channel and rules_channel:
            embed = discord.Embed(
                title="🎉 ยินดีต้อนรับ!",
                description=f"👋 สวัสดี {member.mention}!\n"
                            "เราดีใจที่คุณเข้าร่วมกับเรา 💖\n\n"
                            f"📌 กรุณาอ่านกฎของเซิร์ฟเวอร์ที่นี่: {rules_channel.mention}\n"
                            "✨ มาทำความรู้จักกันและสนุกไปด้วยกันเถอะ!",
                color=discord.Color.green(),
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
            embed.set_footer(text="เราหวังว่าคุณจะมีช่วงเวลาที่ดี!")
            icon_url = None
            if self.bot.user:
                icon_url = self.bot.user.avatar.url if self.bot.user.avatar else self.bot.user.default_avatar.url

            embed.set_author(name="Astoria", icon_url=icon_url)
            embed.set_image(url="https://i0.wp.com/www.galvanizeaction.org/wp-content/uploads/2022/06/Wow-gif.gif?fit=450%2C250&ssl=1")

            await channel.send(embed=embed)
        else:
            print(f"❌ Error: Channel ID {WELCOME_CHANNEL_ID} or {RULES_CHANNEL_ID} not found.")

# Leave
    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        channel = self.bot.get_channel(LEAVE_CHANNEL_ID)
        if channel:
            embed = discord.Embed(
                title="👋 ลาก่อน!",
                description=f"😢 ไม่นะคุณ {member.mention}!\n"
                            "ได้ออกจากเซิร์ฟเวอร์แล้ว...\n"
                            "ขอให้โชคดีและหวังว่าจะได้พบกันอีกนะ! 💔\n"
                            "ถ้าอยากกลับมาเมื่อไหร่ เรายินดีต้อนรับเสมอ! 🤗",
                color=discord.Color.red(),
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
            embed.set_footer(text="เราหวังว่าคุณจะมีช่วงเวลาที่ดี!")
            icon_url = None
            if self.bot.user:
                icon_url = self.bot.user.avatar.url if self.bot.user.avatar else self.bot.user.default_avatar.url

            embed.set_author(name="Astoria", icon_url=icon_url)
            embed.set_image(url="https://media1.giphy.com/media/PiceuRrhk1nshZDduv/giphy.gif?cid=6c09b952r5al7nzzqz996hl8hucr0vaelfvc4o9f69wwqvvn&ep=v1_internal_gif_by_id&rid=giphy.gif&ct=g")

            await channel.send(embed=embed)
        else:
            print(f"❌ Error: Channel ID {LEAVE_CHANNEL_ID} not found.")

# Message
    @commands.Cog.listener()
    async def on_message(self, message: discord.message):
        if message.author == self.bot.user:
            return
        if message.content.lower() == 'ping':
            await message.channel.send('Pong!')
        
        elif any(x in message.content.lower() for x in ['admin']):
            await message.channel.send('What?')

        await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(Events(bot))