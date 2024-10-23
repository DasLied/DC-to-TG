Discord to Telegram Bridge Bot 🌉

Forwards messages from Discord → Telegram
Includes attachments (links)
Shows who sent the original message

Setup Guide 🛠️
Prerequisites
pip install discord.py python-telegram-bot python-dotenv
Step 1: Discord Setup

Go to Discord Developer Portal
Create a "New Application" (give it a cool name)
Go to the "Bot" section
Click "Add Bot" and grab the token
IMPORTANT: Enable these under "Privileged Gateway Intents":

Message Content Intent
Server Members Intent
Presence Intent


Invite the bot to your server using the OAuth2 URL Generator

Select 'bot' scope
Give it 'Read Messages/View Channels' and 'Send Messages' permissions



Step 2: Telegram Setup

Message @BotFather on Telegram
Use the /newbot command to create your bot
Save the token he gives you
Add the bot to your group
Make it an admin in the group (so it can actually send messages)
Get your group ID (easiest way is to use @username_to_id_bot)

Step 3: Configuration

Create a .env file in your project folder:
CopyDISCORD_TOKEN=your_discord_bot_token
DISCORD_CHANNEL_ID=your_channel_id
TELEGRAM_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_group_id

Step 4: Run It! 🚀
python dc.py
