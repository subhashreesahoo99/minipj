print("Welcome to my computer quiz!")
playing = input("Do you want to play?")
if playing.lower() != "yes":
    quit()
print("okay! Let's play:)")
score = 0
answer = input("what does HTML stands for?")
if answer.lower() == "hyper text markup language" :
    print('correct!')
    score = score +1
else:
    print("incorrect!") 

answer = input("Who is making the Web standards?")
if answer.lower() == "world wide web consortium" :
    print('correct!')
    score = score + 1
else:
    print("incorrect!")

answer = input("<br/> what type of tag is this?")
if answer.lower() == "break tag" :
    print('correct!')
    score = score+1
else:
    print("incorrect!")

answer = input("What is the correct HTML element for inserting a line break?")
if answer.lower() == "<br>" :
    print('correct!')
    score = score+1
else:
    print("incorrect!")
           
print("You got" +  str(score)  + "questions correct!")
print("You got" +  str((score / 4) * 100)  + "%")
