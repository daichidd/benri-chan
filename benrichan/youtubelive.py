import requests
import settings


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
        chat_id = self.get_chat_id()
        print('chat_id: ', chat_id)
        # for test
        # await self.message.channel.send('ボイスチャンネルに入ったよ！')

    def get_video_id(self, command):
        pos = command.find('=')
        return command[pos + 1:]

    def get_chat_id(self):
        api_url = 'https://www.googleapis.com/youtube/v3/videos'
        params = {
            'key': settings.YOUTUBE_API_KEY,
            'id': self.video_id,
            'part': 'liveStreamingDetails',
        }
        data = requests.get(api_url, params=params).json()

        liveDetails = data['items'][0]['liveStreamingDetails']
        if 'activeLiveChatId' in liveDetails.keys():
            chat_id = liveDetails['activeLiveChatId']
        else:
            chat_id = None

        return chat_id
