##############.  No need to do anything but run the script. Enjoy! #################
print('----------------------------------------------------------------------------')
print ('github.com/DustyDevelops | Simple Addition  | How many can you get correct?')
print('---------------------------                  -------------------------------')
print('                    Enter answers & press return.                           ')
print('----------------------------------------------------------------------------','\n')
#####################################################################################
import random
print('DIFFICULTY: type easy, medium, hard, harder, or hardest and press return')
difficulty = input('')
min = float(0)
max = float(10)
if difficulty == 'easy':
    min = min
    max = max
if difficulty == 'medium':
    min = min
    max = max * 10
if difficulty == 'hard':
    min = min
    max = max * 100
if difficulty == 'harder':
    min = min
    max = max * 1000

    
startTest = True
score = 100
correct = 0
wrong = 0

totalAsked = 0

while startTest == True:
    print()
    
    
 

    value1 = random.randint(min, max)
    value2 = random.randint(min, max)
    totalAsked +=1
    print('|Question:', totalAsked ,'|','\n')
    print(value1,'+', value2, ' = ','\n')

    correctAnswer = float(value1+value2)
    totalAnswered = float(correct + wrong)
    
    studentAnswer = float(input(''))
    
    if correctAnswer == studentAnswer:
        print('You are correct! The answer is', correctAnswer)
        correct +=1
        score = float((correct/totalAsked)*100)
    else:
            print('WRONG! The correct answer is,', correctAnswer)
            wrong +=1
            score = float((correct/totalAsked)*100)

    print('----------------------------------------------------------------------------')
    print('Questions:',correct+wrong)

    print('Correct:', correct)
    print('Incorrect:',wrong)
    print('Score =', score,'%')
    print('----------------------------------------------------------------------------')
    
    totalAnswered +=1
    
    if  score >= 100.0 and totalAnswered >= 5:
        print('----------------------------------------------------------------------------')
        print('----------------------------------------------------------------------------')
        print('--                                                                        --')
        print('                          You are on fire!                                  ')
        print('                                                                            ')
        print('     The difficulty will now increase by a factor of 10                     ')
        print('--                                                                        --')
        print('----------------------------------------------------------------------------')
        print('----------------------------------------------------------------------------')
        min = min
        max = max * 10 
 

