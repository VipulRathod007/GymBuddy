# ----------------------------------------------------------------------------------------------------------------------
#  Contains the definition of Workout class
#  Copyright (c) 2022. By Vipul Rathod
#  All rights reserved
# ----------------------------------------------------------------------------------------------------------------------

import time

from .Exercise import Exercise


class Workout:
    """Represents Workout class"""

    def __init__(self, inExercises: list[Exercise]):
        self.__mExercises = inExercises
        lastEndTime = time.time()
        for exercise in self.__mExercises:
            if exercise.StartTime != 0:
                if exercise.StartTime < lastEndTime:
                    print(f'Error: {exercise.Name} starts even before the completion of previous exercise')
                    quit(1)
                else:
                    lastEndTime = exercise.CompletionTime
            else:
                exercise.StartTime = lastEndTime

    def start(self):
        for exercise in self.__mExercises:
            if time.time() < exercise.StartTime:
                time.sleep(exercise.StartTime - time.time())
            exercise.doExercise()
