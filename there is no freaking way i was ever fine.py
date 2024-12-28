# fine.py

def calculate_fine(speed, speed_limit):
    """Calculate the fine for speeding."""
    try:
        if speed <= speed_limit:
            return 0
        else:
            fine = (speed - speed_limit) * 10
            return fine
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    speed = 80
    speed_limit = 60
    print(f"Speed: {speed}, Speed Limit: {speed_limit}")

    fine = calculate_fine(speed, speed_limit)
    print(f"The fine is: ${fine}")

if __name__ == "__main__":
    main()
