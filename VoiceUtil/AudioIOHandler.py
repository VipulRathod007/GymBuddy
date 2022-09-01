# ----------------------------------------------------------------------------------------------------------------------
#  Contains the definition of AudioIOHandler class
#  Copyright (c) 2022. By Vipul Rathod
#  All rights reserved
# ----------------------------------------------------------------------------------------------------------------------

import pyttsx3
import speech_recognition


class AudioIOHandler:
    """Represents AudioIOHandler class"""

    __sShared__ = None

    def __init__(self):
        if AudioIOHandler.__sShared__ is None:
            self.__mEngine = pyttsx3.init()
            voices = self.__mEngine.getProperty('voices')
            self.__mEngine.setProperty('voice', voices[1].id)

            self.__mRecognizer = speech_recognition.Recognizer()
            self.__mRecognizer.pause_threshold = 0.5
            AudioIOHandler.__sShared__ = self
        else:
            raise Exception('Attempt to create Multiple instance of Singleton class')

    @staticmethod
    def getInstance():
        return AudioIOHandler() if AudioIOHandler.__sShared__ is None else AudioIOHandler.__sShared__

    def speak(self, inMessage: str):
        self.__mEngine.say(inMessage)
        self.__mEngine.runAndWait()

    def listen(self) -> str:
        # TODO: Fix listening
        with speech_recognition.Microphone() as source:
            self.__mRecognizer.adjust_for_ambient_noise(source)
            query = ''
            while len(query) == 0:
                print('Listening....')
                audio = self.__mRecognizer.listen(source)
                print(audio.get_raw_data().decode())
                try:
                    query = self.__mRecognizer.recognize_google(audio, language='en-in')
                    print(f'Query: {query}')
                    return query
                except Exception as e:
                    print(f'Error: "{e}"')
                    print('Error occurred.\nPlease say it again')
