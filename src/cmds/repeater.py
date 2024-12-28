from discord.ext import commands, tasks
import discord
import yaml

class Repeater(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.settings = yaml.safe_load(open("config.yml", "r").read())
        self.message_loop.start()  # Automatically starts the loop
        self.channels = []  # List to store channels and their messages
        self.get_channels()
        
    def cog_unload(self):
        self.message_loop.stop()

    def get_channels(self):
        """
        Load channels and messages from the configuration file into a list of dictionaries.
        Each entry will contain 'channel' (the Discord channel object) and 'message' (the message to send).
        """
        for entry in self.settings.get("channels", []):  # Iterate over the channels array
            try:
                channel_id = entry["id"]
                message = entry["message"]
                channel = self.bot.get_channel(channel_id)
                if channel is not None:
                    self.channels.append({"channel": channel, "message": message})
                else:
                    print(f"Couldn't retrieve channel: {channel_id}")
            except KeyError as e:
                print(f"Invalid channel entry in config: {entry}, missing key {e}")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.bot.user.id:
            return

    @tasks.loop(seconds=60)  # Default interval, updated in `start_loop`
    async def message_loop(self):
        """
        Send messages to all channels from the loaded configuration.
        Each channel sends its own unique message.
        """
        if self.channels:
            for entry in self.channels:
                channel = entry["channel"]
                message = entry["message"]
                try:
                    await channel.send(message)
                except Exception as e:
                    print(f"Error sending message to {channel.id}: {e}")
        else:
            print("No valid channels to send messages to.")

    @message_loop.before_loop
    async def before_message_loop(self):
        """
        Wait until the bot is ready before starting the loop.
        """
        await self.bot.wait_until_ready()
        self.message_loop.change_interval(seconds=self.settings["interval"])
        print(f"Loop interval set to {self.settings['interval']} seconds.")

    @message_loop.error
    async def message_loop_error(self, error):
        """
        Handle errors in the message loop.
        """
        print(f"An error occurred in the message loop: {error}")

    async def start_loop(self):
        """
        Starts the message loop and adjusts the interval based on settings.
        """
        self.message_loop.change_interval(seconds=self.settings["interval"])
        print(f"Loop interval set to {self.settings['interval']} seconds.")
        if not self.message_loop.is_running():
            self.message_loop.start()


async def setup(bot):
    """
    Add the Repeater cog to the bot.
    """
    await bot.add_cog(Repeater(bot))
