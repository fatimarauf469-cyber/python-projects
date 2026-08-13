score=0

answer=input("what is the capital of france?")

if answer=="paris":
    score+=1
else:
    print("Incorrect anwer")

answer=input("How mnay days are there in a week?")

if answer=="7":
    score+=1
else:
    print("Incorrect answer")

answer=input("What is the largest planet in our solar system?")

if answer=="jupiter":
    score+=1
else:
    print("Incorrect answer")

print("total score is:", score)

