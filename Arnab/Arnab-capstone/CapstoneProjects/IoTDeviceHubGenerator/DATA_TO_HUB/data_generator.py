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
    statuses = ["ON", "OFF", "IDLE"]
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

