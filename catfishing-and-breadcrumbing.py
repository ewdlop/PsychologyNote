from psychopy import visual, core, event, gui, data

# Create a window
win = visual.Window([800, 600], color=(1, 1, 1))

# Collect participant info
info = {"Participant ID": ""}
dlg = gui.DlgFromDict(dictionary=info, title="Experiment Info")
if not dlg.OK:
    core.quit()

# Create a text stimulus
message = visual.TextStim(win, text='', color=(-1, -1, -1), wrapWidth=1.5)

# Create a response box
response_box = visual.TextStim(win, text='', color=(-1, -1, -1), pos=(0, -0.4), wrapWidth=1.5)

# Define the messages to simulate catfishing and breadcrumbing behavior
catfish_messages = [
    "Hey! I saw your profile and thought we have a lot in common.",
    "I travel a lot for work, but I'd love to meet up sometime.",
    "I'm really looking for someone to share adventures with.",
    "Can you tell me more about yourself?"
]

breadcrumb_messages = [
    "I love our chats, but I'm really busy right now.",
    "We should totally hang out sometime soon.",
    "Sorry, I was away. How have you been?",
    "Let's catch up soon, okay?"
]

# Define expected participant responses
expected_responses = [
    "Hi! Nice to meet you. What do you do?",
    "That sounds interesting. Where have you traveled to?",
    "I enjoy adventures too! What kind are you into?",
    "Sure! I'm [participant's response]."
]

# Function to display message and collect response
def display_message_and_collect_response(message_text):
    message.setText(message_text)
    message.draw()
    win.flip()
    
    # Collect participant response
    response = event.waitKeys(keyList=['return'], timeStamped=True)
    response_box.setText(f"Participant response: {expected_responses[0]}")  # Simplified for example
    response_box.draw()
    win.flip()
    core.wait(2)  # Display the response for 2 seconds

# Loop through catfishing messages
for msg in catfish_messages:
    display_message_and_collect_response(msg)

# Loop through breadcrumbing messages
for msg in breadcrumb_messages:
    display_message_and_collect_response(msg)

# End of experiment
end_message = visual.TextStim(win, text="Thank you for participating!", color=(-1, -1, -1))
end_message.draw()
win.flip()
core.wait(3)

win.close()
core.quit()
