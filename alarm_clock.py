# install playsound 1.2.2 
from playsound import playsound
import time

# clear terminal command and start from the bottom of terminal the chrono and print every second on next line
CLEAR = "\033[2J"
# will be return on a same line and don't change the position when chrono run 
CLEAR_AND_RETURN = "\033[H"

"""The total number of seconds to wait. It initializes a variable time_elapsed to 0"""


def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)  # Variable CLEAR to clear the console or terminal screen before starting the alarm.
    while time_elapsed < seconds:  # This is a while loop that will keep running as long as the time_elapsed is less
        # Then the seconds value. It means the loop will continue until the desired alarm time is reached.
        time.sleep(1)  # This is done to simulate the passage of time
        time_elapsed += 1  # After each second, the time_elapsed variable is incremented by 1,
        # representing one more second that has passed.

        """These lines calculate the remaining time in minutes and seconds. It subtracts the time_elapsed from the total 
        seconds to get the remaining time and then calculates the minutes by using 
        integer division // to get the whole number of minutes and the remaining seconds using the modulo operator %."""
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60  # 125 sec // 60 = 2
        seconds_left = time_left % 60  # 125 % 60 = 5

        """This line prints the remaining time on the screen. It uses the constant variable CLEAR_AND_RETURN to clear 
        the console and move the cursor to the beginning of the line. 
        It then prints the minutes and seconds with leading zeros if necessary (using :02d formatting)."""
        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}")

    playsound("iphone_alarm.mp3")

    """The code outside the alarm function prompts the user for the number of minutes and seconds to wait, calculates 
the total seconds, and then calls the alarm function with the total seconds as an argument."""


minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds

alarm(total_seconds)
