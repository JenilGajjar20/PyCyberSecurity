import psutil
import smtplib
import os
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = 'your_email@example.com'
email_pass = 'your_password'
email_send = 'email@example.com'

log_file = 'system_monitor.log'


def getSystemInfo():
    disk_usage = psutil.disk_usage('/')
    free_disk_space = disk_usage.free // (2**30)
    active_processes = len(psutil.pids())

    return free_disk_space, active_processes


def writeLog(free_disk_space, active_processes):
    with open(log_file, 'a') as f:
        log_message = f"{datetime.now()}: Free Disk Space: {free_disk_space} GB, Active Processes: {active_processes}\n"
        f.write(log_message)

def sendEmail():
    subject = 'Daily Server Log'
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['subject'] = subject

    body = 'Attached is the log file for the server status.'

    msg.attach(MIMEText(body, 'plain'))

    if os.path.exists(log_file):
        with open(log_file, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)

            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(log_file)}')

            msg.attach(part)

    text = msg.as_string()
    attachment.close()

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(email_user, email_pass)
        server.sendmail(email_user, email_send, text)

if __name__ == '__main__':
    free_disk_space, active_processes = getSystemInfo()
    print(f"Free Disk Space: {free_disk_space} GB, Active Processes: {active_processes}")

    writeLog(free_disk_space, active_processes)

    sendEmail()