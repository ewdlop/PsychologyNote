import random

# Define rooms and patients
ward = {
    "Room 101": ["Patient A: Fever", "Patient B: Cough"],
    "Room 102": ["Patient C: Injury", "Patient D: Headache"],
    "Room 103": ["Patient E: Stomach Ache", "Patient F: Cold"],
}

# Function to simulate interactions
def interact_with_patient(room, patient):
    interactions = [
        "Checking temperature",
        "Administering medication",
        "Recording symptoms",
        "Providing comfort"
    ]
    action = random.choice(interactions)
    return f"In {room}, {patient}, action taken: {action}"

# Simulate interactions in the ward
for room, patients in ward.items():
    for patient in patients:
        result = interact_with_patient(room, patient)
        print(result)