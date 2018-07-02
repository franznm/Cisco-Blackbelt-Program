import random
rd = random.randint(1,10)
while True:
    number = int(input("Guess the number: "));
    if number == rd:
        print("Correct!");   
        break
    elif number!= rd:
        print("Wrong, try again!"); 
    