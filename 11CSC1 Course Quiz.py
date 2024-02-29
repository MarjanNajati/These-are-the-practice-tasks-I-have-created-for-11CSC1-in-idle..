# Initialize score
score = 0

# Question 1
print("What country was Mr Coker born?")
print("a) New Zealand")
print("b) England")
print("c) Australia")
answer = input("Your answer: ").strip().lower()
if answer == 'b':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 2
print("\nWhere did he grow up?")
print("a) Auckland")
print("b) Palmerston North")
print("c) New Plymouth")
answer = input("Your answer: ").strip().lower()
if answer == 'c':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 3
print("\nHow many kids does he have?")
print("a) 1")
print("b) 2")
print("c) 3")
answer = input("Your answer: ").strip().lower()
if answer == 'b':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 4
print("\nHow many credits are in this course?")
print("a) 22")
print("b) 20")
print("c) 15")
answer = input("Your answer: ").strip().lower()
if answer == 'b':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 5
print("\nHow many internals are there?")
print("a) 1")
print("b) 2")
print("c) 3")
answer = input("Your answer: ").strip().lower()
if answer == 'b':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 6
print("\nHow many externals will you sit at the end of the year?")
print("a) 0")
print("b) 1")
print("c) 2")
answer = input("Your answer: ").strip().lower()
if answer == 'a':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Display final score
print("\nYou scored", score, "out of 6.")
