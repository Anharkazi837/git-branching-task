# IoT Data Hub

This is a Flask-based API that serves as a hub for collecting and displaying data from different IoT devices. The API allows you to retrieve, create, update, and delete data related to temperature, humidity, pressure, light intensity, device status, and timestamps. It is designed to showcase the data in a browser or allow integration with other systems.

## API Endpoints

### 1. **Root Endpoint**
- **URL**: `/`
- **Method**: `GET`
- **Description**: This is the welcome endpoint of the API.
- **Response**:
    ```json
    {
      "message": "Welcome to the Flask API!"
    }
    ```

### 2. **Get All Items**
- **URL**: `/iot`
- **Method**: `GET`
- **Description**: Retrieves all the data from the IoT devices.
- **Response**:
    ```json
    [
        {
            "temperature": 645,
            "humidity": 50,
            "pressure": 1013,
            "light_intensity": 300,
            "device_status": "active",
            "timestamp": "2024-12-23T10:00:00Z"
        },
        ...
    ]
    ```

## How to Run

 - Navogate the FLASK_API folder
1. Clone this repository to your local machine.
2. Install the necessary dependencies using pip:
    ```bash
    pip install flask
    ```
3. Run the Flask application:
    ```bash
    python app.py
    ```
4. The API will be available at `http://localhost:5000`.

---

# Data Generator and Sender for HUB

This Python project simulates generating data from various sources (e.g., temperature, humidity, pressure) and sends the data to a HUB continuously.

## Project Structure

- `config.py`: Configuration settings for the HUB URL and data send interval.
- `data_generator.py`: Generates mock data, including temperature, humidity, pressure, light intensity, device status, and timestamps.
- `data_sender.py`: Sends the generated data to the HUB endpoint.
- `main.py`: The main entry point that continuously generates data and sends it to the HUB.

## Modules

### 1. `config.py`

The `config.py` file contains configuration settings such as the HUB URL and the interval for sending data.

```python
# config.py

HUB_URL = "https://example-hub.com/api/endpoint"  # Replace with actual HUB endpoint
SEND_INTERVAL = 5  # Interval in seconds
```

### 2. `data_generator.py`

The `data_generator.py` file contains functions that simulate generating data from various sources.

```python
# data_generator.py

import random
import time

def generate_temperature():
    """Generates temperature data."""
    return round(random.uniform(20.0, 30.0), 2)

def generate_humidity():
    """Generates humidity data."""
    return round(random.uniform(40.0, 60.0), 2)

def generate_pressure():
    """Generates pressure data in hPa."""
    return round(random.uniform(900.0, 1100.0), 2)

def generate_light_intensity():
    """Generates light intensity in lumens."""
    return round(random.uniform(100.0, 1000.0), 2)

def generate_device_status():
    """Simulates the status of a device."""
    statuses = ["ON", "OFF", "IDLE", "ERROR"]
    return random.choice(statuses)

def generate_timestamp():
    """Generates a UNIX timestamp."""
    return int(time.time())

def generate_data():
    """
    Simulates generating all data to send to the HUB.
    Returns a dictionary with multiple data types.
    """
    return {
        "temperature": generate_temperature(),
        "humidity": generate_humidity(),
        "pressure": generate_pressure(),
        "light_intensity": generate_light_intensity(),
        "device_status": generate_device_status(),
        "timestamp": generate_timestamp()
    }
```

### 3. `data_sender.py`

The `data_sender.py` file contains a function that sends the generated data to the HUB via a POST request.

```python
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

```

### 4. `main.py`

The `main.py` file is the entry point of the program, which continuously generates and sends data to the HUB.

```python
# main.py

import time
from config import HUB_URL, SEND_INTERVAL
from data_generator import generate_data
from data_sender import send_data_to_hub

def main():
    """Main function to continuously generate and send data to the HUB."""
    while True:
        data = generate_data()  # Generates all data types
        send_data_to_hub(HUB_URL, data)  # Sends data to the HUB
        time.sleep(SEND_INTERVAL)

if __name__ == "__main__":
    main()

```

## How to Run

1. **Install Dependencies:**
   Ensure you have the necessary dependencies, such as the `requests` library, installed. You can install it via pip:

   ```bash
   pip install requests
   ```
2. **Configuration: Update the HUB_URL in the config.py file with the actual endpoint URL where you want to send the data. You can also modify the SEND_INTERVAL variable to adjust the time interval (in seconds) between each data send.**
```python
HUB_URL = "https://example-hub.com/api/endpoint"  # Replace with your HUB URL
SEND_INTERVAL = 5  # Time in seconds between each data send
```
3. **Run the Script: To start generating and sending data, run the main.py script. It will run continuously, sending data to the HUB at the specified interval.**

```bash
python main.py
```

---

## Notes
- The `items` list in this API acts as an in-memory database for demonstration purposes. In a production environment, you should integrate with a persistent database such as PostgreSQL or MongoDB.
- The API currently does not implement authentication or authorization.

## License
This project is close-source and available under the Our License.
