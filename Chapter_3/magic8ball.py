import random

predictions = [
    "It is certain",
    "It is decidedly so",
    "Yes",
    "Reply hazy, try again",
    "Ask again later",
    "Concentrate and ask again",
    "My reply is no",
    "Outlook not so good",
    "Very doubtful",
]


def getAnswer(AnswerNumber):

    return predictions[AnswerNumber]


print("\n", getAnswer(random.randint(0, len(predictions) - 1)), "\n")
