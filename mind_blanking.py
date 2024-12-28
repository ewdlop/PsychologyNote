from psychopy import visual, core, event
import random

# Setup window
win = visual.Window([800, 600], color="white")

# Define stimuli
memory_items = ["A", "B", "C", "D"]
distractor_items = ["RED", "BLUE", "GREEN", "YELLOW"]
correct_responses = ["A", "B", "C", "D"]

# Display fixation
fixation = visual.TextStim(win, text="+", color="black")
fixation.draw()
win.flip()
core.wait(0.5)

# Display memory items
for item in memory_items:
    stim = visual.TextStim(win, text=item, color="black")
    stim.draw()
    win.flip()
    core.wait(1)

# Distractor task
for distractor in distractor_items:
    stim = visual.TextStim(win, text=distractor, color="black")
    stim.draw()
    win.flip()
    keys = event.waitKeys(keyList=["r", "b", "g", "y"])  # Responses for RED, BLUE, GREEN, YELLOW

# Recall task
recall_prompt = visual.TextStim(win, text="Recall the sequence:", color="black")
recall_prompt.draw()
win.flip()

response = event.waitKeys(keyList=["a", "b", "c", "d"])

# Check response
if response == correct_responses:
    print("Correct!")
else:
    print("Incorrect!")

win.close()
core.quit()
