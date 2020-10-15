import ctypes
from tkinter import *
import random
from tkinter import messagebox
import os
import subprocess
import webbrowser

fixedNumber = 0
intentos = 3

def avanzar():
    inputString = entry.get()
    newString = ""
    for i in inputString:
        if (i.isnumeric()):
            newString += i
        else:
            messagebox.showerror(message="Acaso '" + i + "' es un número?", title="Error")
            messagebox.showerror(message="No escribas letras, o reiniciaré tu PC", title="AVISO IMPORTANTE")
    if (messagebox.askyesno(message="Usted ha elegido " + newString + " ¿Desea continuar?",
                            title="Esto es un título, ignóralo")):
        if (messagebox.askyesno(message="Usted ha elegido " + newString + " ¿Realmente desea continuar?",
                                title="Esto es un título, ignóralo")):
            if (messagebox.askyesno(message="¿Estas realmente seguro de que quieres continuar?",
                                    title="Esto es un título, ignóralo")):
                if (messagebox.askyesno(message="Pulsa 'Yes' para continuar", title="Esta vez no ignores el título")):
                    messagebox.showerror(message="Usted ha elegido continuar, buena suerte!", title="Esto es un título")
                    global fixedNumber
                    fixedNumber = random.randint(0, int(newString))
                    label.config(text="Intenta adivinar el número: ")
                    label.place(relx=0.418, rely=0.4, anchor='center')
                    buton.config(text="Comprobar", command=avanzar2)
                    buton.place(relx=0.18, rely=0.69, anchor='center')
                    entry.delete(0, 'end')
                    entry.insert(0, "0")
                    #messagebox.showinfo(message=str(fixedNumber), title="Debuc")  # Debug, solo DEBUG, NO DESCOMENTAR!!!
                    #        labelIntentos.place(relx=4, rely=0.1, anchor='center')
                    labelIntentos.pack()

def abrirCosas(repetitions):
    for x in range(repetitions):
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')
        subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
        subprocess.Popen('C:\\Windows\\System32\\mspaint.exe')
        subprocess.Popen(r'explorer /select,"C:"')
        subprocess.Popen('C:\\Windows\\System32\\control.exe')
        webbrowser.open("https://www.google.com/search?client=firefox-b-d&q=pacman")
    exit()

def avanzar2():
    global intentos
    if (intentos >= 1):
        intentos -= 1
        labelIntentos.config(text="Intentos: " + str(intentos))
        inputString = entry.get()
        newString = ""
        for i in inputString:
            if (i.isnumeric()):
                newString += i
        if (int(newString) == fixedNumber):
            for a in range(10):
                messagebox.showerror(message="BIEN, HAS ACERTADO!", title="Esto es un título, ignóralo")
            if (messagebox.askretrycancel(message="Quiere usted volver a jugar?", title="Esto es un título, ignóralo")):
                os.execv(sys.executable, ['python'] + sys.argv)
            else:
                messagebox.showerror(message="Por que no?", title="Por que no?")
                if (messagebox.askyesno(message="No te ha gustado este maravilloso juego?", title="Hehe")):
                    messagebox.showinfo(message="Bien, vuelve cuando quieras!", title="Bien")
                    messagebox.showinfo(message="Hasta pronto!", title="Hasta pronto!")
                    ctypes.windll.user32.LockWorkStation()
                else:
                    if (messagebox.askyesno(message="Esta usted seguro de su respuesta?", title=":/")):
                        for x in range(20):
                            messagebox.showerror(message="Cómo te atreves?" * x, title="Cómo??" * x)
                        messagebox.showerror(message="Tu PC se va a volver loco, buena suerte ;)", title="T de Título")
                        abrirCosas(10)
                    else:
                        messagebox.showerror(message="Lamentamos mucho que no te haya gustado, esperamos verte pronto.",
                                             title=":/")
                        for y in range(40):
                            messagebox.showerror(message=":(" * y, title=":(" * y)
                        abrirCosas(4)
        else:
            messagebox.showerror(message="Has fallado, vuelve a intentarlo", title="Esto es un título, ignóralo")
    else:
        messagebox.showerror(message="Has perdido, no tienes mas intentos", title="Esto es un título")
        labelIntentos.config(text="Intentos: 0 ")
        labelIntentos.config(fg='red')

        if (messagebox.askyesno(message="Quieres comprar mas intentos?", title="Esto no es un título")):
            messagebox.showerror(message="Vas a ser redirigido a la pagina de compra", title="Esto no es un título")
            webbrowser.open("https://www.google.com/search?client=firefox-b-d&q=pacman")
        else:
            if (messagebox.askyesno(message="Quieres reiniciar el juego?", title="Esto no es un título")):
                os.execv(sys.executable, ['python'] + sys.argv)
            else:
                messagebox.showerror(message="Te recomiendo que reinicies", title="Esto no, NO es un título")


root = Tk()
root.configure(bg='#ffffff')
root.resizable(False, False)
root.title("Esto es un título, ignóralo")
root.geometry("800x600")

label = Label(root, text="Elige el número máximo: ", font=("Futura 30 bold"), fg="#1d1d1b", bg="#ffffff")
label.place(relx=0.394, rely=0.4, anchor='center')

labelIntentos = Label(root, text="Intentos: 3", font=("Futura 50 bold"), fg="#1d1d1b", bg="#ffffff")
labelIntentos.pack_forget()

entry = Entry(root, width=10, font=("Futura", 20, "bold"), fg="#1d1d1b", highlightthickness=10,
              highlightcolor="#1d1d1b", highlightbackground="#1d1d1b")
entry.insert(0, "10")
entry.place(relx=0.205, rely=0.54, anchor='center')

buton = Button(root, text="Continuar", font=("Futura", 15, "bold"), fg="#ffffff", bg="#03DAC5",
               highlightbackground="#30D2B2", command=avanzar, highlightthickness=5)
buton.place(relx=0.169, rely=0.7, anchor='center')

root.mainloop()
