from psychopy import visual, core, event

# Create a window
win = visual.Window([800, 600], color=(1, 1, 1))

# Text to display
text = """
The Triforce method comprises strategies to boost reading speed significantly.
1. Eliminating internal monologue
2. Using a visual tracker
3. Adopting a reading strategy (80/20 rule)
"""

# Create a text stimulus
message = visual.TextStim(win, text=text, color=(-1, -1, -1), wrapWidth=1.5)

# Display the text for a set amount of time
message.draw()
win.flip()
core.wait(5)  # Display for 5 seconds

# Instruction for summarization
instruction = visual.TextStim(win, text="Please summarize the content in one or two lines.", color=(-1, -1, -1), pos=(0, -0.4))
instruction.draw()
win.flip()

# Wait for user input (e.g., press any key to finish)
event.waitKeys()

# Close the window
win.close()
