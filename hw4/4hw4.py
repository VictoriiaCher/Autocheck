"""Оцінка	Бали	Оцінка ECTS	Пояснення
    1	    0-34	F	Unsatisfactorily
    2	    35-59	FX	Unsatisfactorily
    3	    60-66	E	Enough
    3	    67-74	D	Satisfactorily
    4	    75-89	C	Good
    5	    90-95	В	Very good
    5	    96-100	A	Perfectly"""


def get_grade(key):
    return get.grade(key, None)


def get_description(key):
    return get.description(key, None)


grade = dict(F=1, FX=2, E=3, D=3, C=4, B=5, A=5)

description = dict(
    F="Unsatisfactorily",
    FX="Unsatisfactorily",
    E="Enough",
    D="Satisfactorily",
    C="Good",
    B="Very good",
    A="Perfectly",
)
