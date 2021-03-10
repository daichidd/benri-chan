from benrichan.client import get_client
import settings

DISCORD_BOT_TOKEN = settings.DISCORD_BOT_TOKEN

client = get_client()

client.run(DISCORD_BOT_TOKEN)
