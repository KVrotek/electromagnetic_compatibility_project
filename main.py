import models
import variables

class Main():
    def __init__(self):
        print("Wybierz model:\n1 - Model idealny\n2 - Model rzeczywisty")
        self.numberOfModel = input()
        self.select_model()

    def select_model(self):
        if int(self.numberOfModel) == 1:
            models.models.RLC_perfect_model()
        else:
            print("Brak modelu")
Main()