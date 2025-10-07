import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Hide the default pygame startup message

import pygame
import time

def alarm(seconds):
    print("\nAlarm will sound in:")
    time_elapsed = 0

    # Countdown loop
    while time_elapsed < seconds:
        time.sleep(1)                     # Wait for one second
        time_elapsed += 1                 # Increment elapsed time
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60    # Convert remaining seconds to minutes
        seconds_left = time_left % 60     # Remaining seconds after full minutes
        
        # Display the countdown timer on the same line
        print(f"\r{minutes_left:02d}:{seconds_left:02d}", end="", flush=True)

    pygame.mixer.init()
    pygame.mixer.music.load("samsung.mp3")
    pygame.mixer.music.play()

    print("\n\n⏰ Alarm ringing! Press Ctrl+C to stop.")

    # Keep the program running until the sound stops
    while pygame.mixer.music.get_busy():
        time.sleep(1)

minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds) # Start the alarm countdown