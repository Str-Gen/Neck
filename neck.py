#!/usr/bin/env -S python -u
import pprint
import argparse
import random
from termcolor import colored
pp = pprint.PrettyPrinter(indent=4)

parser = argparse.ArgumentParser()
parser.add_argument("-Q", "--questions", action="store",
                    dest="Q", help="Number of questions", type=int, default=10)
parser.add_argument("-T", "--time", action="store", dest="T",
                    help="Time the responses, then restrict the answer time", type=bool, default=False)
parser.add_argument("-R", "--reverse", action="store", dest="R",
                    help="Instead of notes -> numbers, numbers -> notes", type=bool, default=False)
parser.add_argument("-F", "--findall", action="store", dest="F",
                    help="Find all instances along the neck", type=bool, default=False)
parser.add_argument("-C", "--chords", action="store",
                    dest="C", help="Train chords")
# todo add sub args for chords Maj, Min, 7, Maj7, Min7, Dim, Aug, ...
parser.add_argument("-S", "--scales", action="store",
                    dest="S", help="Train scales")
# todo add sub args for scales Maj Min and the modes, heptatonic, pentatonic, chromatic, dominant, natural
parsed_opts = parser.parse_args()

# 12 tone
complete = ["A", "A# / Bb", "B / Cb", "B# / C", "C# / Db", "D",
            "D# / Eb", "E / Fb", "E# / F", "F# / Gb", "G", "G# / Ab"]
simplified_sharps = ["A", "A#", "B", "C",
                     "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
simplified_flats = ["A", "Bb", "B", "C", "Db",
                    "D", "Eb", "E", "F", "Gb", "G", "Ab"]

# add half tone schemas for scales / modes

# standard tuning implied

fretboard_complete = []
for tone in ("E / Fb", "A", "D", "G", "B / Cb", "E / Fb"):
    idx = complete.index(tone)
    seq = [complete[i % len(complete)] for i in range(idx, idx+13)]
    fretboard_complete.append(seq)
# pp.pprint(fretboard_complete)

fretboard_sharps = []
for tone in ("E", "A", "D", "G", "B", "E"):
    idx = simplified_sharps.index(tone)
    seq = [simplified_sharps[i % len(simplified_sharps)]
           for i in range(idx, idx+13)]
    fretboard_sharps.append(seq)
# pp.pprint(fretboard_sharps)

fretboard_flats = []
for tone in ("E", "A", "D", "G", "B", "E"):
    idx = simplified_flats.index(tone)
    seq = [simplified_flats[i % len(simplified_flats)]
           for i in range(idx, idx+13)]
    fretboard_flats.append(seq)
# pp.pprint(fretboard_flats)


def extend_to_24(fretboard):
    for x in fretboard:
        x.extend(x[1:])
    return fretboard


extend_to_24(fretboard_complete)
extend_to_24(fretboard_sharps)
extend_to_24(fretboard_flats)

print(colored("The fretboard", "white", "bold"))
for x in fretboard_sharps:
    print(x)


def prepare_questions(nr=parsed_opts.Q+1, fretboard=fretboard_sharps, findall=parsed_opts.F):
    questions = []
    for _ in range(nr):
        stringnr = random.randint(0, 4)
        fretnr = random.randint(0, 24)
        questions.append((stringnr, fretnr, fretboard[stringnr][fretnr]))
    return questions


print(colored("The quiz starts", "white", "bold"))
tuning = ['E', 'A', 'D', 'G', 'B', 'E']
for x in prepare_questions():
    stringnr, fretnr, note = x
    if not parsed_opts.R:
        print(colored("Which fret is "+note +
                      " on string "+tuning[stringnr]+"?", "blue"))
        answer = input("Your answer: ")
        if int(answer) in (fretnr-12, fretnr, fretnr+12):
            print(colored("+", "green"))
        else:
            if fretnr < 12:
                print(colored("- => "+fretnr+" and "+fretnr+12, "red"))
            else:
                print(colored("- => "+fretnr+" and "+fretnr-12, "red"))
