"""
Anthropic Principle Demonstration in PsychoPy

This experiment demonstrates the observer-dependent nature of reality through
various perceptual phenomena that illustrate how the act of observation
influences what is observed - a key insight from the Anthropic Principle.

Perceptual demonstrations:
1. Binocular Rivalry demonstration - competing perceptions
2. Necker Cube demonstration - ambiguous figure reversals
3. Change Blindness demonstration - what we don't observe doesn't "exist" for us
4. Metacognitive Monitoring demonstration - observing our own observations

The experiment illustrates that observation is not passive reception but
active construction, constrained by our cognitive architecture.
"""

from psychopy import visual, core, event, gui
import random
import numpy as np

# --- Window Setup ---
# Create window first to ensure proper cleanup if dialog is cancelled
win = visual.Window(
    size=[1024, 768],
    color=[0, 0, 0],
    units='height',
    fullscr=False
)

# --- Configuration Dialog ---
exp_info = {
    'Participant ID': '',
    'Age': '',
    'Session': '001'
}

dlg = gui.DlgFromDict(dictionary=exp_info, title='Anthropic Principle Experiment')
if not dlg.OK:
    win.close()
    core.quit()

# --- Visual Stimuli ---

# Instructions text
instructions = visual.TextStim(
    win,
    text='',
    height=0.04,
    wrapWidth=0.9,
    color='white'
)

# Fixation cross
fixation = visual.TextStim(
    win,
    text='+',
    height=0.08,
    color='white'
)

# For binocular rivalry simulation
left_grating = visual.GratingStim(
    win,
    tex='sin',
    mask='circle',
    size=0.3,
    sf=5,
    ori=45,
    pos=[-0.2, 0],
    opacity=0.5
)

right_grating = visual.GratingStim(
    win,
    tex='sin',
    mask='circle',
    size=0.3,
    sf=5,
    ori=-45,
    pos=[0.2, 0],
    opacity=0.5
)

# Necker Cube vertices (ambiguous 3D cube)
necker_lines = [
    # Front square
    [(-0.15, -0.15), (-0.15, 0.15)],
    [(-0.15, 0.15), (0.15, 0.15)],
    [(0.15, 0.15), (0.15, -0.15)],
    [(0.15, -0.15), (-0.15, -0.15)],
    # Back square (offset)
    [(-0.05, -0.05), (-0.05, 0.25)],
    [(-0.05, 0.25), (0.25, 0.25)],
    [(0.25, 0.25), (0.25, -0.05)],
    [(0.25, -0.05), (-0.05, -0.05)],
    # Connecting lines
    [(-0.15, -0.15), (-0.05, -0.05)],
    [(-0.15, 0.15), (-0.05, 0.25)],
    [(0.15, 0.15), (0.25, 0.25)],
    [(0.15, -0.15), (0.25, -0.05)]
]

necker_cube = [
    visual.Line(win, start=start, end=end, lineColor='white', lineWidth=3)
    for start, end in necker_lines
]

# Change blindness stimuli
scene_a = visual.Rect(win, width=0.3, height=0.3, pos=[-0.2, 0], fillColor='red')
scene_b = visual.Rect(win, width=0.3, height=0.3, pos=[0.2, 0], fillColor='blue')
scene_change = visual.Rect(win, width=0.3, height=0.3, pos=[-0.2, 0], fillColor='green')  # Changed element

# Response recording
response_text = visual.TextStim(
    win,
    text='',
    pos=[0, -0.4],
    height=0.03,
    color='yellow'
)

# --- Helper Functions ---

def show_instructions(text, duration=None):
    """Display instruction screen"""
    instructions.text = text
    instructions.draw()
    win.flip()
    if duration:
        core.wait(duration)
    else:
        event.waitKeys(keyList=['space'])

def show_fixation(duration=1.0):
    """Display fixation cross"""
    fixation.draw()
    win.flip()
    core.wait(duration)

# --- Experiment Trials ---

def trial_1_observer_selection():
    """
    Trial 1: Observer Selection Effect
    Demonstrates that we can only observe what our perceptual system allows
    """
    show_instructions(
        "TRIAL 1: OBSERVER SELECTION\n\n"
        "The Anthropic Principle states that we can only observe\n"
        "a universe compatible with our existence as observers.\n\n"
        "This means our observations are limited by our\n"
        "perceptual and cognitive capabilities.\n\n"
        "You will see competing visual patterns.\n"
        "Notice how your brain selects what to perceive.\n\n"
        "Press SPACE to continue"
    )

    show_fixation(1.0)

    # Show competing gratings
    show_instructions(
        "Watch the overlapping patterns.\n"
        "Press '1' when you see the LEFT pattern dominating\n"
        "Press '2' when you see the RIGHT pattern dominating\n"
        "Press '3' when you see BOTH equally\n\n"
        "Observe for 15 seconds. Press SPACE to start."
    )

    clock = core.Clock()
    responses = []

    while clock.getTime() < 15:
        # Simulate rivalry with opacity fluctuation
        left_grating.opacity = 0.3 + 0.4 * np.sin(clock.getTime() * 2)
        right_grating.opacity = 0.7 - 0.4 * np.sin(clock.getTime() * 2)

        left_grating.draw()
        right_grating.draw()
        response_text.text = f"Time remaining: {15 - int(clock.getTime())}s"
        response_text.draw()
        win.flip()

        keys = event.getKeys(keyList=['1', '2', '3'])
        if keys:
            responses.append((clock.getTime(), keys[0]))

    show_instructions(
        f"You made {len(responses)} perceptual switches.\n\n"
        "This demonstrates that observation is not passive.\n"
        "Your brain actively selects what to perceive\n"
        "from ambiguous sensory input.\n\n"
        "Press SPACE to continue",
        duration=None
    )

def trial_2_ambiguous_perception():
    """
    Trial 2: The Necker Cube
    Demonstrates multiple valid interpretations of the same stimulus
    """
    show_instructions(
        "TRIAL 2: AMBIGUOUS PERCEPTION\n\n"
        "You will see a Necker Cube - an ambiguous figure\n"
        "that can be perceived in two different 3D orientations.\n\n"
        "The physical stimulus doesn't change,\n"
        "but your perception will spontaneously flip\n"
        "between two interpretations.\n\n"
        "This shows that 'reality' depends on the observer.\n\n"
        "Press SPACE to continue"
    )

    show_fixation(1.0)

    show_instructions(
        "Stare at the cube.\n\n"
        "Press '1' each time you see it flip to a new orientation.\n\n"
        "Observe for 20 seconds. Press SPACE to start."
    )

    clock = core.Clock()
    flip_count = 0

    while clock.getTime() < 20:
        for line in necker_cube:
            line.draw()
        response_text.text = f"Flips detected: {flip_count} | Time: {20 - int(clock.getTime())}s"
        response_text.draw()
        win.flip()

        keys = event.getKeys(keyList=['1'])
        if keys:
            flip_count += 1

    show_instructions(
        f"You experienced {flip_count} perceptual reversals.\n\n"
        "The same physical stimulus was interpreted\n"
        "in different ways by your visual system.\n\n"
        "This demonstrates observer-dependent reality:\n"
        "What you observe depends not just on what's 'out there'\n"
        "but on how your mind constructs meaning.\n\n"
        "Press SPACE to continue"
    )

def trial_3_change_blindness():
    """
    Trial 3: Change Blindness
    If we don't observe it, does it exist for us?
    """
    show_instructions(
        "TRIAL 3: UNOBSERVED CHANGES\n\n"
        "If a change occurs but you don't observe it,\n"
        "did it happen in your subjective reality?\n\n"
        "You will see two colored squares briefly.\n"
        "One square will change color.\n\n"
        "Can you detect which one changed?\n\n"
        "Press SPACE to continue"
    )

    correct_detections = 0
    trials = 5

    for trial in range(trials):
        show_fixation(0.5)

        # Show original scene
        scene_a.draw()
        scene_b.draw()
        win.flip()
        core.wait(0.5)

        # Brief blank
        win.flip()
        core.wait(0.2)

        # Show changed scene (left square changes color)
        scene_change.draw()
        scene_b.draw()
        win.flip()
        core.wait(0.5)

        # Collect response
        instructions.text = "Which square changed?\nPress 'L' for LEFT or 'R' for RIGHT"
        instructions.draw()
        win.flip()

        keys = event.waitKeys(keyList=['l', 'r'])
        if 'l' in keys:
            correct_detections += 1
            feedback = "Correct!"
        else:
            feedback = "Incorrect. The LEFT square changed from RED to GREEN."

        show_instructions(
            feedback + "\n\nPress SPACE for next trial",
            duration=None
        )

    show_instructions(
        f"You detected {correct_detections}/{trials} changes.\n\n"
        "Change blindness shows that unobserved changes\n"
        "effectively don't exist in our conscious experience.\n\n"
        "This relates to the Anthropic Principle:\n"
        "We can only know about what we actually observe.\n\n"
        "Unobserved aspects of reality remain unknown to us.\n\n"
        "Press SPACE to continue"
    )

def trial_4_metacognition():
    """
    Trial 4: Observing the Observer
    Metacognitive awareness - thinking about thinking
    """
    show_instructions(
        "TRIAL 4: OBSERVING THE OBSERVER\n\n"
        "Now turn your attention inward.\n\n"
        "For the next 30 seconds, try to observe\n"
        "your own thought process.\n\n"
        "Notice when your mind wanders.\n"
        "Notice the act of noticing.\n\n"
        "This is metacognition - consciousness observing itself.\n\n"
        "Press SPACE to begin meditation"
    )

    # Guided metacognition
    clock = core.Clock()
    prompts = [
        (5, "Notice your breathing..."),
        (10, "Observe your thoughts..."),
        (15, "Notice that you are noticing..."),
        (20, "Who is the observer?"),
        (25, "Can the observer observe itself?"),
    ]

    prompt_index = 0

    while clock.getTime() < 30:
        if prompt_index < len(prompts) and clock.getTime() >= prompts[prompt_index][0]:
            instructions.text = prompts[prompt_index][1]
            prompt_index += 1

        instructions.draw()
        response_text.text = f"Time: {int(clock.getTime())}/30s"
        response_text.draw()
        win.flip()

    show_instructions(
        "You just engaged in recursive self-observation:\n"
        "The observer observing the observer observing...\n\n"
        "This creates an infinite regress.\n\n"
        "The Anthropic Principle raises similar questions:\n"
        "- Who observes the universe?\n"
        "- Does observation create reality?\n"
        "- Can the universe observe itself through us?\n\n"
        "Press SPACE to continue"
    )

# --- Main Experiment Flow ---

def run_experiment():
    """Execute all experimental trials"""

    # Welcome screen
    show_instructions(
        "ANTHROPIC PRINCIPLE IN PSYCHOLOGY\n\n"
        "An Experimental Demonstration\n\n"
        "This experiment explores how observation\n"
        "shapes reality through four paradigms:\n\n"
        "1. Observer Selection\n"
        "2. Ambiguous Perception\n"
        "3. Change Blindness\n"
        "4. Metacognition\n\n"
        "Press SPACE to begin"
    )

    # Run trials
    trial_1_observer_selection()
    trial_2_ambiguous_perception()
    trial_3_change_blindness()
    trial_4_metacognition()

    # Conclusion
    show_instructions(
        "CONCLUSION\n\n"
        "The Anthropic Principle reminds us that:\n\n"
        "• Observation is not passive but active construction\n"
        "• We can only know what our cognitive systems permit\n"
        "• The observer and observed are fundamentally connected\n"
        "• Reality is observer-dependent\n\n"
        "In psychology, this means:\n"
        "All our experiments reveal human-universe interactions,\n"
        "not objective reality independent of observation.\n\n"
        "Thank you for participating!\n\n"
        "Press SPACE to exit"
    )

    # Cleanup
    win.close()
    core.quit()

# --- Run ---
if __name__ == '__main__':
    run_experiment()
