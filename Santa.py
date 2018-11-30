import smtplib
from getpass import getpass
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from random import sample

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
names = recipients.keys()
namesL= len(names)

test = False
while(not test):
    sfflNames = sample(recipients.keys(),namesL)
    test = not any([sfflNames[i] == names[i] for i in range(namesL)])


#Making sure no-one gets 2 presents
usedNames = []

#Logging onto the email client
server = smtplib.SMTP("smtp." + domain,587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,pword)

#Working out who's sending to whom
for i in range(namesL):
    sendTo = recipients[names[i]]

    recipientName = sfflNames[i]
    recipientEmail= recipients[recipientName]
       
    #Message to be sent
    msg = MIMEMultipart()
    msg['Subject'] = "Secret Santa"
    
    body = "Your secret santa is for: " + recipientName    

    msg.attach(MIMEText(body,'plain'))
    text = msg.as_string()

    #print("sending from: " + sendTo + " to " + recipientName)
    server.sendmail(email, sendTo, text)
    del msg

server.quit()
