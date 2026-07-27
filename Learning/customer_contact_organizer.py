name = input("Enter customer name: ")
phone_number = input("Enter customer phone number: ")
email = input("Enter customer email: ")
existing_customer = input("Existing customer? (yes/no): ")

print("\nNew Customer")
print("Name:", name)
print("Phone Number:", phone_number)
print("Email:", email)

if existing_customer.lower() == "yes":
    print("Priority Customer")
else:
    print("Standard Customer")