# Basic GPS Tracker Program

def gps_tracker():
    print("🚗 Welcome to the Basic GPS Tracker!")
    print("Enter directions: N, S, E, W (or full words like North, south, etc.)")
    print('Type "STOP" to end the session.\n')

    # Starting position
    x, y = 0, 0

    while True:
        command = input("Enter direction: ").strip().lower()

        if command == "stop":
            break

        # Normalize valid commands
        if command in ['n', 'north']:
            y += 1
        elif command in ['s', 'south']:
            y -= 1
        elif command in ['e', 'east']:
            x += 1
        elif command in ['w', 'west']:
            x -= 1
        else:
            print("❌ Invalid input! Please enter N, S, E, W, or STOP.")
            continue

        print(f"📍 Current position: ({x}, {y})")

    # End of session
    print("\n🧭 Tracking session ended.")
    print(f"🏁 Final position: ({x}, {y})")

    if x == 0 and y == 0:
        print("✅ You returned to the origin (0, 0).")
    else:
        print("🚶 You did not return to the origin.")

# Run the program
if __name__ == "main":
    gps_tracker()