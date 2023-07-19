import discord
import os
from dotenv import load_dotenv

class ISClubClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_member_join(self, member):
        return await self.on_message(f"Welcome {member}")

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$count'):
            count = self.count_member()
            await message.channel.send(f'total member in the server is {count}')
        await message.channel.send(f'{message.content}')


intents = discord.Intents.default()
intents.message_content = True
client = ISClubClient(intents=intents)

load_dotenv()
client.run(os.getenv('TOKEN'))