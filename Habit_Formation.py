from psychopy import visual, core, event

# Create a window
win = visual.Window(size=(800, 600), color="black")

# Instructions
instructions = visual.TextStim(win, text="Press 'z' for BLUE, 'm' for RED\nPress any key to start.", color="white")
instructions.draw()
win.flip()
event.waitKeys()

# Stimuli
blue_stim = visual.TextStim(win, text="BLUE", color="blue")
red_stim = visual.TextStim(win, text="RED", color="red")

# Trials
stimuli = [blue_stim, red_stim] * 10  # Repeat each stimulus 10 times
keys = {'z': 'blue', 'm': 'red'}
responses = []
timer = core.Clock()

# Phase 1: Habit Formation
instructions.text = "Phase 1: Press the corresponding key for the color."
instructions.draw()
win.flip()
core.wait(2)

for stim in stimuli:
    stim.draw()
    win.flip()
    timer.reset()
    key = event.waitKeys(keyList=["z", "m", "escape"], timeStamped=timer)
    if key[0][0] == "escape":
        break
    responses.append((stim.text, key[0][0], key[0][1]))  # Stimulus, Response, Time

# Phase 2: Rule Change
instructions.text = "Phase 2: RULE CHANGE! Now 'z' for RED, 'm' for BLUE."
instructions.draw()
win.flip()
core.wait(2)

for stim in stimuli:
    stim.draw()
    win.flip()
    timer.reset()
    key = event.waitKeys(keyList=["z", "m", "escape"], timeStamped=timer)
    if key[0][0] == "escape":
        break
    responses.append((stim.text, key[0][0], key[0][1]))  # Stimulus, Response, Time

# End
instructions.text = "Thank you for participating!"
instructions.draw()
win.flip()
core.wait(3)
win.close()

# Print Results
for response in responses:
    print(response)
