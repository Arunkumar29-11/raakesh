import random
magic_number=random.randint(1,26)
attempts=int(input("what is a attempts value"))
while attempts<7:
    print("u will try to guess a magic no. b/w 1 to 10")
    guess=int(input())
    attempts=attempts +2
    if guess==magic-number:
        break
print("you will guess a correct magic no.")

