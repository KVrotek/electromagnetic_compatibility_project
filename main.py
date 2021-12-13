import math
from tkinter.constants import W
import tkinter as tk
from PIL import ImageTk,Image
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# class main():
#     models.selectModel()
#     model.selectElement()
#     pass

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.frequencyTable = []
        self.impedanceTable = []
        self.impedanceAngleTable = []
        self.realPartTable = []
        self.imaginaryPartTable = []
        self.f_rez = 0

        self.title('RLC in high frequency')
        self.iconphoto(False, tk.PhotoImage(file='icon.png'))

        self.expandListFrame = tk.Frame(self)
        self.expandListFrame.grid(column=0,row=0)
        self.options = ['Rezystor idealny','Rezystor rzeczywisty 1','Rezystor rzeczywisty 2','Rezystor rzeczywisty 3','Cewka idealna','Cewka rzeczywista','Kondensator idealny',"Kondensator rzeczywisty"]
        self.clicked = tk.StringVar()
        self.clicked.set(self.options[0])
        self.choice = 'Rezystor idealny'
        self.expandList = tk.OptionMenu(self.expandListFrame, self.clicked, *self.options, command=self.displaySelected)
        self.expandList.config(width=25, indicatoron=0)
        self.expandList.pack()
        
        self.BtnFrame = tk.Frame(self)
        self.BtnFrame.grid(column=2,row=0)
        self.calculateBtn = tk.Button(self.BtnFrame, text='Oblicz',width=10, command=self.calculate)
        self.calculateBtn.pack()
        
        self.imageFrame = tk.Frame(self)
        self.imageFrame.grid(column=0,row=1)
        self.schemeLabel = tk.Label(self.imageFrame)
        self.schemeLabel.pack()

        self.checkBoxFrame = tk.Frame(self)
        self.checkBoxFrame.grid(column=2, row=1)

        self.inputFrame = tk.Frame(self)
        # self.inputFrame.grid(column=1, row=1)

        self.chartFrame = tk.Frame(self)
        self.chartFrame.grid(column=0, row=2, columnspan=3)

        self.checkBoxes()
        self.functionDisplaySchemes()
        self.idealRModel()
        self.drawChart()
        

    def calculate(self):
        self.canvas.get_tk_widget().pack_forget()
        self.frequencyTable = [] 
        self.impedanceTable = []
        self.impedanceAngleTable = []
        self.realPartTable = []
        self.imaginaryPartTable = []
        self.f_rez = 0
        Fmin_value = int(self.Fmin.get())
        Fmax_value = int(self.Fmax.get())
        Fstep_value = 10
        if Fmax_value > 10000:
            Fstep_value = 100
        elif Fmax_value > 100000:
            Fstep_value = 1000
        elif Fmax_value > 1000000:
            Fstep_value = 10000
        elif Fmax_value > 10000000:
            Fstep_value = 100000
        elif Fmax_value > 100000000:
            Fstep_value = 1000000
        elif Fmax_value > 1000000000:
            Fstep_value = 10000000
        if self.choice == 'Rezystor idealny':
            self.f_rez = 0
            for f in range(Fmin_value,Fmax_value,Fstep_value):
                resistance = float(self.RInput.get())
                reactance = 0
                impedance = np.complex(resistance,reactance)
                impedanceModule = np.absolute(impedance)
                impedanceAngle = np.angle(impedance,deg=True)
                impedanceRealPart = np.real(impedance)
                impedanceImaginaryPart = np.imag(impedance)

                self.imaginaryPartTable.append(impedanceImaginaryPart)
                self.realPartTable.append(impedanceRealPart)
                self.impedanceAngleTable.append(impedanceAngle)
                self.impedanceTable.append(impedanceModule)
                self.frequencyTable.append(f) 
        elif self.choice == 'Cewka idealna':
            self.f_rez = 0
            for f in range(Fmin_value,Fmax_value,Fstep_value):
                omega = 2*math.pi*f*1000
                reactance = omega*int(self.LInput.get())*(10**-6)
                resistance = 0
                impedance = np.complex(resistance,reactance)
                impedanceModule = np.absolute(impedance)
                impedanceAngle = np.angle(impedance,deg=True)
                impedanceRealPart = np.real(impedance)
                impedanceImaginaryPart = np.imag(impedance)

                self.imaginaryPartTable.append(impedanceImaginaryPart)
                self.realPartTable.append(impedanceRealPart)
                self.impedanceAngleTable.append(impedanceAngle)
                self.impedanceTable.append(impedanceModule)
                self.frequencyTable.append(f)
        elif self.choice == 'Kondensator idealny':
            self.f_rez = 0
            for f in range(Fmin_value,Fmax_value,Fstep_value):
                omega = 2*math.pi*f*1000
                resistance = 0
                reactance = -1/(omega*int(self.CInput.get())*(10**-12))
                impedance = np.complex(resistance,reactance)
                impedanceModule = np.absolute(impedance)
                impedanceAngle = np.angle(impedance,deg=True)
                impedanceRealPart = np.real(impedance)
                impedanceImaginaryPart = np.imag(impedance)

                self.imaginaryPartTable.append(impedanceImaginaryPart)
                self.realPartTable.append(impedanceRealPart)
                self.impedanceAngleTable.append(impedanceAngle)
                self.impedanceTable.append(impedanceModule)
                self.frequencyTable.append(f)
        elif self.choice == 'Rezystor rzeczywisty 1':
            Cr_value = float(self.CrInput.get())*(10**-12)
            R_value = float(self.RInput.get())
            self.f_rez = 0
            for f in range(Fmin_value,Fmax_value,Fstep_value):
                omega = 2*math.pi*f*1000
                resistance = R_value/((R_value**2)*(omega**2)*(Cr_value**2)+1)
                reactance = -((R_value**2)*omega*Cr_value)/((R_value**2)*(omega**2)*(Cr_value**2)+1)
                impedance = np.complex(resistance,reactance)
              
                impedanceModule = np.absolute(impedance)
                impedanceAngle = np.angle(impedance,deg=True)
                impedanceRealPart = np.real(impedance)
                impedanceImaginaryPart = np.imag(impedance)

                self.imaginaryPartTable.append(impedanceImaginaryPart)
                self.realPartTable.append(impedanceRealPart)
                self.impedanceAngleTable.append(impedanceAngle)
                self.impedanceTable.append(impedanceModule)
                self.frequencyTable.append(f)
        elif self.choice == 'Rezystor rzeczywisty 2':
            Cr_value = float(self.CrInput.get())*(10**-12)
            R_value = float(self.RInput.get())
            Lr_value = float(self.LrInput.get())*(10**-6)
            self.f_rez = (((-R_value*Cr_value)+(math.sqrt(((R_value**2)*(Cr_value**2))+(4*Lr_value*Cr_value))))/(4*math.pi*Lr_value*Cr_value))/1000
            for f in range(Fmin_value,Fmax_value,Fstep_value):
                omega = 2*math.pi*f*1000
                resistance = R_value/(((omega**2)*(R_value**2)*(Cr_value**2))+((omega**4)*(Lr_value**2)*(Cr_value**2))-(2*(omega**2)*Lr_value*Cr_value)+1)
                reactance = (-((omega**3)*(Lr_value**2)*Cr_value)+(omega*Lr_value)-(omega*(R_value**2)*Cr_value))/(((omega**2)*(R_value**2)*(Cr_value**2))+((omega**4)*(Lr_value**2)*(Cr_value**2))-(2*(omega**2)*Lr_value*Cr_value)+1)
                impedance = np.complex(resistance,reactance)
              
                impedanceModule = np.absolute(impedance)
                impedanceAngle = np.angle(impedance,deg=True)
                impedanceRealPart = np.real(impedance)
                impedanceImaginaryPart = np.imag(impedance)

                self.imaginaryPartTable.append(impedanceImaginaryPart)
                self.realPartTable.append(impedanceRealPart)
                self.impedanceAngleTable.append(impedanceAngle)
                self.impedanceTable.append(impedanceModule)
                self.frequencyTable.append(f)
        elif self.choice == 'Rezystor rzeczywisty 3':
            Cr_value = float(self.CrInput.get())*(10**-12)
            R_value = float(self.RInput.get())
            Lr_value = float(self.LrInput.get())*(10**-6)
            Lw_value = float(self.LwInput.get())*(10**-6)
            self.f_rez = (1/(2*math.pi*math.sqrt(Cr_value*Lr_value)))/1000
            for f in range(Fmin_value,Fmax_value,Fstep_value):
                omega = 2*math.pi*f*1000
                resistance = R_value/(((omega**2)*(R_value**2)*(Cr_value**2))+((omega**4)*(Lr_value**2)*(Cr_value**2))-(2*(omega**2)*Lr_value*Cr_value)+1)
                reactance = (-((omega**3)*(Lr_value**2)*Cr_value)+(omega*Lr_value)-(omega*(R_value**2)*Cr_value)+(omega*Lw_value*((((omega**2)*(R_value**2)*(Cr_value**2))+((omega**4)*(Lr_value**2)*(Cr_value**2))-(2*(omega**2)*Lr_value*Cr_value)+1))))/(((omega**2)*(R_value**2)*(Cr_value**2))+((omega**4)*(Lr_value**2)*(Cr_value**2))-(2*(omega**2)*Lr_value*Cr_value)+1)
                impedance = np.complex(resistance,reactance)
              
                impedanceModule = np.absolute(impedance)
                impedanceAngle = np.angle(impedance,deg=True)
                impedanceRealPart = np.real(impedance)
                impedanceImaginaryPart = np.imag(impedance)

                self.imaginaryPartTable.append(impedanceImaginaryPart)
                self.realPartTable.append(impedanceRealPart)
                self.impedanceAngleTable.append(impedanceAngle)
                self.impedanceTable.append(impedanceModule)
                self.frequencyTable.append(f)
        elif self.choice == 'Cewka rzeczywista':
            Cr_value = float(self.CrInput.get())*(10**-12)
            Rs_value = float(self.RsInput.get())
            L_value = float(self.LInput.get())*(10**-6)
            self.f_rez = (1/(2*math.pi*math.sqrt(Cr_value*L_value)))
            for f in range(Fmin_value,Fmax_value,Fstep_value):
                omega = 2*math.pi*f*1000
                resistance = Rs_value/(((omega**2)*(Rs_value**2)*(Cr_value**2))+((omega**4)*(L_value**2)*(Cr_value**2))-(2*(omega**2)*L_value*Cr_value)+1)
                reactance = (-((omega**3)*(L_value**2)*Cr_value)+(omega*L_value)-(omega*(Rs_value**2)*Cr_value))/(((omega**2)*(Rs_value**2)*(Cr_value**2))+((omega**4)*(L_value**2)*(Cr_value**2))-(2*(omega**2)*L_value*Cr_value)+1)
                impedance = np.complex(resistance,reactance)
              
                impedanceModule = np.absolute(impedance)
                impedanceAngle = np.angle(impedance,deg=True)
                impedanceRealPart = np.real(impedance)
                impedanceImaginaryPart = np.imag(impedance)

                self.imaginaryPartTable.append(impedanceImaginaryPart)
                self.realPartTable.append(impedanceRealPart)
                self.impedanceAngleTable.append(impedanceAngle)
                self.impedanceTable.append(impedanceModule)
                self.frequencyTable.append(f)
        elif self.choice == 'Kondensator rzeczywisty':
            C_value = float(self.CInput.get())*(10**-12)
            Ru_value = float(self.RuInput.get())
            Rs_value = float(self.RsInput.get())
            Lr_value = float(self.LrInput.get())*(10**-6)
            self.f_rez = (1/(2*math.pi*math.sqrt(C_value*Lr_value)))
            for f in range(Fmin_value,Fmax_value,100):
                omega = 2*math.pi*f*1000
                resistance = (Ru_value+(Rs_value*((Ru_value**2)*(omega**2)*(C_value**2)+1)))/((Ru_value**2)*(omega**2)*(C_value**2)+1)
                reactance = ((((Ru_value**2)*-omega*C_value)+(omega*Lr_value*((Ru_value**2)*(omega**2)*(C_value**2)+1)))/((Ru_value**2)*(omega**2)*(C_value**2)+1))
                impedance = np.complex(resistance,reactance)
              
                impedanceModule = np.absolute(impedance)
                impedanceAngle = np.angle(impedance,deg=True)
                impedanceRealPart = np.real(impedance)
                impedanceImaginaryPart = np.imag(impedance)

                self.imaginaryPartTable.append(impedanceImaginaryPart)
                self.realPartTable.append(impedanceRealPart)
                self.impedanceAngleTable.append(impedanceAngle)
                self.impedanceTable.append(impedanceModule)
                self.frequencyTable.append(f)
        else:
            print('Brak modelu obliczenia')
        self.drawChart()
        #Trzeba zrobić hihihxD
        

    def checkBoxes(self):
        self.impedanceModuleB = tk.IntVar(value=1)
        self.impedanceModule = tk.Checkbutton(self.checkBoxFrame, text='Moduł impedancji', variable=self.impedanceModuleB) 
        self.impedanceModule.grid(column=0,row=0, sticky=W)
        self.impedanceAngleB = tk.IntVar(value=1)
        self.impedanceAngle = tk.Checkbutton(self.checkBoxFrame, text='Kąt impedancji', variable=self.impedanceAngleB) 
        self.impedanceAngle.grid(column=0,row=1, sticky=W)
        self.realPartB = tk.IntVar(value=1)
        self.realPart = tk.Checkbutton(self.checkBoxFrame, text='Część rzeczywista', variable=self.realPartB) 
        self.realPart.grid(column=0,row=2, sticky=W)
        self.imaginaryPartB = tk.IntVar(value=1)
        self.imaginaryPart = tk.Checkbutton(self.checkBoxFrame, text='Część urojona', variable=self.imaginaryPartB) 
        self.imaginaryPart.grid(column=0,row=3, sticky=W)
        
    def displaySelected(self, choice):
        self.choice = self.clicked.get()
        self.functionDisplaySchemes()
        self.choiceInput()
        
    # def combineFunction(self, *funcs):
    #     def combinedFunction(*args, **kwargs):
    #         for f in funcs:
    #             f(*args,**kwargs)
    #     return combinedFunction
        
    def functionDisplaySchemes(self):
        scheme1 = ImageTk.PhotoImage(Image.open('schemes/Rideal.png'))
        scheme2 = ImageTk.PhotoImage(Image.open('schemes/Rreal1.png'))
        scheme3 = ImageTk.PhotoImage(Image.open('schemes/Rreal2.png'))
        scheme4 = ImageTk.PhotoImage(Image.open('schemes/Rreal3.png'))
        scheme5 = ImageTk.PhotoImage(Image.open('schemes/Lideal.png'))
        scheme6 = ImageTk.PhotoImage(Image.open('schemes/Lreal.png'))
        scheme7 = ImageTk.PhotoImage(Image.open('schemes/Cideal.png'))
        scheme8 = ImageTk.PhotoImage(Image.open('schemes/Creal.png'))
        
        if self.choice == 'Rezystor idealny':
            self.schemeLabel.config(image=scheme1)
            self.schemeLabel.image = scheme1
        elif self.choice == 'Rezystor rzeczywisty 1':
            self.schemeLabel.config(image=scheme2)
            self.schemeLabel.image = scheme2
        elif self.choice == 'Rezystor rzeczywisty 2':
            self.schemeLabel.config(image=scheme3)
            self.schemeLabel.image = scheme3
        elif self.choice == 'Rezystor rzeczywisty 3':
            self.schemeLabel.config(image=scheme4)
            self.schemeLabel.image = scheme4
        elif self.choice == 'Cewka idealna':
            self.schemeLabel.config(image=scheme5)
            self.schemeLabel.image = scheme5
        elif self.choice == 'Cewka rzeczywista':
            self.schemeLabel.config(image=scheme6)
            self.schemeLabel.image = scheme6
        elif self.choice == 'Kondensator idealny':
            self.schemeLabel.config(image=scheme7)
            self.schemeLabel.image = scheme7
        elif self.choice == 'Kondensator rzeczywisty':
            self.schemeLabel.config(image=scheme8)
            self.schemeLabel.image = scheme8
        

    def choiceInput(self):
        self.inputFrame.destroy()
        self.inputFrame = tk.Frame(self)
        if self.choice == 'Rezystor idealny':
            self.idealRModel()
        elif self.choice == 'Rezystor rzeczywisty 1':
            self.real1RModel()
        elif self.choice == 'Rezystor rzeczywisty 2':
            self.real2RModel()
        elif self.choice == 'Rezystor rzeczywisty 3':
            self.real3RModel()
        elif self.choice == 'Cewka idealna':
            self.idealLModel()
        elif self.choice == 'Cewka rzeczywista':
            self.realLModel()
        elif self.choice == 'Kondensator idealny':
            self.idealCModel()
        elif self.choice == 'Kondensator rzeczywisty':
            self.realCModel()
        
   
    def idealRModel(self):
        #self.inputFrame = tk.Frame(self)
        self.inputFrame.grid(column=1, row=1,padx=30)
        self.RInput = tk.Entry(self.inputFrame)
        self.RInput.grid(column=1,row=0, sticky=W)
        RLabel = tk.Label(self.inputFrame, text='R')
        RLabel.grid(column=0,row=0, sticky=W)
        RUnitLabel = tk.Label(self.inputFrame, text='Ω')
        RUnitLabel.grid(column=3,row=0, sticky=W)
        self.Fmin = tk.Entry(self.inputFrame)
        self.Fmin.grid(column=1, row=1, sticky=W)
        FminLabel = tk.Label(self.inputFrame, text='Fmin')
        FminLabel.grid(column=0, row=1, sticky=W)
        FminUnitLabel = tk.Label(self.inputFrame, text='kHz')
        FminUnitLabel.grid(column=3, row=1, sticky=W)
        self.Fmax = tk.Entry(self.inputFrame)
        self.Fmax.grid(column=1, row=2, sticky=W)
        FmaxLabel = tk.Label(self.inputFrame, text='Fmax')
        FmaxLabel.grid(column=0, row=2, sticky=W)
        FmaxUnitLabel = tk.Label(self.inputFrame, text='kHz')
        FmaxUnitLabel.grid(column=3, row=2, sticky=W)

    def real1RModel(self):
        #self.inputFrame = tk.Frame(self)
        self.inputFrame.grid(column=1, row=1,padx=30)
        self.RInput = tk.Entry(self.inputFrame)
        self.RInput.grid(column=1,row=0, sticky=W)
        RLabel = tk.Label(self.inputFrame, text='R')
        RLabel.grid(column=0,row=0, sticky=W)
        RUnitLabel = tk.Label(self.inputFrame, text='Ω')
        RUnitLabel.grid(column=3,row=0, sticky=W)
        self.CrInput = tk.Entry(self.inputFrame)
        self.CrInput.grid(column=1,row=1, sticky=W)
        CrLabel = tk.Label(self.inputFrame, text='Cr')
        CrLabel.grid(column=0,row=1, sticky=W)
        CrUnitLabel = tk.Label(self.inputFrame, text='pF')
        CrUnitLabel.grid(column=3,row=1, sticky=W)
        self.Fmin = tk.Entry(self.inputFrame)
        self.Fmin.grid(column=1, row=2, sticky=W)
        FminLabel = tk.Label(self.inputFrame, text='Fmin')
        FminLabel.grid(column=0, row=2, sticky=W)
        FminUnitLabel = tk.Label(self.inputFrame, text='kHz')
        FminUnitLabel.grid(column=3, row=2, sticky=W)
        self.Fmax = tk.Entry(self.inputFrame)
        self.Fmax.grid(column=1, row=3, sticky=W)
        FmaxLabel = tk.Label(self.inputFrame, text='Fmax')
        FmaxLabel.grid(column=0, row=3, sticky=W)
        FmaxUnitLabel = tk.Label(self.inputFrame, text='kHz')
        FmaxUnitLabel.grid(column=3, row=3, sticky=W)

    def real2RModel(self):
        #self.inputFrame = tk.Frame(self)
        self.inputFrame.grid(column=1, row=1,padx=30)
        self.RInput = tk.Entry(self.inputFrame)
        self.RInput.grid(column=1,row=0, sticky=W)
        RLabel = tk.Label(self.inputFrame, text='R')
        RLabel.grid(column=0,row=0, sticky=W)
        RUnitLabel = tk.Label(self.inputFrame, text='Ω')
        RUnitLabel.grid(column=3,row=0, sticky=W)
        self.CrInput = tk.Entry(self.inputFrame)
        self.CrInput.grid(column=1,row=1, sticky=W)
        CrLabel = tk.Label(self.inputFrame, text='Cr')
        CrLabel.grid(column=0,row=1, sticky=W)
        CrUnitLabel = tk.Label(self.inputFrame, text='pF')
        CrUnitLabel.grid(column=3,row=1, sticky=W)
        self.LrInput = tk.Entry(self.inputFrame)
        self.LrInput.grid(column=1,row=2, sticky=W)
        LrLabel = tk.Label(self.inputFrame, text='Lr')
        LrLabel.grid(column=0,row=2, sticky=W)
        LrUnitLabel = tk.Label(self.inputFrame, text='µH')
        LrUnitLabel.grid(column=3,row=2, sticky=W)
        self.Fmin = tk.Entry(self.inputFrame)
        self.Fmin.grid(column=1, row=3, sticky=W)
        FminLabel = tk.Label(self.inputFrame, text='Fmin')
        FminLabel.grid(column=0, row=3, sticky=W)
        FminUnitLabel = tk.Label(self.inputFrame, text='kHz')
        FminUnitLabel.grid(column=3, row=3, sticky=W)
        self.Fmax = tk.Entry(self.inputFrame)
        self.Fmax.grid(column=1, row=4, sticky=W)
        FmaxLabel = tk.Label(self.inputFrame, text='Fmax')
        FmaxLabel.grid(column=0, row=4, sticky=W)
        FmaxUnitLabel = tk.Label(self.inputFrame, text='kHz')
        FmaxUnitLabel.grid(column=3, row=4, sticky=W)


    def real3RModel(self):
        #self.inputFrame = tk.Frame(self)
        self.inputFrame.grid(column=1, row=1,padx=30)
        self.RInput = tk.Entry(self.inputFrame)
        self.RInput.grid(column=1,row=0, sticky=W)
        RLabel = tk.Label(self.inputFrame, text='R')
        RLabel.grid(column=0,row=0, sticky=W)
        RUnitLabel = tk.Label(self.inputFrame, text='Ω')
        RUnitLabel.grid(column=3,row=0, sticky=W)
        self.CrInput = tk.Entry(self.inputFrame)
        self.CrInput.grid(column=1,row=1, sticky=W)
        CrLabel = tk.Label(self.inputFrame, text='Cr')
        CrLabel.grid(column=0,row=1, sticky=W)
        CrUnitLabel = tk.Label(self.inputFrame, text='pF')
        CrUnitLabel.grid(column=3,row=1, sticky=W)
        self.LrInput = tk.Entry(self.inputFrame)
        self.LrInput.grid(column=1,row=2, sticky=W)
        LrLabel = tk.Label(self.inputFrame, text='Lr')
        LrLabel.grid(column=0,row=2, sticky=W)
        LrUnitLabel = tk.Label(self.inputFrame, text='µH')
        LrUnitLabel.grid(column=3,row=2, sticky=W)
        self.LwInput = tk.Entry(self.inputFrame)
        self.LwInput.grid(column=1,row=3, sticky=W)
        LwLabel = tk.Label(self.inputFrame, text='Lw')
        LwLabel.grid(column=0,row=3, sticky=W)
        LwUnitLabel = tk.Label(self.inputFrame, text='µH')
        LwUnitLabel.grid(column=3,row=3, sticky=W)
        self.Fmin = tk.Entry(self.inputFrame)
        self.Fmin.grid(column=1, row=4, sticky=W)
        FminLabel = tk.Label(self.inputFrame, text='Fmin')
        FminLabel.grid(column=0, row=4, sticky=W)
        FminUnitLabel = tk.Label(self.inputFrame, text='kHz')
        FminUnitLabel.grid(column=3, row=4, sticky=W)
        self.Fmax = tk.Entry(self.inputFrame)
        self.Fmax.grid(column=1, row=5, sticky=W)
        FmaxLabel = tk.Label(self.inputFrame, text='Fmax')
        FmaxLabel.grid(column=0, row=5, sticky=W)
        FmaxUnitLabel = tk.Label(self.inputFrame, text='kHz')
        FmaxUnitLabel.grid(column=3, row=5, sticky=W)

    def idealLModel(self):
        #self.inputFrame = tk.Frame(self)
        self.inputFrame.grid(column=1, row=1,padx=30)
        self.LInput = tk.Entry(self.inputFrame)
        self.LInput.grid(column=1,row=0, sticky=W)
        LLabel = tk.Label(self.inputFrame, text='L')
        LLabel.grid(column=0,row=0, sticky=W)
        LUnitLabel = tk.Label(self.inputFrame, text='µH')
        LUnitLabel.grid(column=3,row=0, sticky=W)
        self.Fmin = tk.Entry(self.inputFrame)
        self.Fmin.grid(column=1, row=1, sticky=W)
        FminLabel = tk.Label(self.inputFrame, text='Fmin')
        FminLabel.grid(column=0, row=1, sticky=W)
        FminUnitLabel = tk.Label(self.inputFrame, text='kHz')
        FminUnitLabel.grid(column=3, row=1, sticky=W)
        self.Fmax = tk.Entry(self.inputFrame)
        self.Fmax.grid(column=1, row=2, sticky=W)
        FmaxLabel = tk.Label(self.inputFrame, text='Fmax')
        FmaxLabel.grid(column=0, row=2, sticky=W)
        FmaxUnitLabel = tk.Label(self.inputFrame, text='kHz')
        FmaxUnitLabel.grid(column=3, row=2, sticky=W)

    def realLModel(self):
        #self.inputFrame = tk.Frame(self)
        self.inputFrame.grid(column=1, row=1,padx=30)
        self.RsInput = tk.Entry(self.inputFrame)
        self.RsInput.grid(column=1,row=0, sticky=W)
        RsLabel = tk.Label(self.inputFrame, text='Rs')
        RsLabel.grid(column=0,row=0, sticky=W)
        RsUnitLabel = tk.Label(self.inputFrame, text='Ω')
        RsUnitLabel.grid(column=3,row=0, sticky=W)
        self.CrInput = tk.Entry(self.inputFrame)
        self.CrInput.grid(column=1,row=1, sticky=W)
        CrLabel = tk.Label(self.inputFrame, text='Cr')
        CrLabel.grid(column=0,row=1, sticky=W)
        CrUnitLabel = tk.Label(self.inputFrame, text='pF')
        CrUnitLabel.grid(column=3,row=1, sticky=W)
        self.LInput = tk.Entry(self.inputFrame)
        self.LInput.grid(column=1,row=2, sticky=W)
        LLabel = tk.Label(self.inputFrame, text='L')
        LLabel.grid(column=0,row=2, sticky=W)
        LUnitLabel = tk.Label(self.inputFrame, text='µH')
        LUnitLabel.grid(column=3,row=2, sticky=W)
        self.Fmin = tk.Entry(self.inputFrame)
        self.Fmin.grid(column=1, row=3, sticky=W)
        FminLabel = tk.Label(self.inputFrame, text='Fmin')
        FminLabel.grid(column=0, row=3, sticky=W)
        FminUnitLabel = tk.Label(self.inputFrame, text='kHz')
        FminUnitLabel.grid(column=3, row=3, sticky=W)
        self.Fmax = tk.Entry(self.inputFrame)
        self.Fmax.grid(column=1, row=4, sticky=W)
        FmaxLabel = tk.Label(self.inputFrame, text='Fmax')
        FmaxLabel.grid(column=0, row=4, sticky=W)
        FmaxUnitLabel = tk.Label(self.inputFrame, text='kHz')
        FmaxUnitLabel.grid(column=3, row=4, sticky=W)

    def idealCModel(self):
        #self.inputFrame = tk.Frame(self)
        self.inputFrame.grid(column=1, row=1,padx=30)
        self.CInput = tk.Entry(self.inputFrame)
        self.CInput.grid(column=1,row=0, sticky=W)
        CLabel = tk.Label(self.inputFrame, text='C')
        CLabel.grid(column=0,row=0, sticky=W)
        CUnitLabel = tk.Label(self.inputFrame, text='pF')
        CUnitLabel.grid(column=3,row=0, sticky=W)
        self.Fmin = tk.Entry(self.inputFrame)
        self.Fmin.grid(column=1, row=1, sticky=W)
        FminLabel = tk.Label(self.inputFrame, text='Fmin')
        FminLabel.grid(column=0, row=1, sticky=W)
        FminUnitLabel = tk.Label(self.inputFrame, text='kHz')
        FminUnitLabel.grid(column=3, row=1, sticky=W)
        self.Fmax = tk.Entry(self.inputFrame)
        self.Fmax.grid(column=1, row=2, sticky=W)
        FmaxLabel = tk.Label(self.inputFrame, text='Fmax')
        FmaxLabel.grid(column=0, row=2, sticky=W)
        FmaxUnitLabel = tk.Label(self.inputFrame, text='kHz')
        FmaxUnitLabel.grid(column=3, row=2, sticky=W)

    def realCModel(self):
        self.inputFrame.grid(column=1, row=1,padx=30)
        self.RuInput = tk.Entry(self.inputFrame)
        self.RuInput.grid(column=1,row=0, sticky=W)
        RuLabel = tk.Label(self.inputFrame, text='Ru')
        RuLabel.grid(column=0,row=0, sticky=W)
        RuUnitLabel = tk.Label(self.inputFrame, text='Ω')
        RuUnitLabel.grid(column=3,row=0, sticky=W)
        self.CInput = tk.Entry(self.inputFrame)
        self.CInput.grid(column=1,row=1, sticky=W)
        CLabel = tk.Label(self.inputFrame, text='C')
        CLabel.grid(column=0,row=1, sticky=W)
        CUnitLabel = tk.Label(self.inputFrame, text='pF')
        CUnitLabel.grid(column=3,row=1, sticky=W)
        self.LrInput = tk.Entry(self.inputFrame)
        self.LrInput.grid(column=1,row=2, sticky=W)
        LrLabel = tk.Label(self.inputFrame, text='Lr')
        LrLabel.grid(column=0,row=2, sticky=W)
        LrUnitLabel = tk.Label(self.inputFrame, text='µH')
        LrUnitLabel.grid(column=3,row=2, sticky=W)
        self.RsInput = tk.Entry(self.inputFrame)
        self.RsInput.grid(column=1,row=3, sticky=W)
        RsLabel = tk.Label(self.inputFrame, text='Rs')
        RsLabel.grid(column=0,row=3, sticky=W)
        RsUnitLabel = tk.Label(self.inputFrame, text='Ω')
        RsUnitLabel.grid(column=3,row=3, sticky=W)
        self.Fmin = tk.Entry(self.inputFrame)
        self.Fmin.grid(column=1, row=4, sticky=W)
        FminLabel = tk.Label(self.inputFrame, text='Fmin')
        FminLabel.grid(column=0, row=4, sticky=W)
        FminUnitLabel = tk.Label(self.inputFrame, text='kHz')
        FminUnitLabel.grid(column=3, row=4, sticky=W)
        self.Fmax = tk.Entry(self.inputFrame)
        self.Fmax.grid(column=1, row=5, sticky=W)
        FmaxLabel = tk.Label(self.inputFrame, text='Fmax')
        FmaxLabel.grid(column=0, row=5, sticky=W)
        FmaxUnitLabel = tk.Label(self.inputFrame, text='kHz')
        FmaxUnitLabel.grid(column=3, row=5, sticky=W)

    def drawChart(self):
        graph = Figure(figsize=(6.7,3.5),tight_layout=True)
        result = graph.add_subplot(111)
        result.grid(visible=True,axis='both', which='both')
        result.set_xlabel('Częstotliwość [kHz]')
        result.set_ylabel('Impedancja [Ω]')
        result2 = result.twinx()
        result2.set_ylabel('Kąt Impedancji [°]')
        result.set_xscale('log')

        if self.f_rez <= 0:
            pass
        else:
            result.axvline(x=self.f_rez,ls='--',color='black')

        if self.impedanceModuleB.get() == 1:
            result.plot(self.frequencyTable,self.impedanceTable, label='Moduł impedancji')
        else:
            pass
        if self.impedanceAngleB.get() == 1:
            result2.plot(self.frequencyTable,self.impedanceAngleTable, label='Kąt impedancji',c='r')
        else:
            pass
        if self.realPartB.get() == 1:
            result.plot(self.frequencyTable,self.realPartTable, label='Część rzeczywista')
        else:
            pass
        if self.imaginaryPartB.get() == 1:
            result.plot(self.frequencyTable,self.imaginaryPartTable, label='Część urojona')
        else:
            pass

        

        lines, labels = result.get_legend_handles_labels()
        lines2, labels2 = result2.get_legend_handles_labels()
        result.legend(lines+lines2,labels+labels2,loc=8,ncol=4,fontsize='xx-small',bbox_to_anchor=(0.5,-0.35))

        self.canvas = FigureCanvasTkAgg(graph, self.chartFrame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
        
        
    


if __name__ == '__main__':
    app = App()
    app.mainloop()