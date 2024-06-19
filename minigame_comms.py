import requests

# HomeAssistant details
home_assistant_url = "http://your-homeassistant-url:8123"
api_token = "HA_LONG_LIVED_ACCESS_TOKEN"
headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}

# Function to get state
def get_state(entity_id):
    url = f"{home_assistant_url}/api/states/{entity_id}"
    response = requests.get(url, headers=headers)
    return response.json()

# Function to update state
def update_state(entity_id, new_state, attributes=None):
    url = f"{home_assistant_url}/api/states/{entity_id}"
    data = {
        "state": new_state,
        "attributes": attributes or {}
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Example usage
entity_id = "sensor.example_sensor"
state = get_state(entity_id)
print("Current state:", state)

new_state = "on"
attributes = {"custom_attribute": "value"}
update_response = update_state(entity_id, new_state, attributes)
print("Update response:", update_response)
