from psychopy import visual, core, event
import random

# --- Experiment Setup ---
# Create a window
win = visual.Window(size=(800, 600), color=(1, 1, 1), units="norm")

# Create visual elements
balloon = visual.ImageStim(win, image="balloon.png", size=(0.5, 0.5), pos=(0, 0))
pop_balloon = visual.ImageStim(win, image="pop.png", size=(0.5, 0.5), pos=(0, 0))
points_text = visual.TextStim(win, text="Points: 0", pos=(0, -0.7), color=(-1, -1, -1), height=0.08)
feedback_text = visual.TextStim(win, text="", pos=(0, 0), color=(-1, -1, -1), height=0.1)

# Initialize variables
total_points = 0
num_trials = 20

# --- Main Experiment Loop ---
for trial in range(num_trials):
    # Trial-specific variables
    balloon_size = 0.5
    current_trial_points = 0
    pop_limit = random.randint(5, 15)  # Randomize balloon popping point
    
    # Trial loop
    trial_running = True
    while trial_running:
        # Draw stimuli
        balloon.size = (balloon_size, balloon_size)
        balloon.draw()
        points_text.text = f"Points: {total_points}"
        points_text.draw()
        win.flip()
        
        # Collect keypress
        keys = event.waitKeys(keyList=["space", "return"])
        
        if "space" in keys:
            # Inflate the balloon
            balloon_size += 0.1
            current_trial_points += 1
            
            # Check if the balloon pops
            if balloon_size >= pop_limit:
                # Display the popped balloon
                pop_balloon.draw()
                win.flip()
                core.wait(1)
                current_trial_points = 0  # Lose points for this trial
                trial_running = False

        elif "return" in keys:
            # Cash out
            total_points += current_trial_points
            trial_running = False

# --- Feedback at the End ---
feedback_text.text = f"Final Score: {total_points}"
feedback_text.draw()
win.flip()
core.wait(5)

# --- End Experiment ---
win.close()
core.quit()
