
#Name: Abdur Rehman

#Email address: abdurshamsi68@gmail.com

#Complain Management System

print("=== Complaint Handling System ===")

print("Welcome to the Complaint Handling System.")

print("Please follow the prompts to submit your complaint and track its status.")

print("=================================")

# Collecting complaint details

complainer_name = input("please enter your name:")

print(f"name,{complainer_name}!")

complainer_number = input("enter number:")

print(f"number,{complainer_number}!")

complainer_email = input("enter email:")

print(f"email,{complainer_email}!")

complainer_text = input("enter text:")

print(f"text,{complainer_text}!")

# Complaint processing

complainer_status = ("received")

print(f"status,{complainer_status}!")

review_complain = ("complain reviewed")

print(f"review,{review_complain}!")

gather_information = ("gaher information about complain")

print(f"information,{gather_information}!")

responsibility = ("determine our responsibility")

print(f"responsibility,{responsibility}!")

analyze_complaint = ("analyze different solution")

print(f"analyze,{analyze_complaint}!")

implement = ("implement on the best solution")

print(f"implement,{implement}!")

if 'complaint_resolved':

    resolved_complain = "Your complaint is resolved."

    print(f"Resolved: {resolved_complain}")

else:

    still_working = "Your complaint is still being worked on."

    print(f"Status: {still_working}")

# Exiting the system

system = ("exit")

print(exit) 



