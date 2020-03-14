import zipfile 
import pyautogui
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

print("Don't worry it's working, it just takes a few seconds")
zip_file = zipfile.ZipFile('Test.zip', 'w')
#  The Directory of the file can be found my opening a terminal 'cd' into the correct folder then enter 'pwd' and copy below: 
zip_file.write('Change-to-your-choosen-Directory', compress_type=zipfile.ZIP_DEFLATED)
#  Zip the above file 
zip_file.write('Change-to-your-choosen-Directory', compress_type=zipfile.ZIP_DEFLATED)
#  Zip the above file 
zip_file.write('Change-to-your-choosen-Directory', compress_type=zipfile.ZIP_DEFLATED)
#  Zip the above file 
zip_file.close()

print("File compressed") 

#The mail addresses and password, in this example i'm using a gmail
#emailaddress
sender_address = 'gmail@gmail.com'
#emailaddress password
sender_pass = 'gmailpassword'
#smtp of gmail
smtp_server = 'smtp.gmail.com'
#port number of gmail's smtp_server, you can change to your owns if you like :D
smtp_port = 587
print("Email Login Successful")

#Setup mail content
mail_content = '''
		Demo content
	'''

#Setup global the MIME
message = MIMEMultipart()
message['Subject'] = 'Demo subject'
print("Email Subject Created")

#Body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#You'll need to change the directory to your file's location
attach_file_name = '/Users/lennisluigi/Desktop/Test.zip'
attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload) #encode the attachment
payload.add_header('Content-Disposition', 'attachment', filename=attach_file_name)
message.attach(payload)

#Create SMTP session 
session = smtplib.SMTP(smtp_server, smtp_port)
session.starttls() #enable security
session.login(sender_address, sender_pass) #login
text = message.as_string()
print("SMTP Session ceated and secuirty enabled")

#mail addresses of receivers
mails = ['Receiver@hotmail.co.uk', 'Receiver@gmail.com']

for receiver_address in mails:
	#Setup the MIME
	message['From'] = sender_address
	message['To'] = receiver_address
	session.sendmail(sender_address, receiver_address, text)
	print('Mail Sent: '+receiver_address)

print("Everything worked :D")

session.quit()
