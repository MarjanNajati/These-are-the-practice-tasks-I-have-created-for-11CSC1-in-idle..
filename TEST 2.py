print("hello world")
credentials ={"David":"123456", "Alex":"password", "Maria":"qwerty", "Anna":"Dragon", "Marco":"baseball", "Antino":"abc123"}
print(credentials)

user=input("Enter your username")

if user in credentials:
    print("username registered")
else:
    print("username not registered")

answer=input("Please enter your password")
if user in credentials:
    print("You are in")
else:
    print("Wrong")

