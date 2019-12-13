import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from sys import argv
import time
import psutil
import urllib.request as urllib2


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

        fileName = (os.path.join(directoryName,"RunningProcessLog_%s.log" % (time.time())))
        f = open(fileName, "w")

        f.write(separator + "\n")
        f.write("Process logger" + time.ctime())
        f.write(separator + "\n")
        f.write("\n")

        for item in listProcess:
            f.write("%s\n" % item)
        f.close()

        connected = isConnected()

        if connected:
             MailSender(fileName,time.ctime())
        else:
            print("Please check your internet connection..")

    except Exception as e:
        print("Exception occured:",e)


def MailSender(filename, time):
    try:
        fromaddr = "ruchita1796@gmail.com"
        toaddr = argv[2]

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr

        body = """  
          Hello %s,
            Please find the attached doucuments which contains Log of running process.
            This is an auto generated mail

         Thanks & Regards,
            Ruchita Pawar
            """% (toaddr)

        Subject = """
         Process Log generated at
         %s
        """ % (time)

        msg['Subject'] = Subject
        msg.attach(MIMEText(body, 'plain'))

        attachment = open(filename, "rb")

        p = MIMEBase('application', 'octet-stream')

        p.set_payload((attachment).read())

        encoders.encode_base64(p)

        p.add_header('Content Desposition', "attachment;filename =%s" % filename)

        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()

        # enter password while sending mail
        s.login(fromaddr, "-- password here --")

        text = msg.as_string()

        s.sendmail(fromaddr, toaddr, text)

        s.quit()

        print("Log file successfully sent through mail")

    except Exception as E:
        print("Unable to send mail", E)


def isConnected():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err:
        return False


def main():
    print()
    print("""  ---- Automation script which accept directory name and mail id from user and create log
                    file in that directory which contains information of running processes as its name, PID,
                    Username. After creating log file send that log file to the specified mail.  ----
        """)
    print()

    dirName = argv[1]

    runningProcessLog(dirName);

if __name__ == "__main__":
    main();
