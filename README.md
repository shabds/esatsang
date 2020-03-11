# esatsang
Automatically play eSatsang when login opens on the web page

The idea of this program is that it can be started at any time during the day and it will automatically start playing satsang whenever the live stream is made available.

# How to Run

## 1. Download the file named DOWNLOAD_ME.zip and unpack its contents on your local system

## 2. Make sure your E-satsang login credentials are updated in the config.ini file:

```
ESATSANG_USERNAME = "" # Provide UID here
ESATSANG_PASSWORD = "YYYY-MM-DD" # Provide DOB here
```

## 3. Run the executable

The above command will start the process and print out what it's doing on the command line.

By default, the program runs in 'headless' mode - this means that a browser will not actually be launched (but the audio will still play in the background). However, this can be changed through configuration.

The program has configuration (config.ini) to specify start time and end hour ranges for morning and evening satsang. It will poll the website during these times and wait until the login is made available. Once the login page is available, it will automatically login (based on given credentials) and attempt to play the live audio stream.

Note that the program can be started at any time in the day - it will not do anything until the specified time windows for morning and evening satsang. I like to automate the start of the program as well using cron (or Task Scheduler in Windows).

Look for the following lines in config.ini and update them as required:

```
[MAIN]
ESATSANG_USERNAME = 
ESATSANG_PASSWORD = 

MORNING_SATSANG_START_HOUR =3
MORNING_SATSANG_END_HOUR =5

EVENING_SATSANG_START_HOUR =16
EVENING_SATSANG_END_HOUR =17

OVERRIDE_TIME_RESTRICTIONS = False

# Define wait time between login attempts, in minutes
WAITING_PERIOD = 5

HEADLESS=True
```

# Pre-requisites

## 1. Install Firefox (if not already installed)
The code currently expects Firefox to already be installed on the system.




