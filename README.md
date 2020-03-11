# esatsang
Automatically play eSatsang when login opens on the web page

The idea of this program is that it can be started at any time during the day and it will automatically start playing satsang whenever the live stream is made available.

By default, the program runs in 'headless' mode - this means that a browser will not actually be launched (but the audio will still play in the background). However, this can be changed in the code line if you want a browser to be launched.

`opts.headless = True`

The program has configuration (within the code, for now) to specify start time and end time ranges for morning and evening satsang. It will poll the website during these times and wait until the login is made available. Once the login page is available, it will automatically login (based on given credentials) and attempt to play the live audio stream.

Note that the program can be started at any time in the day - it will not do anything until the specified time windows for morning and evening satsang. I like to automate the start of the program as well using cron (or Task Scheduler in Windows).

Look for the following lines in the code:

```

MORNING_SATSANG_START_TIME = datetime.time(3, 0, 0)
MORNING_SATSANG_END_TIME = datetime.time(5, 0, 0)

EVENING_SATSANG_START_TIME = datetime.time(16, 0, 0)
EVENING_SATSANG_END_TIME = datetime.time(17, 0, 0)
```

# Pre-requisites
## 1. Install Python3

Download and install the latest Python3 version based on your OS from here - https://www.python.org/downloads/

## 2. Install selenium package for Python3

Typically, this can be done using the following command:

`pip3 install selenium`

## 3. Install Firefox (if not already installed)
The code currently expects Firefox to already be installed on the system.


# How to Run

Make sure your E-satsang login credentials are updated in the play_satsang.py file at the following lines:

```
ESATSANG_USERNAME = "" # Provide UID here
ESATSANG_PASSWORD = "YYYY-MM-DD" # Provide DOB here
```

Then, simply run this from a command prompt (or Terminal):

`python play_satsang.py`

The above command will start the process and print out what it's doing on the command line.

# Sample output

```
c:\esatsang>python play_satsang.py
2020-03-10 20:59:48.951448: Starting...
2020-03-10 20:59:51.673140: Doing nothing as current time not within expected range.
2020-03-10 20:59:51.674137: Will check again in 5 minutes...
```
