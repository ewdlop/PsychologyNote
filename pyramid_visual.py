from psychopy import visual, core, event
import math

# Initialize window
win = visual.Window([1000, 800], color="white", units="pix")

# Pyramid parameters
pyramid_levels = 5
blocks_per_level_base = 8  # Number of blocks in the bottom level
block_width = 80
block_height = 40
spacing = 5
start_y = -250

# Colors for different levels (gradient from bottom to top)
level_colors = [
    [-0.5, -0.5, -0.2],  # Sandy brown (bottom)
    [-0.3, -0.3, -0.1],  # Tan
    [-0.2, -0.2, 0.0],   # Light tan
    [-0.1, -0.1, 0.1],   # Very light tan
    [0.0, 0.0, 0.2],     # Near white (top)
]

# Title text
title = visual.TextStim(
    win,
    text="Pyramid Structure Visualization",
    pos=(0, 350),
    color=[-1, -1, -1],
    height=30,
    bold=True
)

# Info text
info_text = visual.TextStim(
    win,
    text="Press SPACE to animate | ESC to exit",
    pos=(0, -350),
    color=[-1, -1, -1],
    height=20
)

# Create pyramid blocks
def create_pyramid():
    """Create all blocks for the pyramid structure"""
    blocks = []
    labels = []
    
    for level in range(pyramid_levels):
        blocks_in_level = blocks_per_level_base - level
        total_width = blocks_in_level * block_width + (blocks_in_level - 1) * spacing
        start_x = -total_width / 2 + block_width / 2
        y_pos = start_y + level * (block_height + spacing)
        
        for i in range(blocks_in_level):
            x_pos = start_x + i * (block_width + spacing)
            
            # Create block
            block = visual.Rect(
                win,
                width=block_width,
                height=block_height,
                fillColor=level_colors[level],
                lineColor=[-0.8, -0.8, -0.8],
                lineWidth=2,
                pos=(x_pos, y_pos)
            )
            blocks.append(block)
            
            # Create label for the level
            if i == blocks_in_level // 2:  # Only label middle block of each level
                label = visual.TextStim(
                    win,
                    text=f"Level {pyramid_levels - level}",
                    pos=(x_pos, y_pos),
                    color=[-1, -1, -1],
                    height=15,
                    bold=True
                )
                labels.append(label)
    
    return blocks, labels

# Create statistics text
def create_statistics():
    """Create text showing pyramid statistics"""
    stats = []
    
    # Calculate statistics
    total_blocks = sum(blocks_per_level_base - i for i in range(pyramid_levels))
    
    stat_x = 400
    stat_y_start = 250
    stat_spacing = 40
    
    stats_data = [
        f"Total Levels: {pyramid_levels}",
        f"Total Blocks: {total_blocks}",
        f"Base Width: {blocks_per_level_base}",
        f"Growth Rate: -1/level",
        f"Shape: Hierarchical"
    ]
    
    for i, stat in enumerate(stats_data):
        text = visual.TextStim(
            win,
            text=stat,
            pos=(stat_x, stat_y_start - i * stat_spacing),
            color=[-1, -1, -1],
            height=20,
            alignText='left'
        )
        stats.append(text)
    
    return stats

# Create people icons to show pyramid scheme structure
def create_people_representation():
    """Create a representation of people in pyramid scheme"""
    people = []
    people_per_level = [1, 3, 9, 27, 81]  # Exponential growth
    
    person_y_start = 200
    person_spacing_y = 50
    
    for level_idx in range(min(4, pyramid_levels)):  # Show first 4 levels
        count = people_per_level[level_idx]
        y_pos = person_y_start - level_idx * person_spacing_y
        
        # Calculate spacing to fit all people
        if count <= 10:
            person_spacing_x = 60
        else:
            person_spacing_x = 800 / count
            
        total_width = (count - 1) * person_spacing_x
        start_x = -total_width / 2
        
        # Draw up to 10 people per level (to avoid clutter)
        display_count = min(count, 10)
        
        for i in range(display_count):
            x_pos = start_x + i * person_spacing_x
            
            # Simple circle to represent person
            person = visual.Circle(
                win,
                radius=10,
                fillColor=[0.3, 0.3, 0.8],
                lineColor=[-0.8, -0.8, -0.8],
                lineWidth=1,
                pos=(x_pos, y_pos)
            )
            people.append(person)
        
        # Add label showing actual count
        if count > display_count:
            label = visual.TextStim(
                win,
                text=f"(+{count - display_count} more)",
                pos=(start_x + display_count * person_spacing_x + 50, y_pos),
                color=[-1, -1, -1],
                height=12
            )
            people.append(label)
    
    return people

# Animation function
def animate_pyramid_construction(blocks, labels):
    """Animate the construction of the pyramid"""
    for i, block in enumerate(blocks):
        block.opacity = 0
    
    # Build from bottom to top
    for i, block in enumerate(blocks):
        block.opacity = 1
        
        # Draw all blocks up to current one
        for j in range(i + 1):
            blocks[j].draw()
        
        # Draw all labels
        for label in labels:
            label.draw()
        
        title.draw()
        info_text.draw()
        win.flip()
        core.wait(0.05)  # Small delay for animation effect

# Main visualization
def show_pyramid():
    """Display the complete pyramid"""
    blocks, labels = create_pyramid()
    stats = create_statistics()
    
    # Initial static display
    for block in blocks:
        block.draw()
    for label in labels:
        label.draw()
    for stat in stats:
        stat.draw()
    
    title.draw()
    info_text.draw()
    win.flip()
    
    # Wait for user input
    waiting = True
    while waiting:
        keys = event.getKeys()
        
        if 'space' in keys:
            # Animate pyramid construction
            for stat in stats:
                stat.draw()
            animate_pyramid_construction(blocks, labels)
            
            # Show final state with stats
            for block in blocks:
                block.draw()
            for label in labels:
                label.draw()
            for stat in stats:
                stat.draw()
            title.draw()
            info_text.draw()
            win.flip()
            
        elif 'escape' in keys:
            waiting = False
        
        core.wait(0.01)

# Alternative: Show pyramid scheme with people
def show_pyramid_scheme_people():
    """Display pyramid scheme representation with people"""
    win.color = [0.9, 0.9, 0.9]
    win.flip()
    
    people = create_people_representation()
    
    scheme_title = visual.TextStim(
        win,
        text="Pyramid Scheme: People Structure",
        pos=(0, 350),
        color=[-1, -1, -1],
        height=30,
        bold=True
    )
    
    warning_text = visual.TextStim(
        win,
        text="WARNING: This demonstrates exponential growth that is mathematically unsustainable",
        pos=(0, 300),
        color=[0.8, -0.8, -0.8],
        height=18,
        bold=True
    )
    
    level_labels = []
    levels_data = [
        ("Level 1 (Top)", 1, 150),
        ("Level 2", 3, 100),
        ("Level 3", 9, 50),
        ("Level 4", 27, 0),
    ]
    
    for label_text, count, y_offset in levels_data:
        label = visual.TextStim(
            win,
            text=f"{label_text}: {count} people",
            pos=(-450, 200 - y_offset),
            color=[-1, -1, -1],
            height=16,
            alignText='left'
        )
        level_labels.append(label)
    
    # Draw everything
    scheme_title.draw()
    warning_text.draw()
    
    for person in people:
        person.draw()
    
    for label in level_labels:
        label.draw()
    
    info_text.text = "Press 'B' to go back | ESC to exit"
    info_text.draw()
    
    win.flip()
    
    # Wait for user input
    waiting = True
    while waiting:
        keys = event.getKeys()
        
        if 'b' in keys:
            win.color = "white"
            return True  # Go back to main view
        elif 'escape' in keys:
            return False  # Exit
        
        core.wait(0.01)
    
    return False

# Main program
def main():
    """Main program loop"""
    # Show the pyramid visualization
    show_pyramid()
    
    # Clean up
    win.close()
    core.quit()

if __name__ == "__main__":
    main()
