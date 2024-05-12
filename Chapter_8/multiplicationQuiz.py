import pyinputplus as pyip
import random
import time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    num1, num2 = random.randint(1,9), random.randint(1,9) 
    2
    prompt = "#%s: %s x %s = " % (questionNumber + 1, num1, num2)

    try: 
        # Right answers are handled by allowRegexes
        # Wrong answers are handled by blockRegexes, with a cutom message
        response = pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],            
        blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
    except pyip.TimeoutException:
        print("Out of time!")
    except pyip.RetryLimitException:
        print("Out of tries!")
    else:
        # This block runs if no exceptions were raised in the try block
        print("Correct!")
        correctAnswers += 1

    time.sleep(1) # Brief pause to let user see the result.
print("Score: %s / %s" % (correctAnswers, numberOfQuestions))
