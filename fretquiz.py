import random
import fretboard as f
from termcolor import colored

class FretQuiz:
    def __init__(self, fretboard=f.Fretboard()):
        self.quiz = []
        self.fretboard = fretboard
        self.prepare_qa(fretboard.sharp_fretboard)

    def prepare_qa(self, fretboard, nr=10):        
        for _ in range(nr):
            stringnr = random.randint(0, 4)
            fretnr = random.randint(0, 24)
            self.quiz.append((stringnr, fretnr, fretboard[stringnr][fretnr]))

    def run_quiz(self):
        print(colored("The quiz starts", "white", attrs=["bold"]))        
        for _ in self.quiz:
            stringnr, fretnr, note = _            
            print(colored("Which fret is "+note +
                          " on string "+self.fretboard.tuning[stringnr]+"?", "blue"))
            answer = input("Your answer: ")
            if int(answer) in (fretnr-12, fretnr, fretnr+12):
                print(colored("+", "green"))
            else:
                if fretnr <= 12:
                    print(colored("- => "+str(fretnr)+" and "+str(fretnr+12), "red"))
                else:
                    print(colored("- => "+str(fretnr)+" and "+str(fretnr-12), "red"))
