from psychopy import visual, core

# Initialize window
win = visual.Window([800, 600], color="black", units="pix")

# Create walls (example)
left_wall = visual.Rect(win, width=200, height=600, fillColor="gray", pos=(-300, 0))
right_wall = visual.Rect(win, width=200, height=600, fillColor="gray", pos=(300, 0))
floor = visual.Rect(win, width=800, height=200, fillColor="darkgray", pos=(0, -300))
ceiling = visual.Rect(win, width=800, height=200, fillColor="darkgray", pos=(0, 300))

# Original stimulus
stimulus = visual.ImageStim(win, image="stimulus.jpg", pos=(0, 0), size=(100, 100))

# Reflected stimulus
mirror_stimulus = visual.ImageStim(win, image="stimulus.jpg", pos=(0, 0), size=(100, 100), flipHoriz=True)

# Example positions for reflection
stimulus.pos = (-100, 0)  # Original position
mirror_stimulus.pos = (100, 0)  # Mirrored position

# Draw the room and stimuli
left_wall.draw()
right_wall.draw()
floor.draw()
ceiling.draw()

stimulus.draw()         # Original
mirror_stimulus.draw()  # Mirrored

# Display the scene
win.flip()
core.wait(2)

# Move the stimulus interactively
while True:
    keys = event.getKeys()
    if 'left' in keys:
        stimulus.pos += (-10, 0)
        mirror_stimulus.pos += (10, 0)  # Reflect the movement
    elif 'right' in keys:
        stimulus.pos += (10, 0)
        mirror_stimulus.pos += (-10, 0)

    # Redraw everything
    left_wall.draw()
    right_wall.draw()
    floor.draw()
    ceiling.draw()
    stimulus.draw()
    mirror_stimulus.draw()
    win.flip()

    if 'escape' in keys:
        break

win.close()
core.quit()

