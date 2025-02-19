from psychopy import visual, event, core, gui, data
import os

# Initialize PsychoPy Window
win = visual.Window(fullscr=True, color=(0, 0, 0))

# Load Rorschach images (Ensure these images are in the same folder as the script)
image_list = ["rorschach1.jpg", "rorschach2.jpg", "rorschach3.jpg"]
stimuli = [visual.ImageStim(win, image=img) for img in image_list]

# Prepare to collect data
exp_info = {'Participant': ''}
dlg = gui.DlgFromDict(dictionary=exp_info, title="Rorschach Test")
if not dlg.OK:
    core.quit()

# Create data file
filename = f"data/{exp_info['Participant']}_rorschach_{data.getDateStr()}.csv"
os.makedirs("data", exist_ok=True)
data_file = open(filename, 'w')
data_file.write("Participant, Image, Response\n")

# Run the Experiment
for stim in stimuli:
    stim.draw()
    win.flip()
    
    # Get Response (text-based)
    response = event.waitKeys(keyList=['1', '2', '3', '4', '5', 'space', 'return'], timeStamped=True)

    # Save Data
    data_file.write(f"{exp_info['Participant']}, {stim.image}, {response}\n")

# Cleanup
data_file.close()
win.close()
core.quit()
