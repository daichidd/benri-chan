import discord
import settings
import re

from benrichan.youtubelive import YoutubeLive

YOUTUBE_API_KEY = settings.YOUTUBE_API_KEY
YOUTUBE_LIVE_URL_BASE = r'https://www.youtube.com/watch\?v='


def get_client():
    client = discord.Client()

    @client.event
    async def on_ready():
        print('run benri-chan')

    @client.event
    async def on_message(message):
        # ignore bot self message
        if message.author.bot:
            return

        # for test
        # if message.content == '!test':
        #     await message.channel.send(f'{message.author.mention}さんおはよう')

        # youtube live comment speaker
        pattern = f'!benri\s{YOUTUBE_LIVE_URL_BASE}\w*'
        if re.match(pattern, message.content):
            _youtube_live = YoutubeLive(message)
            await _youtube_live.comment_speaker()

        # TODO: みんないなくなったら自動で切断するようにしたい
        # !disだとRythmと被る
        if message.content == '!benridis':

            if message.guild.voice_client is None:
                await message.channel.send('ボイスチャンネルにいないよ！')
                return

            await message.guild.voice_client.disconnect()

    return client
