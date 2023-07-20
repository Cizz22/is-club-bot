import discord
import os
from dotenv import load_dotenv
import requests
import time

class ISClubClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_member_join(self, member):
        channel_target = self.get_channel(752854944331202650)
        channel_roadmap = self.get_channel(778971281202348042)
        channel_networking = self.get_channel(778971357236428810)
        channel_qna = self.get_channel(778971357236428810)

        await member.send(
            f"""
            Welcome to the **IS Club** community, {member.mention}! :handshake:

**IS Club** dibuat dengan harapan mahasiswa SI dapat menemukan bidang yang diminati dan ditekuni, jadi buat komunitas ini menjadi tempat yang nyaman untuk belajar :innocent:
            > **GUIDELINE**
            > You can introduce yourself in channel {channel_networking.mention}
            > You can see the learning roadmaps here {channel_roadmap.mention}
            > For further questions, you can ask at {channel_qna.mention}
            """)
        
        await channel_target.send(
            f"""
            Welcome to the **IS Club** community, {member.mention}! :handshake:

**IS Club** dibuat dengan harapan mahasiswa SI dapat menemukan bidang yang diminati dan ditekuni, jadi buat komunitas ini menjadi tempat yang nyaman untuk belajar :innocent:
            > **GUIDELINE**
            > You can introduce yourself in channel {channel_networking.mention}
            > You can see the learning roadmaps here {channel_roadmap}
            > For further questions, you can ask at {channel_qna.mention}
            """)
        
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('>jokes'):
            content = await self.get_jokes()
            await message.channel.send(content)

    async def get_jokes(self):
        header = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36',
                'Accept': 'application/json',
            }
        time.sleep(2)
        fetch = requests.get('https://icanhazdadjoke.com/', headers=header)
        content = fetch.json()['joke']

        return content

# Configurations
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = ISClubClient(intents=intents)
load_dotenv()
client.run(os.getenv('TOKEN'))