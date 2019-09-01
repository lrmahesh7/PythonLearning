first_name=str(input("please enter first name:"))
middle_name=str(input("please enter middle name:"))
last_name=str(input("please enter last name:"))
format_name=f"{first_name}{middle_name:2s}{last_name}"
print(format_name)