import argparse


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-Q", "--questions", action="store",
                        dest="Q", help="Number of questions", type=int, default=10)
    parser.add_argument("-T", "--time", action="store", dest="T",
                        help="Time the responses, then restrict the answer time", type=bool, default=False)
    parser.add_argument("-R", "--reverse", action="store", dest="R",
                        help="Instead of notes -> numbers, numbers -> notes", type=bool, default=False)
    parser.add_argument("-F", "--findall", action="store", dest="F",
                        help="Find all instances along the neck", type=bool, default=False)
    parser.add_argument("-C", "--chords", action="store", nargs="+", choices=["Maj", "Min", "Maj7", "Min7", "7", "Dim", "Aug"],
                        dest="C", help="Train chords")
    parser.add_argument("-S", "--scales", action="store", nargs="+", choices=["major", "ionian", "dorian", "phrygian", "lydian", "mixolydian", "minor", "aeolian", "locrian"],
                        dest="S", help="Train scales")
    # todo add sub args for scales Maj Min and the modes, heptatonic, pentatonic, chromatic, dominant, natural
    return parser
