score=input("Enter the score to know your grade ")
try:
    score = float(score)
except:
    print("Do not complicate things just enter your score a numerics")
    quit()
if (score < 0)|(score > 1) :
    print("You Fool, if you dont you know how your grading works, you've probably flunked")
    print("Enter a score between 0 & 1")
    quit()
print("Your Grade for score ",score,"is ")
if score >= 0.9 :
    print("A")
elif score >= 0.8 :
    print("B")
elif score >= 0.7 :
    print("C")
elif score >= 0.6 :
    print("D")
else :
    print("F")
