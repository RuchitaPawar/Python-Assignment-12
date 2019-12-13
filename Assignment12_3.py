import os
from sys import argv
import time
import psutil

def runningProcessLog(directoryName):
    listProcess = []

    # make directory if not exists.
    if not os.path.exists(directoryName):
        try:
            os.mkdir(directoryName)
        except:
            pass


    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['name','pid','username'])

            listProcess.append(pinfo)

        except:(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess)
        pass

    try:
        separator = "-" * 80
        absPath = os.path.abspath(directoryName)
        log_path = os.path.join(absPath, "RunningProcessLog_%s.log" % (time.ctime()))

        f = open(os.path.join(directoryName,"RunningProcessLog_%s.log" % (time.time())), "w")

       # f = open(os.path.join(directoryName, "RunningProcessLog.log"), "w")
        f.write(separator + "\n")
        f.write("Process logger" + time.ctime())
        f.write(separator + "\n")
        f.write("\n")

        for item in listProcess:
            f.write("%s\n" % item)
        f.close()
        print("Log file generated successfully.")
    except Exception as e:
        print("Exception occured:",e)

def main():
    print()
    print("""  ----  Automation script which accept directory name from user 
                     and create log file in that directory which contains
                     information of running processes as its name, PID, Username  ----
        """)
    print()

    dirName = argv[1]

    runningProcessLog(dirName);

if __name__ == "__main__":
    main();
