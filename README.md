# smart_community_bot
# 🤖 Smart Community Bot

This project is a **Telegram bot** designed to help manage and classify group messages in a community. It categorizes important messages like meetings, events, and maintenance updates, and also answers user questions about them later.

---

## ✨ Features

- 🧠 Automatically classifies messages into:
  - MEETING
  - EVENT
  - MAINTENANCE
  - GENERAL

- 💬 Answers user queries like:
  - “When is the meeting?”
  - “Is there any festival/event?”
  - “Any maintenance info?”

- ✅ Stores messages under the correct category
- 📌 Highlights important messages automatically

---

## 🚀 How to Use

1. **Start the bot** by sending `/start`.
2. **Send announcements** like:
   - `"Meeting on Friday at 5 PM"` → gets stored under MEETING
   - `"Festival celebration on Sunday!"` → stored under EVENT
3. **Ask queries** like:
   - `"When is the meeting?"` → bot replies with latest MEETING info
   - `"Any maintenance work?"` → bot replies accordingly

---

## 🛠 Tech Stack

- Python 🐍
- `python-telegram-bot` library
- Telegram Bot API

---

## 📦 Running Locally

1. Install the required package:
   ```bash
   pip install python-telegram-bot
2. Add your Bot Token inside telegram_bot.py:

python

bot_token = "YOUR_BOT_TOKEN"

3. Run the bot:

bash

python telegram_bot.py   
[README.md](https://github.com/user-attachments/files/21363479/README.md)
