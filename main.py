import discord
import settings


class BenriChan:
    DISCORD_BOT_TOKEN = settings.DISCORD_BOT_TOKEN

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
        if message.content == "!test":
            await message.channel.send(f"{message.author.mention}さんおはよう")

    client.run(DISCORD_BOT_TOKEN)


benriChan = BenriChan()
