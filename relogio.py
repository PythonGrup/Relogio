import tkinter
from time import strftime

def tic():
    rel['text'] = strftime('%H:%M:%S') #Formato padrão da hora

def tac():
    tic()
    rel.after(1000, tac) #atualizar a cada um segundo

rel = tkinter.Label()
rel['font'] = 'Helvetica 60 bold' #tipo da fonte e tamanho
rel.pack()
tac()
# para que funcione como um script, temos que chamar mainloop,
# senão o programa termina imediatamente após a chamada tac()
rel.mainloop()
