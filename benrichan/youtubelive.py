
class YoutubeLive():
    def __init__(self, message):
        self.message = message
        self.video_id = self.get_video_id(message.content)

    async def comment_speaker(self):
        # speaker is not in voice channel
        if self.message.author.voice is None:
            await self.message.channel.send('ボイスチャンネルに入ってから呼んでね')
            return

        # benri-chan connect to voice channel
        await self.message.author.voice.channel.connect()
        print(self.video_id)
        # for test
        # await self.message.channel.send('ボイスチャンネルに入ったよ！')

    def get_video_id(self, command):
        pos = command.find('=')
        return command[pos + 1:]
