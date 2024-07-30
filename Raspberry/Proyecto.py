# Control GPIO en fisico

from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
import os
import time
import subprocess
import RPi.GPIO as GPIO
import pygame


#Crear ventana
v0=Tk()
v0.title("CONTROL DE MICROPROCESADOR")
v0.geometry("500x350+0+0")

#Declarar variables
text1 = font.Font(family="Arial", size=20)
text2 = font.Font(family="Helvetica", size=80)

# ENCENDIDOS
dirOn17 = f"sudo /./home/julian/on17.sh" #LUZ ROJA
dirOn22 = f"sudo /./home/julian/on22.sh" #LUZ VERDE

# APAGADOS
dirOff17 = f"sudo /./home/julian/off17.sh" #LUZ ROJA
dirOff22 = f"sudo /./home/julian/off22.sh" #LUZ VERDE

# TXT
dirTxt27 = f"/home/julian/estado.txt"

# DIRRECION DEL CORREO
dirEmail27 = f"/home/julian/lectura.sh"

dirsensorPIR = f"/home/julian/sensorPIR.sh"

def actualiza201():
    pf1 = open(dirTxt27, "r")
    for linea in pf1:
        campo = linea.split("\n")
        campof = campo[0]
        if campof == "1":
            label_on = Label(v0, text="1", font=text2).place(x=250, y=50)
            v0.after(1000, actualiza201)
        if campof == "0":
            label_off = Label(v0, text="0", font=text2).place(x=250, y=50)
            v0.after(1000, actualiza201)

actualiza201()

img_on = PhotoImage(file="on.gif")
img_off = PhotoImage(file="off.gif")


def actualiza202():
    pf2 = open(dirTxt27, "r")
    for linea2 in pf2:
        campo = linea2.split("\n")
        campof = campo[0]
        if campof == "1":
            btn_on = Button(v0, image=img_on).place(x=350, y=50)
            v0.after(1000, actualiza202)
        if campof == "0":
            btn_off = Button(v0, image=img_off).place(x=350, y=50)
            v0.after(1000, actualiza202)


# Llamar Funcion
actualiza202()
   

def on():

    os.system(dirOn22)
    os.system(dirOff17)
    


def off():
    os.system(dirOn17)
    os.system(dirOff22)


def Tiempo():
    ct=str(checkt.get())
    if (ct == "1"):
        def Register():
            hi = str(horai.get())
            mi = str(minini.get())
            hf = str(horaf.get())
            mf = str(minf.get())
            tab = " "
            dia = "*"
            mes = "*"
            ano = "*"
            user = "root"
            path1 = "sudo /./home/julian/onTem.sh"
            path2 = "sudo /./home/julian/offTem.sh"
            cadena1 = str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path1)
            cadena2 = str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path2)

            #Permisos 777
            os.system("sudo chmod -R 777 /etc/cron.d/accion1")
            os.system("sudo chmod -R 777 /etc/cron.d/accion2")

            # Abrir archivo en modo escritura
            pf1=open("/etc/cron.d/accion1","w")
            pf1.write(cadena1)
            pf1.write("\n")
            pf1.close()

            # Abrir archivo en modo escritura
            pf1=open("/etc/cron.d/accion2","w")
            pf1.write(cadena2)
            pf1.write("\n")
            pf1.close()
            #delay
            time.sleep(0.1)
            #Reversion de permisos 755
            os.system("sudo chmod -R 755 /etc/cron.d/accion1")
            os.system("sudo chmod -R 755 /etc/cron.d/accion2")
            #Reiniciar el servicio cron para aplicar cambios en la tarea
            os.system("sudo /./etc/init.d/cron restart")
        print("Llamar dialogo de tiempo")
        v1=Toplevel()
        v1.title("Configuracion de Tiempo")
        v1.geometry("300x250+200+200")
        #Configurar texto
        text_v1=font.Font(family="Arial",size=12)
        #Etiquetas
        label_hi=Label(v1,text="Hora inicial",font=text_v1).place(x=10,y=50)
        label_mi=Label(v1,text="Minuto inicial",font=text_v1).place(x=10,y=90)
        label_hf=Label(v1,text="Hora final",font=text_v1).place(x=10,y=130)
        label_mf=Label(v1,text="Minuto final",font=text_v1).place(x=10,y=170)
        
        #Cajas de texto 
        global horai,minini,horaf,minf
        horai=StringVar()
        minini=StringVar()
        horaf=StringVar()
        minf=StringVar()
        txt_horai=Entry(v1,textvariable=horai,width=2).place(x=120,y=50)
        txt_minini=Entry(v1,textvariable=minini,width=2).place(x=120,y=90)
        txt_horaf=Entry(v1,textvariable=horaf,width=2).place(x=120,y=130)
        txt_minf=Entry(v1,textvariable=minf,width=2).place(x=120,y=170)
        #Boton
        btn_registrar=Button(v1,text="Registrar",command=Register).place(x=200,y=100)
        v1.mainloop()
    if(ct==0):
        messagebox.showinfo("save",message="Objeto deseleccionado")

def EvaluarRadio20():
    r = radio20.get()
    if r == 1:
        os.system(dirOn22)
        os.system(dirOff17)
    if r == 0:
        off()

def EvaluarCheck27():
    r = check27.get()
    if r == "1":
        os.system(dirOn22)
        os.system(dirOff17)
    if r == "0":
        off()

global proceso_email #Variable global para la parte de los correos
def EvaluarCheckEmail27():
    print("Entro")
    global proceso_email
    r = checkEmail27.get()
    print(r)
    if r == "1":
        print("1")
        proceso_email = subprocess.Popen(["sh",dirEmail27])
    if r == "0" and proceso_email is not None:
        print("0")
        proceso_email.terminate()
        proceso_email = None

global proceso_sensor #Variable global para la parte de los sensores
def EvaluarProcesoSensor():
    print("Entro Sensor")
    global proceso_sensor
    r = checkSensor.get()
    print(r)
    if r == "1":
        print("1")
        proceso_sensor = subprocess.Popen(["python3",dirsensorPIR])
    if r == "0" and proceso_sensor is not None:
        print("0")
        proceso_sensor.terminate()
        proceso_sensor = None



def VerificarCombo27():
    print("Opcion")
    ck = str(combo27.get())
    if ck == "ON":
        on()
    if ck == "OFF":
        off()



global combo27
combo27 = StringVar()
cl20 = ttk.Combobox(v0, textvariable=combo27, values=["ON", "OFF"])
cl20.place(x=50, y=200)
btn_combo = Button(v0, text="CONFIRMAR", command=VerificarCombo27).place(x=230, y=195)

global check27
check27 = StringVar()
c120 = Checkbutton(v0, text="ON/OFF", variable=check27, command=EvaluarCheck27)
c120.place(x=50, y=150)

global checkSensor
checkSensor = StringVar()
c120 = Checkbutton(v0, text="Sensor", variable=checkSensor, command=EvaluarProcesoSensor)
c120.place(x=150, y=150)

global checkEmail27
checkEmail27 = StringVar()
c120 = Checkbutton(v0, text="SISTEMA DE CORREO", variable=checkEmail27, command=EvaluarCheckEmail27)
c120.place(x=50, y=170)

global checktemp
checkt = StringVar()
c120 = Checkbutton(v0, text="Temporizador", variable=checkt, command=Tiempo)
c120.place(x=215, y=170)

global radio20
radio20 = IntVar()
r120 = Radiobutton(v0, text="ON", variable=radio20, value=1, command=EvaluarRadio20)
r120.place(x=50, y=50)
r220 = Radiobutton(v0, text="OFF", variable=radio20, value=0, command=EvaluarRadio20)
r220.place(x=50, y=110)
label_titulo = Label(v0, text="CONTROL DE ESTADO", font=text1).place(x=100, y=10)
btn_on = Button(v0, text="ON", command=on).place(x=150, y=50)
btn_off = Button(v0, text="OFF", command=off).place(x=150, y=110)

v0.mainloop()
