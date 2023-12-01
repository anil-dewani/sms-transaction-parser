import requests


def send_data_to_api(data):
    # Replace 'https://api.example.com/endpoint' with the actual API endpoint URL
    api_endpoint = "https://api.example.com/endpoint"

    try:
        # Send a POST request with the data
        response = requests.post(api_endpoint, json=data)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("Data sent successfully!")
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
            print(response.text)  # Print the response content for further inspection
    except Exception as e:
        print(f"Error sending data: {e}")


# Example data to be sent to the API endpoint
data_to_send = {"key1": "value1", "key2": "value2"}
