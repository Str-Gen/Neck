# todo make an interval dictionary with names and half steps
# then make questions out of them

class Intervals:    
    intervals = [
        (0,"perfect unison","P1"),
        (1,"minor second","m2"),
        (2,"major second","M2"),
        (3,"minor third","m3"),
        (4,"major third","M3"),
        (5,"perfect fourth","P4"),
        (6,"-","Tritone"),
        (7,"perfect fifth","P5"),
        (8,"minor sixth","m6"),
        (9,"major sixth","M6"),
        (10,"minor seventh","m7"),
        (11,"major seventh","M7"),
        (12,"perfect octave","P8")
    ]

    # standard tuning string differences
    standard_tune_intervals = [
        ("E-A",5),
        ("A-D",5),
        ("D-G",5),
        ("G-B",4),
        ("B-E",5)
    ]

    def interval_to_number(self,interval):
        for number,inter,short in self.intervals:
            if inter == interval or short == interval:
                return number

    def number_to_interval(self,number):
        return self.intervals[number][1]