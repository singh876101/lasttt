import requests

TOKEN = "7714162630:AAFIy7UvMS9OdDOTj68b8GRxSk0MHitCeJE"
WEBHOOK_URL = "https://boiling-aurora-sonusharma-9c2bf4bb.koyeb.app/"

def set_webhook():
    url = f"https://api.telegram.org/bot{TOKEN}/setWebhook"
    data = {"url": WEBHOOK_URL}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Webhook set successfully")
    else:
        print(f"Failed to set webhook: {response.text}")

if __name__ == "__main__":
    set_webhook()

