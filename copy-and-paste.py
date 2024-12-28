from psychopy import visual, core

# Create a window
win = visual.Window(size=(800, 600), fullscr=False, color=(1, 1, 1), units='height')

# Create text stimulus
text = visual.TextStim(win, text="Hello, World!", color=(-1, -1, -1))

# Draw the text to the window
text.draw()

# Update the display
win.flip()

# Wait for 5 seconds
core.wait(5)

# Close the window
win.close()
