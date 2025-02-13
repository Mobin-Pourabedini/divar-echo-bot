import os

from kenarBot import KenarBot
from kenarBot.types import ChatBotMessage
import cowsay

# Initialize your API key from Kenar platform
DIVAR_API_KEY = os.getenv("DIVAR_API_KEY")
DIVAR_IDENTIFICATION_KEY = os.getenv("DIVAR_IDENTIFICATION_KEY")

# Create a bot instance
bot = KenarBot(DIVAR_IDENTIFICATION_KEY, "/webhook", DIVAR_API_KEY)

def swap_chars(text: str, a: str, b: str) -> str:
    parts = text.split(a)
    for i, part in enumerate(parts):
        parts[i] = part.replace(b, a)
    return b.join(parts)

def kenar_cow_say(text: str) -> str:
    text = text.replace(' ', 'ß')   # preserve spaces in original text
    text = cowsay.get_output_string("cow", text)
    text = swap_chars(text, '/', '\\')  # swapped for rtl compatibility
    text = text.replace('  ', '...')  # adjusted based on divar font ratio's
    parts = text.split('\n')
    for i, part in enumerate(parts):
        # force each line to be rtl for compatibility across android and web clients
        parts[i] = u'\u200F' + part
    parts[2] = parts[2].replace('.', '')  # beautify
    parts[0] = parts[0].replace('.', '_')  # beautify
    text = '\n'.join(parts)
    return text.replace('ß', ' ')

# Define a message handler that responds to messages containing "hello"
@bot.message_handler()
def handle_hello(chatbot_message: ChatBotMessage):
    # Send a response back to the same conversation
    bot.send_message(chatbot_message.conversation_id, kenar_cow_say(chatbot_message.message))

if __name__ == "__main__":
    bot.run()
