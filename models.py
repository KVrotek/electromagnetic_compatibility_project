import math 
import matplotlib.pyplot as plt

# R_value = 20
# C_value = 800
# L_value = 40

class selectModel():
    def __init__(self):
        self.RLCVariables()
        print("Wybierz model:\n1 - Model idealny\n2 - Model rzeczywisty")
        self.numberOfModel = input()
        self.checkIfModelExist()

    def checkIfModelExist(self):
        if int(self.numberOfModel) == 1:
            models.RLC_perfect_model()
        elif int(self.numberOfModel) == 2:
            print("Model 2!")
        else:
            print("Nie ma takiego modelu!")

    def RLCVariables(self):
        global R_value
        global L_value
        global C_value
        print("Podaj Rezystancje:")
        R_value = input()
        print("Podaj Indukcyjność:")
        L_value = input()
        print("Podaj Pojemność:")
        C_value = input()
        

class models():
    def RLC_perfect_model():
        frequency_table = []
        impedance_table = []
        for f in range(10,50000,10):
            Omega = 2*math.pi*f
            Resistance = float(R_value)
            Reactance_L = Omega*float(L_value)
            Reactance_C = -1/(Omega*float(C_value))
            Reactance = Reactance_C + Reactance_L
            Impedance = math.sqrt((Resistance**2)+(Reactance**2))
            frequency_table.append(f)
            impedance_table.append(Impedance)
        plt.plot(frequency_table,impedance_table)
        plt.xscale("log")
        plt.show()



        
       