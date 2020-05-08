##############.  No need to do anything but run the script. Enjoy! #################
print('----------------------------------------------------------------------------')
print ('github.com/DustyDevelops |THE WORST GAME EVER! | good luck ')
print('-----------------------------------------------------------------------------')
print('---------------------------      rules        -------------------------------')
print(' no calculator        Enter answers & press return.          no pen or paper ')
print('----------------------------------------------------------------------------','\n')
#####################################################################################
import random

min = float(0)
max = float(10)

startTest = True
score = 100
correct = 0
wrong = 0
totalAsked = 0

while startTest == True:

    value1 = random.randint(min, max)
    value2 = random.randint(min, max)
    totalAsked +=1
    print('|Question:', totalAsked ,'|')
    print(value1,'+', value2, ' = ')

    correctAnswer = float(value1+value2)
    totalAnswered = float(correct + wrong)
    
    studentAnswer = float(input(''))
    if correctAnswer == studentAnswer:
        print('HARDER!')
        correct +=1
        score = float((correct/totalAsked)*100)
    else:
            print('WRONG! YOU LOSE!')
            print('The correct answer is:', correctAnswer)
            wrong +=1
            score = float((correct/totalAsked)*100)
            print('-------------------------')
            print('You made it to question:', correct)
            print('goodbye')
            break

    totalAnswered +=1
    
    if  score >= 100.0:
        print('                                                           ')
        min = min
        max = max * 10 
 
    
