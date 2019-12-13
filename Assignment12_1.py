import psutil

def DisplayProcess():
    listProcess = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['name','pid','username'])

            listProcess.append(pinfo)

        except:(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess)
        pass

    return listProcess;


def main():
    print("----  Automation script which display information of running processes as its Name, PID,Username  ---- ")

    listProcess = DisplayProcess();

    for pobj in listProcess:
        print(pobj)
        print()


if __name__ == "__main__":
    main();
