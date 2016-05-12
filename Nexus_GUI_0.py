# -*- coding: utf-8 -*-
from Tkinter import *
import serial
import time


class App:
    def __init__(self, master):

        #Cria um frame e divide ele em uma matriz
        frame = Frame(master)
        frame.grid(row = 3, column = 12)

        #Cria os botões com nome text e que executa o command
        self.avan = Button(frame, text="Avançar", command=ser.write('1'))
        self.avan.grid(row=1, column=2)

        self.re = Button(frame, text="Retroceder", command=ser.write('2'))
        self.re.grid(row=3, column=2)

        self.esquerda = Button(frame, text="Esquerda", command=ser.write('3'))
        self.esquerda.grid(row=2, column=1)

        self.direita = Button(frame, text="Direita", command=ser.write('4'))
        self.direita.grid(row=2, column=3)

        self.rode = Button(frame, text="Girar Esquerda", command=ser.write('5'))
        self.rode.grid(row=2, column = 9)

        self.rodd = Button(frame, text="Girar Direita", command=ser.write('6'))
        self.rodd.grid(row = 2, column = 11)

        self.parar = Button(frame, text="Parar", command=ser.write('7'))
        self.parar.grid(row = 2, column = 5)

        self.auto = Button(frame, text="auto", command=ser.write('8'))
        self.auto.grid(row = 2, column = 7)    
            
        
        


#Função que inicia a comunicação serial
def init_serial():
    COMNUM = 1
    global ser #Cria uma variável global para se usar fora da função
    port = '/dev/ttyUSB0'
    ser = serial.Serial(port)  #Define a leitura na porta entre ''
    ser.baudrate = 9600   #Configura a comunicação pra 9600 bits/s

    ser.timeout = 10

    #Verifica se a porta serial esta aberta
    if ser.isOpen():
        print 'Open: ' + port


init_serial() #Inicia a comunicação serial

time.sleep(1) #Espera antes de executar alguma coisa, assim evitamos erros na comunicação

root = Tk()   #Cria a ierarquia
app = App(root) #Inicia nosso aplicativo
root.mainloop() #Executa o root em loop
