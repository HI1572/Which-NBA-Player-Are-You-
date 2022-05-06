"""
Lucio
May 6, 2022
This code is a quiz that will let you know which NBA player you are.
"""

#functions
def points(): #Create points funtion that will determine your score after each question is answered, to then see your final player
    global score #Brings score into function
    answer = input("ANSWER: ").upper() #Answer is going to equal your input
    if answer == "A": #If answer equals A
        score = score + 10 #Then add 10 to score
    elif answer == "B": #If answer equals B
        score = score + 20 #Then add 20 to score
    elif answer == "C": #If answer equals C
        score = score + 30 #Then add 30 to score
    elif answer == "D": #If answer equals D
        score = score + 40 #Then add 40 to score

def player(): #Create player function that uses your score to see your final player
    if score == 70 or score == 80: #If score is in between 70 and 80
        print("YOU ARE GORAN DRAGIC") #Then you are Goran Dragic
    elif score == 90 or score == 100 or score == 110: #If score is in between 90 and 110
        print("YOU ARE RUSSELL WESTBROOK") #Then you are Russell Westbrook
    elif score == 120 or score == 130 or score == 140: #If score is in between 120 and 140
        print("YOU ARE STEPHEN CURRY") #Then you are Stephen Curry
    elif score == 150 or score == 160 or score == 170: #If score is in between 150 and 170
        print("YOU ARE KEVIN DURANT") #Then you are Kevin Durant
    elif score == 180 or score == 190 or score == 200 or score == 210: #If score is in between 180 and 210
        print("YOU ARE LEBRON JAMES") #Then you are Lebron James
    elif score == 220 or score == 230 or score == 240: #If score is in between 220 and 240
        print("YOU ARE BLAKE GRIFFIN") #Then you are Blake Griffin
    elif score == 250 or score == 260: #If score is in between 250 and 260
        print("YOU ARE ANTHONY DAVIS") #Then you are Anthony Davis
    elif score == 270 or score == 280: #If score is in between 270 and 280
        print("YOU ARE DEANDRE JORDAN") #Then you are Deandre Jordan

#game sequence
print("""WELCOME TO THIS NBA QUIZ
WHICH PLAYER ARE YOU?
YOU WILL GET 7 QUESTIONS TO SEE WHO YOU ARE
LET'S GET INTO IT!
""")
#Welcome message

start = input("TYPE 'START' WHEN YOU ARE READY: ").upper() #Input to be start when ready

if start == "START": #When they input start start the quiz
    
    score = 0 #Starting score is 0
    
    print("""
1. PICK THE STATS YOU PREFER!
   a. 6 pts/10 assists/4 steals
   b. 34 pts/3 assists/2 rebounds
   c. 20 pts/7 assists/7 rebounds
   d. 14 pts/6 assists/13 rebounds""")
#Question 1 
    
    points() #Calls points function

    print("""
2. WHAT NBA PLAYER RELATES TO YOU?
   a. Chris Paul
   b. Stephen Curry
   c. Lebron James
   d. Anthony Davis""")
#Question 2

    points() #Calls points function

    print("""
3. WHO IS THE BEST PLAYER OF ALL TIME?
   a. Magic Johnson
   b. Kobe Bryant
   c. Michael Jordan
   d. Shaquille O'Neal""")
#Question 3

    points() #Calls points function

    print("""
4. WHAT IS YOUR BIGGEST STRENGTH?
   a. I'm fast
   b. I'm smart
   c. I'm brave
   d. I'm strong""")
#Question 4

    points() #Calls points function

    print("""
5. WHAT'S YOUR STYLE OF PLAY?
   a. Passing and Dribbling
   b. Shooting and Driving
   c. Dunking and Rebounding
   d. Rebounding and Blocking""")
#Question 5

    points() #Calls points function

    print("""
6. HOW TALL ARE YOU?
   a. 5'9 and Down
   b. 5'9 to 6'2
   c. 6'2 to 6'7
   d. 6'7 and Up""")
#Question 6

    points() #Calls points function

    print("""
7. 3 SECONDS LEFT, YOU'RE DOWN BY ONE. WHAT DO YOU DO?
   a. Draw a foul or Pass it out
   b. Go for a shot
   c. Go for a layup
   d. Go to the glass for the rebound""")
#Question 7
    
    points() #Calls points function
    
    player() #Calls player function