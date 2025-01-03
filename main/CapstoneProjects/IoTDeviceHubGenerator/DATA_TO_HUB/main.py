# main.py

import time
from config import HUB_URL, SEND_INTERVAL
from data_generator import generate_data
from data_sender import send_data_to_hub

def main():
    """
    Main function to continuously generate and send data to the HUB.
    """
    while True:
        data = generate_data()
        print(f"Data: {data}")
        send_data_to_hub(HUB_URL, data)
        time.sleep(SEND_INTERVAL)

if __name__ == "__main__":
    main()
