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
message = visual.TextStim(win, text=text, color=(-1, -1, -1), wrapWidth=1.5, pos=(0, 0.2))

# Create a visual tracker (e.g., a dot)
tracker = visual.Circle(win, radius=0.01, fillColor='red', pos=(-0.7, -0.2))

# Display the text and move the tracker
message.draw()
win.flip()
core.wait(1)  # Initial wait

for pos in np.linspace(-0.7, 0.7, 100):
    tracker.pos = (pos, -0.2)
    message.draw()
    tracker.draw()
    win.flip()
    core.wait(0.05)

# Close the window
win.close()
