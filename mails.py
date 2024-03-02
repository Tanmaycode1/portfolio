import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def mailtoclient(email,name):
   sender_email = "tanmayarora118@gmail.com"
   receiver_email = email
   password = "qsghqbashgoysgle"

   message = MIMEMultipart("alternative")
   message["Subject"] = "Thanks for showing interest in our services we'll contact you soon"
   message["From"] = sender_email
   message["To"] = receiver_email


   text = """Dear {},

Thank you for reaching out! I've received your message and am currently reviewing the details. 
I appreciate your interest and will get back to you shortly with a personalized response. Your patience is valued.

Best regards,
Tanmay arora
""".format(name)


   part1 = MIMEText(text, "plain")

   message.attach(part1)

   context = ssl.create_default_context()
   with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
       server.login(sender_email, password)
       server.sendmail(
           sender_email, receiver_email, message.as_string()
       )

def mailtoourself(email,name,subject,message):
   sender_email = "examplemsit@gmail.com"
   receiver_email = "tanmayarora118@gmail.com"
   password = "smwtujbcmobbmbda"

   message = MIMEMultipart("alternative")
   message["Subject"] = "New client Alert"
   message["From"] = sender_email
   message["To"] = receiver_email


   text = """
   client request
   name :{}
   email:{}
   subject:{}
   message:{}
""".format(name,email,subject,message)


   part1 = MIMEText(text, "plain")

   message.attach(part1)

   context = ssl.create_default_context()
   with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
       server.login(sender_email, password)
       server.sendmail(
           sender_email, receiver_email, message.as_string()
       )
