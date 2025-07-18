from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from keep_alive import keep_alive

BOT_TOKEN = "8132147727:AAFJT1PR4bg8nXmXuukmidzlgQU73lph-NM"
ADMIN_ID = 8021896750
SHEET_ID = "1fV9FUhGQzca_xctInKgAmwi5yOKARz9aH8IF7pvUwA8"

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open_by_key(SHEET_ID).sheet1

def log_event(text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([timestamp, text])

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text("Halo! MatchBot aktif.")
    log_event(f"{user.id} started bot.")

def main():
    keep_alive()
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
