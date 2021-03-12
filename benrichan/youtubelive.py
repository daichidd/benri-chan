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

        # for test
        # await self.message.channel.send('ボイスチャンネルに入ったよ！')

        # benri-chan connect to voice channel
        await self.message.author.voice.channel.connect()
        chat_id = self.get_chat_id()

        nextPageToken = None
        iter_item = 90
        slp_time = 10
        for i in range(iter_item):
            print('in for')
            try:
                print('in try')
                nextPageToken = self.get_chat(chat_id, nextPageToken)
                time.sleep(slp_time)
            except Exception as e:
                print('error ', e)
                break

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
        chat_id = None
        if 'activeLiveChatId' in liveDetails.keys():
            chat_id = liveDetails['activeLiveChatId']

        return chat_id

    def get_chat(self, chat_id, pageToken):
        api_url = 'https://www.googleapis.com/youtube/v3/liveChat/messages'
        params = {'key': settings.YOUTUBE_API_KEY, 'liveChatId': chat_id, 'part': 'id,snippet,authorDetails'}

        if type(pageToken) == str:
            params['pageToken'] = pageToken

        data = requests.get(api_url, params=params).json()

        print('data', data)
