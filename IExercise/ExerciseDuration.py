# ----------------------------------------------------------------------------------------------------------------------
#  Contains the definition of ExerciseDuration class
#  Copyright (c) 2022. By Vipul Rathod
#  All rights reserved
# ----------------------------------------------------------------------------------------------------------------------


class ExerciseDuration:
    """Represents ExerciseDuration class"""

    def __init__(self, inSetRestSec: float, inSetDurationSec: float):
        """
        TODO: Determine whether Rest time needed?
        The constructor
        :param inSetRestSec: Rest time in between Set in Seconds
        :param inSetDurationSec: Time duration for a repetition in seconds
        """
        self.__mSetRestSec = inSetRestSec
        self.__mSetDurationSec = inSetDurationSec

    @property
    def DurationOfSetSec(self) -> float:
        """Returns the duration in seconds for a set of exercise"""
        return self.__mSetDurationSec

    @property
    def RestDurationSec(self):
        """Returns the rest duration in between Sets"""
        return self.__mSetRestSec

    def __sub__(self, inOther):
        """Overloaded Minus operator"""
        return ExerciseDuration(self.__mSetRestSec - inOther.__mSetRestSec,
                                self.__mSetDurationSec - inOther.__mSetDurationSec)

    def __add__(self, inOther):
        """Overloaded Minus operator"""
        return ExerciseDuration(self.__mSetRestSec + inOther.__mSetRestSec,
                                self.__mSetDurationSec + inOther.__mSetDurationSec)

    def __divmod__(self, inOther):
        """Overloaded Division operator"""
        return ExerciseDuration(self.__mSetRestSec / inOther.__mSetRestSec,
                                self.__mSetDurationSec / inOther.__mSetDurationSec)

    def __mul__(self, inOther: float):
        """Overloaded Division operator"""
        return ExerciseDuration(self.__mSetRestSec * inOther, self.__mSetDurationSec * inOther)

    def compare(self, inOther):
        """Compares the performance"""
        return self.__sub__(inOther).__divmod__(inOther) * 100

    @classmethod
    def sum(cls, *args):
        total = ExerciseDuration(0, 0)
        for _ in args:
            total += _
        return total

    @classmethod
    def avg(cls, *args):
        total = ExerciseDuration(0, 0)
        for _ in args:
            total += _
        return total * (1 / len(args))
