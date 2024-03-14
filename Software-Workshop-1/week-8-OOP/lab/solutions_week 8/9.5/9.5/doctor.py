"""
File: doctor.py
Project 5

Softbot for a non-directive psychotherapist.
"""

import random

class Doctor():

    # All doctors share the same qualifiers, replacements, and hedges.

    QUALIFIERS = ['Why do you say that ', 'You seem to think that ',
                  'Did I just hear you say that ',
                  'Why do you believe that ']

    REPLACEMENTS = {'i': 'you', 'me': 'you', 'my': 'your',
                    'we': 'you', 'us': 'you', 'am': 'are',
                    'you': 'i', 'you': 'I'}

    HEDGES = ['Go on.', 'I would like to hear more about that.',
              'And what do you think about this?', 'Please continue.']

    # Each doctor keeps its own individual history.

    def __init__(self):
        """Loads history from a file, if it exists."""
        self.history = []

    def greeting(self):
        """Returns the doctor's greeting"""
        return "Hello, how can I help you today?"

    def farewell(self):
        """Returns the doctor's farewell"""
        return "Have a nice day!"

    def reply(self, sentence):
        """Returns the doctor's reply to sentence."""
        choice = random.randint (1, 10)
        if choice in (1, 2):
            if len(self.history) > 3:
                answer = 'Earlier you said that ' + \
                self.change_person(random.choice(self.history))
            else:
                answer = random.choice(Doctor.HEDGES)
        elif choice in range(3, 7):
            answer = random.choice(Doctor.QUALIFIERS) + \
            self.change_person(sentence) + "?"
        else:
            answer = random.choice(Doctor.HEDGES)
        self.history.append(sentence)
        return answer
        
    def change_person(self, sentence):
        """Replaces pronouns so as to shift the address."""
        oldlist = sentence.split()
        newlist = []
        for word in oldlist:
            newlist.append(Doctor.REPLACEMENTS.get(word.lower(),
                                                   word))
        return " ".join(newlist)

def main():
    """Tester function for Doctor class.
    The patient enters 'quit' to exit."""
    doctor = Doctor()
    print(doctor.greeting())
    while True:
        sentence = input("> ")
        if sentence.upper() == "QUIT":
            print(doctor.farewell())
            break
        else:            
            print(doctor.reply(sentence))

if __name__ == "__main__":
    main()

    
        
    



    
    
    

