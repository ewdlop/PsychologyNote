from psychopy import visual, core, event

# Create a window
win = visual.Window([800, 600], color=(1, 1, 1))

# Create a text stimulus
message = visual.TextStim(win, text='Hello, PsychoPy!', color=(-1, -1, -1))

# Draw the text stimulus on the window
message.draw()

# Flip (update) the window to show the stimulus
win.flip()

# Wait for 2 seconds
core.wait(2)

# Close the window
win.close()
