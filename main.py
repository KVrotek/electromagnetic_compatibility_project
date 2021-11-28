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

        self.title('RLC in high frequency')

        self.expandListFrame = tk.Frame(self)
        self.expandListFrame.grid(column=0,row=0)
        self.options = ['Rezystor idealny','Rezystor rzeczywisty','Cewka idealna','Cewka rzeczywista','Kondensator idealny',"Kondensator rzeczywisty"]
        self.clicked = tk.StringVar()
        self.clicked.set(self.options[0])
        self.choice = 'Rezystor idealny'
        self.expandList = tk.OptionMenu(self.expandListFrame, self.clicked, *self.options, command=self.displaySelected)
        self.expandList.pack()
        
        self.BtnFrame = tk.Frame(self)
        self.BtnFrame.grid(column=2,row=0)
        self.calculateBtn = tk.Button(self.BtnFrame, text='Oblicz', command=self.calculate)
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
        if self.choice == 'Rezystor idealny':
            for f in range(int(self.Fmin.get()),int(self.Fmax.get()),10):
                resistance = int(self.RInput.get())
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
            for f in range(int(self.Fmin.get()),int(self.Fmax.get()),10):
                omega = 2*math.pi*f
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
            for f in range(int(self.Fmin.get()),int(self.Fmax.get()),10):
                omega = 2*math.pi*f
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
        scheme1 = ImageTk.PhotoImage(Image.open('schemes/1.png'))
        scheme2 = ImageTk.PhotoImage(Image.open('schemes/2.png'))
        scheme3 = ImageTk.PhotoImage(Image.open('schemes/3.png'))
        scheme4 = ImageTk.PhotoImage(Image.open('schemes/4.png'))
        scheme5 = ImageTk.PhotoImage(Image.open('schemes/5.png'))
        scheme6 = ImageTk.PhotoImage(Image.open('schemes/6.png'))
        
        if self.choice == 'Rezystor idealny':
            self.schemeLabel.config(image=scheme1)
            self.schemeLabel.image = scheme1
        elif self.choice == 'Rezystor rzeczywisty':
            self.schemeLabel.config(image=scheme2)
            self.schemeLabel.image = scheme2
        elif self.choice == 'Cewka idealna':
            self.schemeLabel.config(image=scheme3)
            self.schemeLabel.image = scheme3
        elif self.choice == 'Cewka rzeczywista':
            self.schemeLabel.config(image=scheme4)
            self.schemeLabel.image = scheme4
        elif self.choice == 'Kondensator idealny':
            self.schemeLabel.config(image=scheme5)
            self.schemeLabel.image = scheme5
        elif self.choice == 'Kondensator rzeczywisty':
            self.schemeLabel.config(image=scheme6)
            self.schemeLabel.image = scheme6

    def choiceInput(self):
        self.inputFrame.grid_forget()
        if self.choice == 'Rezystor idealny':
            self.idealRModel()
        elif self.choice == 'Cewka idealna':
            self.idealLModel()
        elif self.choice == 'Kondensator idealny':
            self.idealCModel()

    def idealRModel(self):
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
        FminUnitLabel = tk.Label(self.inputFrame, text='Hz')
        FminUnitLabel.grid(column=3, row=1, sticky=W)
        self.Fmax = tk.Entry(self.inputFrame)
        self.Fmax.grid(column=1, row=2, sticky=W)
        FmaxLabel = tk.Label(self.inputFrame, text='Fmax')
        FmaxLabel.grid(column=0, row=2, sticky=W)
        FmaxUnitLabel = tk.Label(self.inputFrame, text='Hz')
        FmaxUnitLabel.grid(column=3, row=2, sticky=W)
    
    def idealLModel(self):
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
        FminUnitLabel = tk.Label(self.inputFrame, text='Hz')
        FminUnitLabel.grid(column=3, row=1, sticky=W)
        self.Fmax = tk.Entry(self.inputFrame)
        self.Fmax.grid(column=1, row=2, sticky=W)
        FmaxLabel = tk.Label(self.inputFrame, text='Fmax')
        FmaxLabel.grid(column=0, row=2, sticky=W)
        FmaxUnitLabel = tk.Label(self.inputFrame, text='Hz')
        FmaxUnitLabel.grid(column=3, row=2, sticky=W)

    def idealCModel(self):
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
        FminUnitLabel = tk.Label(self.inputFrame, text='Hz')
        FminUnitLabel.grid(column=3, row=1, sticky=W)
        self.Fmax = tk.Entry(self.inputFrame)
        self.Fmax.grid(column=1, row=2, sticky=W)
        FmaxLabel = tk.Label(self.inputFrame, text='Fmax')
        FmaxLabel.grid(column=0, row=2, sticky=W)
        FmaxUnitLabel = tk.Label(self.inputFrame, text='Hz')
        FmaxUnitLabel.grid(column=3, row=2, sticky=W)

    def drawChart(self):
        graph = Figure(figsize=(6.7,3.5),tight_layout=True)
        result = graph.add_subplot(111)
        result.grid(visible=True,axis='both', which='both')
        result.set_xlabel('Częstotliwość [Hz]')
        result.set_ylabel('Impedancja [Ω]')
        result2 = result.twinx()
        result2.set_ylabel('Kąt impedancji [°]')
        result.set_xscale('log')

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