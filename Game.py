import random 

chances = 2

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]

number = random.choice(list1) 

guess = int(input ("put you guess:-"))

while chances <5:
    if guess == number :
        print ("you win")
       
    elif guess < number :
        print ("you guess was lower")
        break
    elif guess > number :
        print ("you guess was higher")
        break
if chances >5:
    print (("the number was",number))
    