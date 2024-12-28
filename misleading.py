from psychopy import visual, event, core
import random

# Setup
win = visual.Window([800, 600], color="white")
feedback_options = ["Correct!", "Incorrect!"]

# Trial Loop
for trial in range(5):
    # Display a simple stimulus
    stim = visual.TextStim(win, text="Press 'a' or 'b'", color="black")
    stim.draw()
    win.flip()
    
    # Wait for response
    keys = event.waitKeys(keyList=['a', 'b'])
    
    # Generate misleading feedback randomly
    feedback = random.choice(feedback_options)
    
    # Display feedback
    feedback_stim = visual.TextStim(win, text=feedback, color="red")
    feedback_stim.draw()
    win.flip()
    core.wait(1)

win.close()
core.quit()
