from pathlib import Path

# ----------------------------
# Load the prompt
# ----------------------------

prompt_path = Path(__file__).parent / "prompts" / "email_summary.txt"

with open(prompt_path, "r") as file:
    prompt = file.read()

# ----------------------------
# Load customer email
# ----------------------------

email_path = Path(__file__).parent / "sample_emails" / "emergency.txt"

with open(email_path, "r") as file:
    customer_email = file.read()

print("Customer Email")
print("----------------")
print(customer_email)

# ----------------------------
# Simulated AI Response
# ----------------------------

customer_name = "Sarah"
summary = "Customer's furnace is not working."
priority = "High"
service_requested = "Emergency furnace repair"
draft_reply = """
Hi Sarah,

We're sorry to hear your furnace stopped working.

We'll do our best to schedule a technician as soon as possible.

Thank you,
HVAC Team
"""

# ----------------------------
# Display Results
# ----------------------------

print("\nAnalysis")
print("----------------")
print(f"Customer Name: {customer_name}")
print(f"Summary: {summary}")
print(f"Priority: {priority}")
print(f"Service Requested: {service_requested}")

print("\nDraft Reply")
print("----------------")
print(draft_reply)

if priority.lower() == "high":
    print("⚠️ Immediate Attention Recommended")