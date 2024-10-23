import discord
from discord.ext import commands
import telegram
from datetime import datetime
import os
from dotenv import load_dotenv
import asyncio  # Import asyncio for running coroutines

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID', 0))
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

print("Starting bot...")
print(f"Discord Channel ID: {DISCORD_CHANNEL_ID}")
print(f"Telegram Chat ID: {TELEGRAM_CHAT_ID}")

# Initialize Discord bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Initialize Telegram bot (async)
telegram_bot = telegram.Bot(token=TELEGRAM_TOKEN)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is in {len(bot.guilds)} servers')
    print(f'Monitoring channel ID: {DISCORD_CHANNEL_ID}')
    
    # Send test message to Telegram using asyncio.run() to run the coroutine
    try:
        await telegram_bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="Discord bot is now connected! 🚀")
        print("Successfully connected to Telegram!")
    except Exception as e:
        print(f"Telegram connection error: {e}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id == DISCORD_CHANNEL_ID:
        formatted_message = f"{message.author.name}: {message.content}"
        
        if message.attachments:
            for attachment in message.attachments:
                formatted_message += f"\n{attachment.url}"

        try:
            # Synchronously send the message to Telegram using await (since on_message is async)
            await telegram_bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=formatted_message)
            print(f"Message forwarded to Telegram at {datetime.now()}")
            print(f"Message content: {formatted_message}")
        except Exception as e:
            print(f"Error forwarding message: {e}")
            print(f"Attempted to send to chat_id: {TELEGRAM_CHAT_ID}")
            print(f"Message was: {formatted_message}")

    await bot.process_commands(message)

# Run the bot
bot.run(DISCORD_TOKEN)
