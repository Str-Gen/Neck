class Fretboard:
    # 12 tone
    __complete = ["A", "A# / Bb", "B / Cb", "B# / C", "C# / Db",
                     "D", "D# / Eb", "E / Fb", "E# / F", "F# / Gb", "G", "G# / Ab"]
    __simplified_sharps = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    __simplified_flats = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
    full_fretboard = None
    sharp_fretboard = None
    flat_fretboard = None
    tuning = None

    def __init__(self, tuning=["E", "A", "D", "G", "B", "E"]):
        self.tuning = tuning
        self.full_fretboard = self._build_sharp_flat_fretboard()
        self.sharp_fretboard = self._build_fretboard(self.__simplified_sharps)
        self.flat_fretboard = self._build_fretboard(self.__simplified_flats)        

    def _build_sharp_flat_fretboard(self):
        fretboard_complete = list()
        for tone in ("E / Fb", "A", "D", "G", "B / Cb", "E / Fb"):
            idx = self.__complete.index(tone)
            seq = [self.__complete[i % len(self.__complete)]
                   for i in range(idx, idx+13)]
            fretboard_complete.append(seq)
        return self._extend_to_24(fretboard_complete)

    def _build_fretboard(self, frets):
        fretboard_sharps = list()
        for tone in self.tuning:
            idx = frets.index(tone)
            seq = [frets[i % len(frets)]
                   for i in range(idx, idx+13)]
            fretboard_sharps.append(seq)
        return self._extend_to_24(fretboard_sharps)

    def _extend_to_24(self, fretboard):
        for x in fretboard:
            x.extend(x[1:])
        return fretboard
