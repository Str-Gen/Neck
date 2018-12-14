#!/usr/bin/env -S python -u
import pprint
from termcolor import colored
from fretboard import Fretboard
from fretquiz import FretQuiz
from misc import build_parser
pp = pprint.PrettyPrinter(indent=4)

parser = build_parser()
parsed_opts = parser.parse_args()

# add half tone schemas for scales / modes

# standard tuning implied
fretboard = Fretboard()
fretboard_sharps = fretboard.sharp_fretboard

print(colored("The fretboard", "white", attrs=["bold"]))
print(list(range(0,25)))
for x in fretboard_sharps:
    print(x)

q = FretQuiz(fretboard=fretboard)
q.run_quiz()