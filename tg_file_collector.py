from config import Config
import asyncio
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
import qrcode

api_id = Config.API_ID
api_hash = Config.API_HASH

async def authorize_with_qr():
    client = TelegramClient("session", api_id, api_hash)
    await client.connect()

    try:
        if not await client.is_user_authorized():
            qr = await client.qr_login()

            qrcode.make(qr.url).save("telegram_login_qr.png")
            print("Open telegram_login_qr.png and scan QR code with you Telegram app to authorize.")
            await qr.wait()
    finally:
        await client.disconnect()

async def get_files_from_telegram(chat_link, topic_id=None):
    async with TelegramClient("session", api_id, api_hash) as Client:

        entity = await Client.get_entity(chat_link)
        print(f"\nПодключились к: {entity.title}\n")
        print("Собираем файлы...\n")

        files = []

        async for message in Client.iter_messages(
            entity,
            reply_to = topic_id if topic_id else None
        ):
            if message.document:
                file_name = message.file.name if message.file else "File is noname"
                files.append(file_name)

        return files

async def main():
    chat_link = "https://t.me/+CXM7VjXkpeMzMmEy"    # My group

    topic_id = 632  # Topic with courses

    await authorize_with_qr()

    files = await get_files_from_telegram(chat_link, topic_id)

    with open("files.txt", "w", encoding="utf-8") as f:
        for file in files:
            f.write(file + "\n")

    print("Files have been saved to files.txt")


if __name__ == "__main__":
    asyncio.run(main())