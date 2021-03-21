import os, subprocess, time

print("Loading...")

# Determine whether or not the user has a SHELL environment variable set/Is running script on a non-Linux machine
SHELL=os.getenv('SHELL')
if SHELL==None:
    exit("You don't have a shell environment variable set or you're trying to run this on a non-Linux machine!")

# Stores the command output as an array
cmdoutput=str(subprocess.check_output("ps -eo pid,command",shell=True).decode("utf-8")).split()
last=""

print("Loaded! Terminating Spotify processes in-order to fix Spotify...\n")

# Searches for "spotify" in each case-lowered element from the command output array
for process in cmdoutput:
    if "spotify" in str(process).lower():
        time.sleep(0.04)
        os.system("kill -kill " + last)
        print("Killed Spotify process " + str(last))
    else:
        last=str(process)

print("\nDone! Try relaunching Spotify!")
