from flask import Flask
import requests

app = Flask(__name__)

# Replace with your actual bot token and Koyeb URL
TOKEN = "7714162630:AAFLwJTbKIHGq_4HIdn0DiPctFaQHvt8pXU"
WEBHOOK_URL = "https://boiling-aurora-sonusharma-9c2bf4bb.koyeb.app/"

@app.route('/')
def hello_world():
    return 'Hello from Koyeb'

def set_webhook():
    url = f"https://api.telegram.org/bot{TOKEN}/setWebhook"
    data = {"url": WEBHOOK_URL}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Webhook set successfully")
    else:
        print(f"Failed to set webhook: {response.text}")

if __name__ == "__main__":
    set_webhook()  # Set the webhook when the app starts
    app.run(host="0.0.0.0", port=8080)


