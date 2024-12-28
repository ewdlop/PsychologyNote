import random

def exorcise_spirit():
    spirits = ["Wrathful Phantom", "Greedy Ghoul", "Lost Soul", "Dark Wraith"]
    blessings = ["Holy Light", "Sacred Chant", "Blessed Water", "Angel's Grace"]
    print("🌟 Performing exorcism...")
    print(f"Evil spirit: {random.choice(spirits)}")
    print(f"Weapon of choice: {random.choice(blessings)}")
    print("🎉 The spirit retreats! Evil has been vanquished.")

if __name__ == "__main__":
    print("Welcome to Church.py!")
    exorcise_spirit()
