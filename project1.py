import random

def shuffleword(wrd):
    pw = random.sample(wrd,k=len(wrd))
    return ''.join(pw)

def printpuzzlequestion(word,score):
    problemword=shuffleword(word)
    print("\n arrange the letters to form valid word")
    print(problemword)
    userword=input()
    print()
    if userword.upper()==word:
        print("correct")
        score+=1
    else:
        print("wrong")
        score-=1
    return score

def main():
    score=0
    words = ["FATHER","BREAK","COUNTRY"]
    words = random.sample(words,k=len(words))

    for word in words:
        score=printpuzzlequestion(word,score)


    print("Your score is",score)

main()



