import os
import requests
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

load_dotenv()

current_utc_time = datetime.utcnow()
desired_timezone = timezone(timedelta(hours=1))
current_datetime_with_timezone = current_utc_time.replace(
    tzinfo=timezone.utc
).astimezone(desired_timezone)
formatted_datetime = current_datetime_with_timezone.strftime("%Y-%m-%dT%H:%M:%S%z")


def send_transaction(transaction_type, amount, description, source_name, message):
    api_endpoint = os.getenv("FIREFLY_III_API_ENDPOINT") + "/v1/transactions"
    try:
        data = {
            "error_if_duplicate_hash": True,
            "apply_rules": True,
            "fire_webhooks": True,
            "transactions": [
                {
                    "type": transaction_type,
                    "date": formatted_datetime,
                    "amount": amount,
                    "description": description,
                    "notes": message,
                    "source_name": source_name,
                }
            ],
        }

        response = requests.post(api_endpoint, json=data)

        if response.status_code == 200:
            print("Data sent successfully!")
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
            print(response.text)  # Print the response content for further inspection
    except Exception as e:
        print(f"Error sending data: {e}")
