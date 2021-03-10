from benrichan.client import get_client
import settings

DISCORD_BOT_TOKEN = settings.DISCORD_BOT_TOKEN


def main():
    client = get_client()

    client.run(DISCORD_BOT_TOKEN)


if __name__ == '__main__':
    main()
