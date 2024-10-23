from discord.ext import commands
from discord.ext import tasks
import discord
import yaml

class Repeater(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.settings = yaml.safe_load(open("config.yml", "r").read())
        self.channel_id = self.settings.get("channel")  # Use .get() to avoid KeyError if channel isn't present
        self.message_loop.start()  # This will automatically start the loop
        self.channel = self.bot.get_channel(self.channel_id)
        if self.channel:
            print(f"Channel found. (ID {self.channel.id})")
        else:
            print("Channel not found")

    def cog_unload(self):
        self.message_loop.stop()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.bot.user.id:
            return

    @tasks.loop(seconds=60)  # Default interval, adjusted in start_loop()
    async def message_loop(self):
        if self.channel:
            await self.channel.send(self.settings["message"])
        else:
            print(f"Channel with ID {self.channel_id} not found.")

    @message_loop.before_loop
    async def before_message_loop(self):
        await self.start_loop()
        await self.bot.wait_until_ready()  # Ensure the bot is ready before the loop starts

    @message_loop.error
    async def message_loop_error(self, error):
        print(f'An error occurred in the message loop: {error}')

    async def start_loop(self):
        self.message_loop.change_interval(seconds=self.settings["interval"])
        print(f"Loop interval set to {self.settings['interval']} seconds.")
        if not self.message_loop.is_running():
            self.message_loop.start()


async def setup(bot):
    await bot.add_cog(Repeater(bot))
