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
assert(namesL > 1)

#Shuffling Names
test = True
while(test):
    sfflNames = sample(names,namesL)
    test = any([sfflNames[i] == names[i] for i in range(namesL)])

#Logging onto the email client
server = smtplib.SMTP("smtp." + domain,587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,pword)

#Working out who's sending to whom
for i in range(namesL):
    sendTo = recipients[names[i]] #Person receiving the email

    recipientName = sfflNames[i]  #Person receiving the gift
       
    #Message to be sent
    msg = MIMEMultipart()
    msg['Subject'] = "Secret Santa"
    
    body = "\nYour secret santa is for: " + recipientName    

    msg.attach(MIMEText(body,'plain'))
    text = msg.as_string()

    #print("sending from: " + sendTo + " to " + recipientName)
    server.sendmail(email, sendTo, text)
    del msg

server.quit()
