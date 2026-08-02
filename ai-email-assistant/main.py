import os

API_KEY = os.getenv("OPENAI_API_KEY")

customer_email = """
Hi,

I think I was charged twice for my last service appointment.

Could someone check my invoice?

Thank you,
Emily
"""

with open("sample_emails/emergency.txt", "r") as file:
    customer_email = file.read()