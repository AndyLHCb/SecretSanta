import smtplib
from getpass import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import sample

#setting up the sending email address
username = "Warwick.secretsanta"
domain = "gmail.com"
email = username + "@" + domain
pword = getpass() #Password for the Warwick.secretsanta@gmail.com account

recipients = {"Andy"   : "Andy.Morris@warwick.ac.uk",
              "Ross"   : "Ross.Hunter@warwick.ac.uk",
              "Flavia" : "Flavia.Cicala@warwick.ac.uk",
              "Katy"   : "KatyIkin@gmail.com",
              "Bryn"   : "Bryn.Roberts@warwick.ac.uk",
              "Eleanor": "Eleanor.Jones.1@warwick.ac.uk"}
names = [*recipients]
namesL= len(names)
assert(namesL > 1)

#Shuffling Names
test = True
while(test):
    sfflNames = sample(names,namesL)
    test = any([sfflNames[i] == names[i] for i in range(namesL)])

#Logging onto the email client
server = smtplib.SMTP_SSL("smtp." + domain,465)
server.ehlo()
#server.starttls()
server.ehlo()
server.login(username,pword)

#Working out who's sending to whom
for i in range(namesL):
    sendTo = recipients[names[i]] #Person receiving the email

    recipientName = sfflNames[i]  #Person receiving the gift
       
    #Message to be sent
    msg = MIMEMultipart()
    msg['Subject'] = "R.E. Secret Santa"
    
    body = ("\nYour secret Santa is for: " + recipientName + ".\nThe spending limit is 5CHF.")

    msg.attach(MIMEText(body,'plain'))
    text = msg.as_string()

    #print("sending from: " + sendTo + " to " + recipientName)
    server.sendmail(email, sendTo, text)
    del msg

server.quit()
