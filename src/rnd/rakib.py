import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email server details
username = "noreply@immican.ai"
password = "Ayratech1234"
incoming_server = "mail.immican.ai"
outgoing_server = "mail.immican.ai"
smtp_port = 465

# Sender and recipient email addresses
sender_email = "noreply@immican.ai"
recipient_email = "rakibahmed412245@gmail.com"

# Message details
subject = "Test Email"
body = "Hello, this is a test email from Python!"

# Create the MIME object
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Connect to the SMTP server
with smtplib.SMTP_SSL(outgoing_server, smtp_port) as server:
    # Log in to the email account
    server.login(username, password)

    # Send the email
    server.sendmail(sender_email, recipient_email, message.as_string())

print("Email sent successfully!")
