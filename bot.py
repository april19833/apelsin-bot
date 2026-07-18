import os
from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters,
)

ADMIN_ID = 379198558
TOKEN = os.getenv("8343671858:AAEFHlF8lgT6q_oOr2rVCs9MVNhJbhVCM90")


async def forward_to_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.forward_message(
        chat_id=ADMIN_ID,
        from_chat_id=update.effective_chat.id,
        message_id=update.message.message_id,
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.PHOTO, forward_to_admin))
    app.add_handler(MessageHandler(filters.Document.IMAGE, forward_to_admin))

    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
