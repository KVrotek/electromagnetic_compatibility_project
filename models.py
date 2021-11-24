import variables
import math 
import matplotlib.pyplot as plt

R_value = 20
C_value = 800
L_value = 40

class models():
    def RLC_perfect_model():
        frequency_table = []
        impedance_table = []
        for f in range(10,50000,10):
            Omega = 2*math.pi*f
            Resistance = R_value
            Reactance_L = Omega*L_value
            Reactance_C = -1/(Omega*C_value)
            Reactance = Reactance_C + Reactance_L
            Impedance = math.sqrt((Resistance**2)+(Reactance**2))
            frequency_table.append(f)
            impedance_table.append(Impedance)
        plt.plot(frequency_table,impedance_table)
        plt.xscale("log")
        plt.show()



        
       