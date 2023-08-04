
## Alarm-Clock
This Python script implements a simple countdown timer (chrono) with an alarm using the `playsound` library. The script allows you to specify the number of minutes and seconds to wait before the alarm goes off.


 
## Requirements
- Python 3.x
- playsound 1.2.2 (Install using pip install playsound)
## Start the project
- Make sure you have Python installed on your system.
- Install the required playsound library by running:

1. Copy code
`pip install playsound==1.2.2`

2. Run the script and provide the number of minutes and seconds you want to wait.
3. The countdown timer will start, and the remaining time will be displayed on the terminal in the format "mm:ss".
4. When the specified time elapses, an alarm sound ("iphone_alarm.mp3") will play to notify you.
## Description
- The script starts by importing the necessary modules, playsound and time.
It then defines two constant variables, CLEAR and CLEAR_AND_RETURN, which are ANSI escape sequences to clear the terminal screen and move the cursor to the top-left position.

- The alarm function takes the total number of seconds as input and runs a countdown timer using a while loop. Inside the loop, the script uses time.sleep(1) to pause for 1 second and updates the time_elapsed variable.

- The remaining time in minutes and seconds is calculated from the time_left variable. The script uses string formatting to display the time in the format "mm:ss".

- Once the countdown timer is complete, the playsound function is called to play the "iphone_alarm.mp3" sound file, indicating that the specified time has elapsed.

- Example Usage
```minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds

alarm(total_seconds)
```
- In this example, the user is prompted to enter the number of minutes and seconds they want to wait, and then the alarm function is called with the total number of seconds.