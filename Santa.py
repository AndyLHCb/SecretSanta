import smtplib
from getpass import getpass
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from random import choice

#setting up the sending email address
username = "Warwick.secretsanta"
domain = "gmail.com"
email = username + "@" + domain
pword = getpass() #Password for the Warwick.secretsanta@gmail.com account

recipients = {"Andy"   : "Andy.Morris@warwick.ac.uk",
              "Ross"   : "Ross.Hunter@warwick.ac.uk",
              "Flavia" : "Flavia.Cicala@warwick.ac.uk",
              "Mousam" : "Mousam.Rai@warwick.ac.uk",
              "Bryn"   : "Bryn.Roberts@warwick.ac.uk",
              "Eleanor": "Eleanor.Jones.1@warwick.ac.uk"}

#Making sure no-one gets 2 presents
usedNames = []

#Logging onto the email client
server = smtplib.SMTP("smtp." + domain,587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,pword)

#Working out who's sending to whom
for key in recipients.keys():
    sendTo = recipients[key]
    while(True):
        recipientName = choice(recipients.keys())
        recipientEmail= recipients[recipientName]

        if (recipientEmail != sendTo) and (not (recipientName in usedNames)):
            usedNames += [recipientName]
            break

    #Message to be sent
    msg = MIMEMultipart()
    msg['Subject'] = "Secret Santa"
    
    body = "Your secret santa is for: " + recipientName    

    msg.attach(MIMEText(body,'plain'))
    text = msg.as_string()

    server.sendmail(email, sendTo, text)
    del msg

server.quit()
