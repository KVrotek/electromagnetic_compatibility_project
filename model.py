import math
import matplotlib.pyplot as plt

class selectElement():
    def __init__(self):
        print("Wybierz Element RLC:\n1 - Rezystor\n2 - Cewka\n3 - Kondensator")
        self.selectElementRLC = input()
        print("Wybierz model:\n1 - Model idealny\n2 - Model rzeczywisty")
        self.selectModel = input()
        self.checkIfElementExist()

    def checkIfElementExist(self):
        if int(self.selectElementRLC) == 1:
            if int(self.selectModel) == 1:
                Models.idealResistor()
                #print("Rezystor idealny")
            elif int(self.selectModel) == 2:
                print("Rezystor rzeczywisty")
            else:
                print("Nie ma takiego modelu")
        elif int(self.selectElementRLC) == 2:
            if int(self.selectModel) == 1:
                Models.idealCoil()
                #print("Cewka idealna")
            elif int(self.selectModel) == 2:
                print("Cewka rzeczywista")
            else:
                print("Nie ma takiego modelu")
        elif int(self.selectElementRLC) == 3:
            if int(self.selectModel) == 1:
                Models.idealCapacitor()
                #print("Kondensator idealny")
            elif int(self.selectModel) == 2:
                print("Kondensator rzeczywisty")
            else:
                print("Nie ma takiego modelu")
        else:
            print("Nie ma takiego elementu!")

class Models():
    def idealResistor():
        resistance = input("R[Ω] - ")
        reactance = 0
        #print(resistance)
        for f in range(10,50000,10):
            impedance = math.sqrt((float(resistance)**2)+(float(reactance)**2))
            resultTables.impedanceTable.append(impedance)
            resultTables.frequencyTable.append(f)
        #print(resultTables.impedanceTable)
        #print(resultTables.frequencyTable)
        drawChart()
    def idealCapacitor():
        capacity = input("C[pF] - ")
        resistance = 0
        for f in range(10,50000,10):
            omega = 2*math.pi*f
            reactance = -1/(omega*float(capacity)*(10**-12))
            impedance = math.sqrt((float(resistance)**2)+(float(reactance)**2))
            resultTables.impedanceTable.append(impedance)
            resultTables.frequencyTable.append(f)
        drawChart()
    def idealCoil():
        inductance = input("L[µH] - ")
        resistance = 0
        for f in range(10,50000,10):
            omega = 2*math.pi*f
            reactance = omega*float(inductance)*(10**-6)
            impedance = math.sqrt((float(resistance)**2)+(float(reactance)**2))
            resultTables.impedanceTable.append(impedance)
            resultTables.frequencyTable.append(f)
        drawChart()


class resultTables():
    impedanceTable = []
    frequencyTable = []

class drawChart():
    def __init__(self):
        plt.plot(resultTables.frequencyTable,resultTables.impedanceTable)
        plt.xscale("log")
        plt.grid(visible=True,axis='both', which='both')
        plt.ylabel('Impedancja [Ω]')
        plt.xlabel('Częstotliwość [Hz]')
        plt.show()
