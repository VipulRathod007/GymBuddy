# ----------------------------------------------------------------------------------------------------------------------
#  Contains the definition of Exercise class
#  Copyright (c) 2022. By Vipul Rathod
#  All rights reserved
# ----------------------------------------------------------------------------------------------------------------------

import time

from VoiceUtil import AudioIOHandler
from .ExerciseDuration import ExerciseDuration


class Exercise:
    """Represents Exercise class"""

    def __init__(self, inName: str, inSets: int, inReps: int,
                 inExerciseDuration: ExerciseDuration,
                 inPostExerciseRestTime: time,
                 inStartTime: time = 0):
        self.__mName = inName
        self.__mSets = inSets
        self.__mReps = inReps
        self.__mExerciseDuration = inExerciseDuration
        self.__mStartTime = inStartTime
        self.__mPostExerciseRestTime = inPostExerciseRestTime
        self.__mSetDurationSec = self.__mExerciseDuration.DurationOfSetSec
        self.__mRestDurationSec = self.__mExerciseDuration.RestDurationSec
        self.__mRepDurationSec = self.__mExerciseDuration.DurationOfSetSec // self.__mReps

    @property
    def Name(self) -> str:
        """Name of the exercise"""
        return self.__mName

    @property
    def Sets(self) -> int:
        """Number of sets of the exercise"""
        return self.__mSets

    @property
    def Repetitions(self) -> int:
        """Number of repetitions in a set of the exercise"""
        return self.__mReps

    @property
    def StartTime(self):
        """The time when exercise should start"""
        return self.__mStartTime

    @StartTime.setter
    def StartTime(self, inTime: time):
        """The time when exercise should start"""
        self.__mStartTime = inTime

    @property
    def CompletionTime(self) -> time:
        """The time when exercise get completed"""
        return self.__mStartTime + self.__mSets * ((self.__mReps * self.__mRepDurationSec) + self.__mRestDurationSec) +\
               self.__mPostExerciseRestTime

    def doExercise(self):
        # TODO: Multi-thread support to make interactive
        AudioIOHandler.getInstance().speak(f'Get ready for {self.__mName}')
        lastPerf = self.__mExerciseDuration
        perfData = list()
        for setNum in range(1, self.__mSets + 1):
            if setNum == 1:
                AudioIOHandler.getInstance().speak(f'You have {int(self.__mSetDurationSec)} seconds '
                                                   f'to beat {self.__mReps} reps'
                                                   f'Kill it!')
            repStartTime = time.time()
            for repNum in range(1, self.__mReps + 1):
                AudioIOHandler.getInstance().speak(str(repNum))
                time.sleep(self.__mRepDurationSec)
            setDuration = time.time() - repStartTime
            currPerf = ExerciseDuration(lastPerf.RestDurationSec, setDuration)
            perfData.append(currPerf)
            # Set-wise Analysis
            # perf = currPerf.compare(lastPerf)
            # if perf.DurationSec < 0:
            #     AudioIOHandler.getInstance().speak(f'Well done! {int(perf.DurationSec)} percent faster this time.')
            # else:
            #     AudioIOHandler.getInstance().speak(f'Naah, {int(perf.DurationSec)} percent slower you are.')
            time.sleep(self.__mRestDurationSec)
        AudioIOHandler.getInstance().speak(f'{self.__mSets * self.__mReps} Reps done of {self.__mName}.')
        # Final Analysis
        # perf = ExerciseDuration.avg(*perfData).compare(inExercisePerf)
        # if perf.DurationSec < 0:
        #     AudioIOHandler.getInstance().speak(f'Woah! {int(perf.DurationSec)} percent faster.'
        #                                        f'Keep going strong.')
        # else:
        #     AudioIOHandler.getInstance().speak(f'Naah, {int(perf.DurationSec)} percent slower you are.')
