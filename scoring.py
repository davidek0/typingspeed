import timeit

class Score:
    timeit.default_timer
    words_typed = 0

    @classmethod
    def score(cls, score):
        if score:
            cls.words_typed += 1