import os

from kenarBot import KenarBot
from kenarBot.types import ChatBotMessage

# Initialize your API key from Kenar platform
DIVAR_API_KEY = os.getenv("DIVAR_API_KEY")
DIVAR_IDENTIFICATION_KEY = os.getenv("DIVAR_IDENTIFICATION_KEY")

# Create a bot instance
bot = KenarBot(DIVAR_IDENTIFICATION_KEY, "/webhook", DIVAR_API_KEY)

# Define a message handler that responds to messages containing "hello"
@bot.message_handler(regexp="hello")
def handle_hello(chatbot_message: ChatBotMessage):
    # Send a response back to the same conversation
    bot.send_message(chatbot_message.conversation_id, f"Hi, my name is AmazingKenarBot")

if __name__ == "__main__":
    # Start the bot
    bot.run()
