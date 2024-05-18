import argparse
import time
import pyttsx3

# Setting up argument parser
parser = argparse.ArgumentParser(description='Timer with optional message.')
parser.add_argument('--seconds', type=int, default=0, help='Number of seconds to sleep (default: 0)')
parser.add_argument('--minutes', type=int, default=0, help='Number of minutes to sleep (default: 0)')
parser.add_argument('--hours', type=int, default=0, help='Number of hours to sleep (default: 0)')
parser.add_argument('--repeat-times', type=int, default=3, help='Number of times to repeat the message (default: 3)')
parser.add_argument('--message', type=str, default='Time is up', help='Message to repeat (default: "Time is up")')
args = parser.parse_args()

# Calculate total sleep time
sleep_time = args.seconds + args.minutes * 60 + args.hours * 3600

# Sleep for the specified time
time.sleep(sleep_time)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Repeat the message for the specified times
for i in range(args.repeat_times):
    engine.say(args.message)
    engine.runAndWait()
