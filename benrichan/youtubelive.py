
class YoutubeLive():
    def __init__(self, message):
        self.message = message

    async def comment_speaker(self):
        # speaker is not in voice channel
        if self.message.author.voice is None:
            await self.message.channel.send('ボイスチャンネルに入ってから呼んでね')
            return

        # benri-chan connect to voice channel
        await self.message.author.voice.channel.connect()
        # for test
        # await self.message.channel.send('ボイスチャンネルに入ったよ！')

    async def disconnect(self):
        if self.message.guild.voice_client is None:
            await self.message.channel.send('ボイスチャンネルにいないよ！')
            return

        await self.message.guild.voice_client.disconnect()
        # for test
        # await self.message.channel.send('ボイスチャンネルから出たよ！')
