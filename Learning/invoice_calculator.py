hourly_rate = float(input("Enter your hourly rate: "))
hours_worked = float(input("Enter hours worked: "))

total_invoice = hourly_rate * hours_worked

option = input("Would you like to add sales tax or a discount? (tax/discount): ")

if option.lower() == "tax":
    tax_rate = float(input("Enter sales tax rate (as a percentage): "))
    total_invoice += total_invoice * (tax_rate / 100)

elif option.lower() == "discount":
    discount_rate = float(input("Enter discount rate (as a percentage): "))
    total_invoice -= total_invoice * (discount_rate / 100)

print("\nInvoice Summary")
print("----------------")
print(f"Hourly Rate: ${hourly_rate:.2f}")
print(f"Hours Worked: {hours_worked}")
print(f"Total Invoice: ${total_invoice:.2f}")
