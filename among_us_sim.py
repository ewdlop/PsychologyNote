
import sys
import time
import random
import math

# Try to import PsychoPy
try:
    from psychopy import visual, core, event, gui, data
except ImportError:
    print("Error: PsychoPy is not installed. Please install it using 'pip install psychopy'")
    sys.exit(1)

# Try to import pylsl for psychophysiology
try:
    from pylsl import StreamInfo, StreamOutlet
    LSL_AVAILABLE = True
except ImportError:
    print("Warning: pylsl not found. LSL markers will be printed to console instead.")
    LSL_AVAILABLE = False


class LSLHandler:
    """
    Handles sending markers to an LSL stream for psychophysiology integration.
    """
    def __init__(self, name="AmongUsMarkers", type="Markers", channel_count=1, nominal_srate=0, channel_format='string', source_id='amongus_psycho'):
        self.outlet = None
        if LSL_AVAILABLE:
            try:
                info = StreamInfo(name, type, channel_count, nominal_srate, channel_format, source_id)
                self.outlet = StreamOutlet(info)
                print(f"LSL Stream '{name}' created.")
            except Exception as e:
                print(f"Failed to create LSL stream: {e}")

    def send_marker(self, marker_string):
        """Sends a string marker."""
        if self.outlet:
            self.outlet.push_sample([marker_string])
            print(f"[LSL] Sent marker: {marker_string}")
        else:
            print(f"[MOCK LSL] {marker_string}")


class GameConfig:
    """
    Configuration settings for the game.
    """
    WINDOW_SIZE = [1024, 768]
    FULL_SCREEN = False
    BG_COLOR = 'black'
    PLAYER_SPEED = 3
    IMPOSTER_SPEED = 1.5
    PLAYER_SIZE = 30
    IMPOSTER_SIZE = 35
    TASK_RADIUS = 50


class Player:
    def __init__(self, win):
        self.win = win
        self.shape = visual.Circle(
            win,
            radius=GameConfig.PLAYER_SIZE/2,
            fillColor='cyan',
            lineColor='white',
            edges=32
        )
        self.shape.pos = [0, 0]
        self.visor = visual.Rect(
            win,
            width=GameConfig.PLAYER_SIZE * 0.7,
            height=GameConfig.PLAYER_SIZE * 0.4,
            fillColor='white',
            lineColor='black',
            pos=[5, 5] # Offset relative to body
        )
        self.speed = GameConfig.PLAYER_SPEED

    def update(self, keys, walls):
        """
        Update player position based on keyboard input and collision.
        keys: list of keys pressed
        walls: list of visual.Rect objects representing walls
        """
        dx, dy = 0, 0
        if 'left' in keys or 'a' in keys:
            dx = -self.speed
        if 'right' in keys or 'd' in keys:
            dx = self.speed
        if 'up' in keys or 'w' in keys:
            dy = self.speed
        if 'down' in keys or 's' in keys:
            dy = -self.speed

        # Predict new position
        new_x = self.shape.pos[0] + dx
        new_y = self.shape.pos[1] + dy

        # Simple Collision Detection (Bounding Box)
        # We check x and y separately to allow sliding against walls

        if not self.check_collision(new_x, self.shape.pos[1], walls):
            self.shape.pos[0] = new_x

        if not self.check_collision(self.shape.pos[0], new_y, walls):
            self.shape.pos[1] = new_y

        # Update visor position relative to body
        self.visor.pos = [self.shape.pos[0] + 5, self.shape.pos[1] + 5]

    def check_collision(self, x, y, walls):
        # Create a temporary bounding box for the player at (x, y)
        player_r = GameConfig.PLAYER_SIZE / 2
        p_left = x - player_r
        p_right = x + player_r
        p_top = y + player_r
        p_bottom = y - player_r

        for wall in walls:
            # Wall bounds
            w_width, w_height = wall.width, wall.height
            w_x, w_y = wall.pos
            w_left = w_x - w_width/2
            w_right = w_x + w_width/2
            w_top = w_y + w_height/2
            w_bottom = w_y - w_height/2

            # AABB Collision Check
            if (p_left < w_right and p_right > w_left and
                p_top > w_bottom and p_bottom < w_top):
                return True
        return False

    def draw(self):
        self.shape.draw()
        self.visor.draw()


class TaskZone:
    def __init__(self, win, pos, name):
        self.win = win
        self.pos = pos
        self.name = name
        self.completed = False
        self.shape = visual.Rect(win, width=40, height=40, pos=pos, fillColor='yellow', lineColor='orange')
        self.proximity_radius = 60

    def check_proximity(self, player_pos):
        dist = math.hypot(player_pos[0] - self.pos[0], player_pos[1] - self.pos[1])
        return dist < self.proximity_radius

    def highlight(self):
        self.shape.lineColor = 'white'
        self.shape.lineWidth = 3

    def unhighlight(self):
        self.shape.lineColor = 'orange'
        self.shape.lineWidth = 1

    def draw(self):
        if not self.completed:
            self.shape.draw()

    def run_task(self, win, lsl):
        # Base method, should be overridden
        return True

class WiringTask(TaskZone):
    def __init__(self, win, pos):
        super().__init__(win, pos, "WIRING")

    def run_task(self, win, lsl):
        # Simple wiring minigame: Click 4 buttons in order
        colors = ['red', 'blue', 'green', 'yellow']
        buttons = []
        for i, col in enumerate(colors):
            btn = visual.Circle(win, radius=20, fillColor=col, lineColor='white', pos=(-150 + i*100, 0))
            buttons.append(btn)

        target_seq = list(range(4))
        random.shuffle(target_seq)
        current_idx = 0

        task_running = True
        mouse = event.Mouse(win=win)
        mouse.setVisible(True)

        instruction = visual.TextStim(win, text="Click colors in order: " + ", ".join([colors[i] for i in target_seq]), pos=(0, 100))

        while task_running:
            instruction.draw()
            for btn in buttons:
                btn.draw()
            win.flip()

            if mouse.getPressed()[0]:
                for i, btn in enumerate(buttons):
                    if btn.contains(mouse):
                        if i == target_seq[current_idx]:
                            current_idx += 1
                            # Feedback
                            lsl.send_marker(f"WIRE_{current_idx}_CONNECTED")
                            core.wait(0.2) # Debounce
                            if current_idx >= 4:
                                mouse.setVisible(False)
                                return True
                        else:
                            # Error
                            lsl.send_marker("WIRE_ERROR")
                            pass
                while mouse.getPressed()[0]: pass # Wait for release

            if 'escape' in event.getKeys():
                mouse.setVisible(False)
                return False

        mouse.setVisible(False)
        return False

class DownloadTask(TaskZone):
    def __init__(self, win, pos):
        super().__init__(win, pos, "DOWNLOAD")

    def run_task(self, win, lsl):
        # Hold spacebar to fill bar
        bar_bg = visual.Rect(win, width=300, height=30, fillColor='gray', pos=(0,0))
        bar_fill = visual.Rect(win, width=0, height=30, fillColor='green', pos=(-150,0), anchor='left')
        # Note: older psychopy versions don't support 'anchor'. If this fails, we need manual pos calc.
        # But let's assume relatively recent psychopy. If not, the user can adapt.

        progress = 0
        instruction = visual.TextStim(win, text="Mash SPACE to download", pos=(0, 50))

        while progress < 100:
            keys = event.getKeys()
            if 'escape' in keys: return False

            if 'space' in keys:
                progress += 5

            # Update bar
            width = (progress / 100) * 300
            bar_fill.width = width
            # If anchor doesn't work, we'd do: bar_fill.pos = (-150 + width/2, 0)

            bar_bg.draw()
            bar_fill.draw()
            instruction.draw()
            win.flip()

        return True


def create_map(win):
    """
    Creates a simple map with walls.
    Returns a list of visual.Rect stimuli.
    """
    walls = []
    wall_color = 'gray'

    # Outer Borders
    w, h = GameConfig.WINDOW_SIZE
    thickness = 20

    # Top
    walls.append(visual.Rect(win, width=w, height=thickness, pos=(0, h/2 - thickness/2), fillColor=wall_color))
    # Bottom
    walls.append(visual.Rect(win, width=w, height=thickness, pos=(0, -h/2 + thickness/2), fillColor=wall_color))
    # Left
    walls.append(visual.Rect(win, width=thickness, height=h, pos=(-w/2 + thickness/2, 0), fillColor=wall_color))
    # Right
    walls.append(visual.Rect(win, width=thickness, height=h, pos=(w/2 - thickness/2, 0), fillColor=wall_color))

    # Internal Walls (Simple Layout)
    # Center block
    walls.append(visual.Rect(win, width=200, height=200, pos=(0, 0), fillColor=wall_color))

    # Room dividers
    walls.append(visual.Rect(win, width=20, height=300, pos=(-250, 100), fillColor=wall_color))
    walls.append(visual.Rect(win, width=300, height=20, pos=(250, -150), fillColor=wall_color))

    return walls


class Imposter:
    def __init__(self, win):
        self.win = win
        self.active = False
        self.shape = visual.Circle(
            win,
            radius=GameConfig.IMPOSTER_SIZE/2,
            fillColor='red',
            lineColor='darkred',
            edges=32
        )
        self.speed = GameConfig.IMPOSTER_SPEED
        self.knife = visual.Polygon(win, edges=3, radius=10, fillColor='silver', pos=(0,0))

    def spawn(self, player_pos):
        # Spawn far from player
        w, h = GameConfig.WINDOW_SIZE
        angle = random.uniform(0, 2*math.pi)
        dist = max(w, h) / 2

        # Determine spawn position outside/near edge
        sx = player_pos[0] + math.cos(angle) * 400
        sy = player_pos[1] + math.sin(angle) * 400

        # Clamp to screen bounds roughly
        sx = max(-w/2, min(w/2, sx))
        sy = max(-h/2, min(h/2, sy))

        self.shape.pos = [sx, sy]
        self.active = True

    def update(self, target_pos):
        if not self.active: return

        # Move towards target
        curr = self.shape.pos
        dx = target_pos[0] - curr[0]
        dy = target_pos[1] - curr[1]
        dist = math.hypot(dx, dy)

        if dist > 0:
            move_x = (dx / dist) * self.speed
            move_y = (dy / dist) * self.speed
            self.shape.pos = [curr[0] + move_x, curr[1] + move_y]

        # Despawn if too long? For now, relentless chase.

    def check_collision(self, target_pos):
        if not self.active: return False
        dist = math.hypot(target_pos[0] - self.shape.pos[0], target_pos[1] - self.shape.pos[1])
        # Collision if distance < sum of radii
        if dist < (GameConfig.PLAYER_SIZE/2 + GameConfig.IMPOSTER_SIZE/2):
            return True
        return False

    def draw(self):
        if self.active:
            self.shape.draw()


def main():
    print("Initializing Among Us Psychophysiology Simulation...")

    # 1. Setup LSL
    lsl_handler = LSLHandler()
    lsl_handler.send_marker("EXP_SETUP")

    # 2. Setup Window
    win = visual.Window(
        size=GameConfig.WINDOW_SIZE,
        fullscr=GameConfig.FULL_SCREEN,
        color=GameConfig.BG_COLOR,
        units='pix'
    )

    # 3. Setup Game Objects
    player = Player(win)
    walls = create_map(win)

    # Create Tasks
    tasks = []
    tasks.append(WiringTask(win, pos=(-200, -200)))
    tasks.append(DownloadTask(win, pos=(200, 200)))

    lsl_handler.send_marker("GAME_START")

    # Main Game Loop
    clock = core.Clock()
    running = True

    # Initialize Imposter
    imposter = Imposter(win)
    imposter_timer = core.CountdownTimer(random.uniform(3, 8)) # Random spawn time

    # Simple input handling: Velocity Decay
    # If a key is pressed, velocity is set. Velocity decays every frame.
    player_vel = [0, 0]
    decay = 0.8

    while running:
        dt = clock.getTime() # Get time? No, getTime is absolute.
        # We just run frame by frame for simplicity.

        # Input
        keys = event.getKeys()
        if 'escape' in keys:
            running = False
            lsl_handler.send_marker("GAME_QUIT")

        # Velocity input (simulated "hold")
        if 'left' in keys or 'a' in keys:
            player_vel[0] = -GameConfig.PLAYER_SPEED
        if 'right' in keys or 'd' in keys:
            player_vel[0] = GameConfig.PLAYER_SPEED
        if 'up' in keys or 'w' in keys:
            player_vel[1] = GameConfig.PLAYER_SPEED
        if 'down' in keys or 's' in keys:
            player_vel[1] = -GameConfig.PLAYER_SPEED

        # Apply velocity with decay for smoother stop
        if abs(player_vel[0]) < 0.1: player_vel[0] = 0
        if abs(player_vel[1]) < 0.1: player_vel[1] = 0

        # Update Player
        active_move_keys = []
        if player_vel[0] < -0.5: active_move_keys.append('left')
        if player_vel[0] > 0.5: active_move_keys.append('right')
        if player_vel[1] > 0.5: active_move_keys.append('up')
        if player_vel[1] < -0.5: active_move_keys.append('down')

        player.update(active_move_keys, walls)

        # Decay velocity
        player_vel[0] *= decay
        player_vel[1] *= decay

        # Check task interaction
        for task in tasks:
            if not task.completed and task.check_proximity(player.shape.pos):
                task.highlight()
                if 'space' in keys:
                    lsl_handler.send_marker(f"TASK_START_{task.name}")
                    result = task.run_task(win, lsl_handler)
                    if result:
                        lsl_handler.send_marker(f"TASK_COMPLETE_{task.name}")
                        task.completed = True
            else:
                task.unhighlight()

        # Check win condition
        if all(t.completed for t in tasks):
            print("ALL TASKS COMPLETED!")
            lsl_handler.send_marker("GAME_WIN")
            win_text = visual.TextStim(win, text="VICTORY", color='lime', height=50)
            win_text.draw()
            win.flip()
            core.wait(2)
            running = False

        # Update Imposter
        if imposter.active:
            imposter.update(player.shape.pos)
            if imposter.check_collision(player.shape.pos):
                print("CAUGHT BY IMPOSTER!")
                lsl_handler.send_marker("DEATH_BY_IMPOSTER")
                # Visual Feedback
                fail_text = visual.TextStim(win, text="DEFEAT", color='red', height=50)
                fail_text.draw()
                win.flip()
                core.wait(2)
                running = False
        else:
            # Check spawn timer
            if imposter_timer.getTime() <= 0:
                imposter.spawn(player.shape.pos)
                lsl_handler.send_marker("IMPOSTER_SPAWN")
                imposter_timer.reset(random.uniform(10, 20)) # Respawn later

        # Draw
        for wall in walls:
            wall.draw()

        for task in tasks:
            task.draw()

        player.draw()
        imposter.draw()

        win.flip()

    win.close()
    core.quit()

if __name__ == "__main__":
    main()
