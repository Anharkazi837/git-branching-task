# data_sender.py

import requests

def send_data_to_hub(hub_url, data):
    """
    Sends data to the specified HUB URL.
    
    Parameters:
    - hub_url: str, the endpoint to send data to.
    - data: dict, the payload to send.
    
    Returns:
    - Response object
    """
    try:
        response = requests.post(hub_url, json=data)
        response.raise_for_status()
        print(f"Data sent successfully: {data}")
        return response
    except requests.RequestException as e:
        print(f"Failed to send data: {e}")
        return None
