import os, subprocess, time, argparse

# Adds command parser
parser = argparse.ArgumentParser(description='Kill all processes with the term')
parser.add_argument('process', metavar='processName', type=str, help='process name')
arg = parser.parse_args().process.lower()

# Determine whether or not the user has a SHELL environment variable set/Is running script on a non-Linux machine
SHELL=os.getenv('SHELL')
if SHELL==None:
    exit("You don't have a shell environment variable set or you're trying to run this on a non-Linux machine!")

# Stores the command output as an array
cmdoutput=str(subprocess.check_output("ps -eo pid,command",shell=True).decode("utf-8")).split()
last=""

# Searches for the thingtokill value in each case-lowered element from the command output array
for process in cmdoutput:
    if arg in str(process).lower():
        time.sleep(0.04)
        os.system("kill -kill " + last)
    else:
        last=str(process)
