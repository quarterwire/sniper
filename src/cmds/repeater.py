from discord.ext import commands
from discord.ext import tasks
import discord
import yaml

class Repeater(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.settings = yaml.safe_load(open("config.yml", "r").read())
        self.message_loop.start()  # This will automatically start the loop
        self.channels = []
        self.get_channels()
        
    def cog_unload(self):
        self.message_loop.stop()
    
    def get_channels(self):
        for id in self.settings.get("channels"):
            try:
                channel = self.bot.get_channel(id)
                self.channels.append(channel)
            except:
                print(f"Couldn't retrieve channel: {id}")
        

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.bot.user.id:
            return

    @tasks.loop(seconds=60)  # Default interval, adjusted in start_loop()
    async def message_loop(self):
        if self.channels:
            for channel in self.channels:
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
