import getpass as g
import smtplib
from email.mime.text import MIMEText

body='''
I am Chandrani
BCA student
IEM college
'''
# create the mime text class object with body text
msg=MIMEText(body)

# from which mail id the mail id is sent
fromaddr="mukherjee.debjani75@gmail.com"

# to which the mail address is sent
# ishitabiswas2002@gmail.com

toaddr="ishitabiswas2002@gmail.com"

# store the addresses in msg object

msg['From']=fromaddr
msg['To']=toaddr
msg['Subject']="Hi Ishita!"

# connect to gmail.com server using 587 port number
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

# login to the server with your correct password
server.login(fromaddr,g.getpass("Enter the password \n"))
# send the message to the server
server.send_message(msg)

print("The mail is sent...")

server.quit()