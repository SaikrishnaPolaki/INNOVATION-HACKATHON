import smtplib
from email.message import EmailMessage



# ========== CONFIGURATION ==========
SENDER_EMAIL = "" # I Used Deepesh Mail ID For Testing.
SENDER_PASSWORD = ""   # Use App Password Here (IMPORTANT)

# List of recipient emails
recipients = [


   # All The Mail ID's Of Teams In A String By Separating With Comas. 
  
]

# Corresponding Team Names
teamNames = [
    
   # All The Team Names Of The Specific Event In A String By Separating With Comas. 
  
]
# Email Subject
subject = "Innovation Hackathon 2026 - Important Update"

# ========== SEND EMAILS ==========
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        for email, team in zip(recipients, teamNames):
            # Prepare email body for each team
            body = f"""
Dear Participant,

Greetings from the Innovation Hackathon Team!

You with {team} are selected for the Hackathon.

Thank you,
Team Innovation Hackathon
"""
            # Create a new EmailMessage for each email
            msg = EmailMessage()
            msg["From"] = SENDER_EMAIL
            msg["To"] = email
            msg["Subject"] = subject
            msg.set_content(body)

            # Send the email
            server.send_message(msg)
            print(f"Email sent to {team} -> {email}")

    print("\nAll emails sent successfully!")

except Exception as e:
    print("Error:", e)
