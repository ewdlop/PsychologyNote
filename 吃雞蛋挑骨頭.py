# Picking bones out of eggs
# Pick your os
# Install python
# Install pip
# !pip install psychopy

from psychopy import visual, event, core

# Create a window
win = visual.Window([800, 600], color="white", units="pix")

# Define some stimuli (e.g., "eggs")
instructions = visual.TextStim(win, text="Identify if there's a 'bone' in the egg.\nPress 'y' for Yes, 'n' for No.", color="black", pos=(0, 200))
egg_normal = visual.ImageStim(win, image="egg_normal.png", pos=(0, 0), size=(300, 300))
egg_faulty = visual.ImageStim(win, image="egg_with_bone.png", pos=(0, 0), size=(300, 300))

# Stimuli and conditions
stimuli = [
    {"stimulus": egg_normal, "has_bone": False},
    {"stimulus": egg_faulty, "has_bone": True},
    {"stimulus": egg_normal, "has_bone": False},
]
response_data = []

# Display instructions
instructions.draw()
win.flip()
core.wait(2)

# Trial loop
for trial in stimuli:
    stimulus = trial["stimulus"]
    has_bone = trial["has_bone"]

    stimulus.draw()
    win.flip()

    # Wait for participant response
    keys = event.waitKeys(keyList=["y", "n", "escape"])
    if "escape" in keys:
        break  # Exit the experiment

    # Store response
    response = keys[0]
    is_correct = (response == "y" and has_bone) or (response == "n" and not has_bone)
    response_data.append({"stimulus": stimulus.image, "response": response, "correct": is_correct})

    # Give feedback
    feedback = visual.TextStim(
        win,
        text="Correct!" if is_correct else "Wrong!",
        color="green" if is_correct else "red",
        pos=(0, -200),
    )
    feedback.draw()
    win.flip()
    core.wait(1)

# End of experiment
end_text = visual.TextStim(win, text="Experiment Complete. Thank you!", color="black")
end_text.draw()
win.flip()
core.wait(3)

# Cleanup
win.close()
core.quit()

# Print results
for data in response_data:
    print(data)
