from sys import argv
import psutil

def DisplayInformation(ProcessName):

    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if ProcessName.lower() == proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def main():
    print("----  Automation script which accept process name and display information of that process if it is running. ----")

    processName = argv[1];

    result = DisplayInformation(processName)

    if(result):
        print("Process %s is running"%processName)
    else:
        print("Process %s is not running" % processName)

if __name__ == "__main__":
    main();
