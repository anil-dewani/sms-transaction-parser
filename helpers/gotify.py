import requests


def send_gotify_notification(title, message, priority=5):
    # Replace these with your Gotify server URL and API token
    GOTIFY_SERVER_URL = "https://your-gotify-server.com"
    GOTIFY_API_TOKEN = "your-gotify-api-token"

    # Gotify API endpoint for sending a message
    endpoint = f"{GOTIFY_SERVER_URL}/message"

    # Data to be sent in the request
    data = {"title": title, "message": message, "priority": priority}

    # Headers with the API token
    headers = {"X-Gotify-Key": GOTIFY_API_TOKEN}

    try:
        # Make a POST request to the Gotify server
        response = requests.post(endpoint, json=data, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("Gotify notification sent successfully!")
        else:
            print(
                f"Failed to send Gotify notification. Status code: {response.status_code}"
            )
    except Exception as e:
        print(f"Error sending Gotify notification: {e}")
