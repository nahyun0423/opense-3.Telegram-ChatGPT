import time
import requests
import openai

OPENAI_API_KEY = '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'
openai.api_key = OPENAI_API_KEY

TELEGRAM_BOT_TOKEN = '6940871687:AAF2prfaM75J4tW0-2Vk0c8PYbJz3ko2UgA'
TELEGRAM_CHAT_ID = '6532805693'

def send_telegram_message(token, chat_id, message):
    base_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    response = requests.get(base_url)
    return response.json()

def chatGPT(message):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=message,
            max_tokens=150
        )

        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error in ChatGPT API: {e}")
        return "Error in ChatGPT API"

def main():
    while True:
        user_input = input("Enter a message: ")

        gpt_response = chatGPT(user_input)

        print("ChatGPT Response:", gpt_response)

        send_telegram_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, gpt_response)

        time.sleep(2)

if __name__ == "__main__":
    main()