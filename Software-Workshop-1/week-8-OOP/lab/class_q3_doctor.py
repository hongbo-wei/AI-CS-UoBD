""" 
File: doctor.py 
Project 5.10 (book project 9.5 - Week 8 Q3)
Conducts an interactive session of nondirective psychotherapy. 
Adds a history list of earlier patient sentences, 
which can be chosen for replies to shift the conversation to an earlier topic. 
""" 
'''
Restructure this program according to the
model/view pattern so that these areas of responsibility are
assigned to separate sets of classes. The program should include
a Doctor class with an interface that allows one to obtain a
greeting, a signoff message, and a reply to a patient's string. The
rest of the program, in a separate main program module, handles
the user's interactions with the Doctor object. You may develop
either a terminal-based user interface or a GUI.
'''
import random 
history = [] 
hedges = ("Please tell me more.", 
          "Many of my patients tell me the same thing.", 
          "Please coninue.")
 
qualifiers = ("Why do you say that ", 
              "You seem to think that ", 
              "Can you explain why ")
 
replacements = {"I":"you", "me":"you", "my":"your", 
                "we":"you", "us":"you", "mine":"yours", 
                "you":"I", "your":"my", "yours":"mine"}  
 
def reply(sentence): 
    """Implements three different reply strategies.""" 
    probability = random.randint(1, 5) 
    if probability in (1, 2): 
        # Just hedge 
        answer = random.choice(hedges) 
    elif probability == 3 and len(history) > 3: 
        # Go back to an earlier topic 
        answer = "Earlier you said that " + \
            changePerson(random.choice(history)) 
    else: 
        # Transform the current input 
        answer = random.choice(qualifiers) + changePerson(sentence)
    # Always add the current sentence to the history list 
    history.append(sentence) 
    return answer 
 
def changePerson(sentence): 
    """Replaces first person pronouns with second person pronouns.""" 
    words = sentence.split() 
    replyWords = [] 
    for word in words: 
        replyWords.append(replacements.get(word, word)) 
    return " ".join(replyWords)  
 
def main(): 
    """Handles the interaction between patient and doctor.""" 
    print("Good morning, I hope you are well today.") 
    print("What can I do for you?") 
    while True: 
        sentence = input("\n>> ") 
        if sentence.upper() == "QUIT": 
            print("Have a nice day!") 
            break 
        print(reply(sentence)) 
 
# The entry point for program execution 
if __name__ == "__main__": 
    main()