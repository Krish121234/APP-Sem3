#python code for factory method 
#it comes under the creational design pattern

class FrenchLocalizer:
    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette", "cycle": "cyclette"}

    def localizer(self, msg):
        return self.translations.get(msg, msg)

class SpanishLocalizer:
    def __init__(self):
        self.translations = {"car":"coche", "bike": "bicicleta", "cycle":"ciclo"}

    def localizer(self, msg):
        return self.translations.get(msg,msg)

class EnglishLocalizer:
    def localizer(self, msg):
        return msg


def Factory(language = "English"):
    localizers={
        "French":FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer
    }
    return localizers[language]()

if __name__ == "__main__":
    f = Factory("French")
    e = Factory("English")
    s = Factory("Spanish")

    message = ["car", "bike", "cycle"]
    for msg in message:
        print(f.localizer(msg))
        print(e.localizer(msg))
        print(s.localizer(msg))