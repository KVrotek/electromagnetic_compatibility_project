from tkinter.constants import W
import models
import model
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
        self.impedaceTable = []

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
        self.impedaceTable = []
        if self.choice == 'Rezystor idealny':
            for f in range(int(self.Fmin.get()),int(self.Fmax.get()),10):
                resistance = int(self.RInput.get())
                reactance = 0
                impedance = np.complex(resistance,reactance)
                impedanceModule = np.absolute(impedance)

                self.impedaceTable.append(impedanceModule)
                self.frequencyTable.append(f) 
        self.drawChart()
        #Trzeba zrobić hihihxD
        

    def checkBoxes(self):
        self.impedanceModule = tk.Checkbutton(self.checkBoxFrame, text='Moduł impedancji') 
        self.impedanceModule.grid(column=0,row=0, sticky=W)
        self.impedanceAngle = tk.Checkbutton(self.checkBoxFrame, text='Kąt impedancji') 
        self.impedanceAngle.grid(column=0,row=1, sticky=W)
        self.realPart = tk.Checkbutton(self.checkBoxFrame, text='Część rzeczywista') 
        self.realPart.grid(column=0,row=2, sticky=W)
        self.imaginaryPart = tk.Checkbutton(self.checkBoxFrame, text='Część urojona') 
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
        LInput = tk.Entry(self.inputFrame)
        LInput.grid(column=1,row=0, sticky=W)
        LLabel = tk.Label(self.inputFrame, text='L')
        LLabel.grid(column=0,row=0, sticky=W)
        LUnitLabel = tk.Label(self.inputFrame, text='µH')
        LUnitLabel.grid(column=3,row=0, sticky=W)
        Fmin = tk.Entry(self.inputFrame)
        Fmin.grid(column=1, row=1, sticky=W)
        FminLabel = tk.Label(self.inputFrame, text='Fmin')
        FminLabel.grid(column=0, row=1, sticky=W)
        FminUnitLabel = tk.Label(self.inputFrame, text='Hz')
        FminUnitLabel.grid(column=3, row=1, sticky=W)
        Fmax = tk.Entry(self.inputFrame)
        Fmax.grid(column=1, row=2, sticky=W)
        FmaxLabel = tk.Label(self.inputFrame, text='Fmax')
        FmaxLabel.grid(column=0, row=2, sticky=W)
        FmaxUnitLabel = tk.Label(self.inputFrame, text='Hz')
        FmaxUnitLabel.grid(column=3, row=2, sticky=W)

    def idealCModel(self):
        self.inputFrame.grid(column=1, row=1,padx=30)
        CInput = tk.Entry(self.inputFrame)
        CInput.grid(column=1,row=0, sticky=W)
        CLabel = tk.Label(self.inputFrame, text='C')
        CLabel.grid(column=0,row=0, sticky=W)
        CUnitLabel = tk.Label(self.inputFrame, text='pF')
        CUnitLabel.grid(column=3,row=0, sticky=W)
        Fmin = tk.Entry(self.inputFrame)
        Fmin.grid(column=1, row=1, sticky=W)
        FminLabel = tk.Label(self.inputFrame, text='Fmin')
        FminLabel.grid(column=0, row=1, sticky=W)
        FminUnitLabel = tk.Label(self.inputFrame, text='Hz')
        FminUnitLabel.grid(column=3, row=1, sticky=W)
        Fmax = tk.Entry(self.inputFrame)
        Fmax.grid(column=1, row=2, sticky=W)
        FmaxLabel = tk.Label(self.inputFrame, text='Fmax')
        FmaxLabel.grid(column=0, row=2, sticky=W)
        FmaxUnitLabel = tk.Label(self.inputFrame, text='Hz')
        FmaxUnitLabel.grid(column=3, row=2, sticky=W)

    def drawChart(self):
        graph = Figure(figsize=(6.7,3),tight_layout=True)
        result = graph.add_subplot(111)
        result.grid(visible=True,axis='both', which='both')
        result.set_xlabel('Częstotliwość [Hz]')
        result.set_ylabel('Impedancja [Ω]')
        result.set_xscale('log')
        result.plot(self.frequencyTable,self.impedaceTable)
        self.canvas = FigureCanvasTkAgg(graph, self.chartFrame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
        
        
    


if __name__ == '__main__':
    app = App()
    app.mainloop()