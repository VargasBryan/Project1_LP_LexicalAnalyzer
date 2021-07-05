import tkinter as tk
from tkinter.constants import DISABLED
from tkinter.scrolledtext import ScrolledText
import ply.lex as lex
import main
import ply.yacc as yacc
import sintactical as sinc

root = tk.Tk()
root.title("Analizador Semántico")
root.config(width=1000, height=600)

output = ScrolledText(root)
output.place(x=550, y=50,width=425,height=500)

input=tk.Entry(root)
input.place(x=50, y=50,width=225)

inputLabel=tk.Label(root,text="Entrada")
inputLabel.place(x=50,y=20)

outputLabel=tk.Label(root,text="Salida")
outputLabel.place(x=550,y=20)


lexerLabel=tk.Label(root,text="Análisis léxico y sintáctico")
lexerLabel.place(x=50,y=120)

lexerOutput = ScrolledText(root)
lexerOutput.place(x=50, y=150,width=300,height=300)


def numOpAction():
    lexicTokens=[]
    data =str(input.get())
    main.lexer.input(data)
    lexerOutput.config(state="normal")
    lexerOutput.delete('1.0', tk.END)
    output.config(state="normal")
    output.delete('1.0', tk.END)
    while True:
        tok = main.lexer.token()
        if not tok:
            break  # No more input
        token=str(tok)[9:-1]
        token2=token.split(",")
        lexicTokens.append(token2[0])
        lexerOutput.insert(tk.END, str(tok)+"\n")
    sintaxis=sinc.sintaxAnalisys("\n"+str(input.get()))
    lexerOutput.insert(tk.END, "\n"+sintaxis)
    lexerOutput.config(state="disabled")
    print(lexicTokens)
    valida=[]
    for i in range(0,len(lexicTokens)):
        if lexicTokens[i]=="IGUAL":
            analisis=lexicTokens[i+1:]
            counter=0
            while True:
                if(analisis[-1]!="SEMICOLON"):
                    output.insert(tk.END,"Orden semántico incorrecto, se esparaba punto y coma (;)\n")
                    break
                if analisis[counter]=="SEMICOLON":
                    if analisis[counter-1]=="SUMA" or analisis[counter-1]=="RESTA" or analisis[counter-1]=="MULTIPLICACION" or analisis[counter-1]=="DIVISION":
                        output.insert(tk.END,"Orden semántico incorrecto, no se esparaba un operador matematico\n")
                    else:
                        output.insert(tk.END,"Orden semántico correcto\n")
                        output.insert(tk.END,str(valida))
                    break
                if counter==0:
                    if analisis[0]=="NUMBER" or analisis[0]=="NAME":
                        valida.append(analisis[0])
                    else:
                        output.insert(tk.END,"Orden semántico incorrecto, se esparaba un número o una variable\n")
                        break
                elif counter%2==0:
                    if analisis[counter]=="NUMBER" or analisis[counter]=="NAME":
                        valida.append(analisis[counter])
                    else:
                        output.insert(tk.END,"Orden semántico incorrecto, se esparaba un número o una variable\n")
                        break
                else:
                    if analisis[counter]=="SUMA" or analisis[counter]=="RESTA" or analisis[counter]=="MULTIPLICACION" or analisis[counter]=="DIVISION":
                        valida.append(analisis[counter])
                    else:
                        output.insert(tk.END,"Orden semántico incorrecto, se esparaba un operador matematico\n")
                        break
                counter+=1
    output.config(state="disabled")

boton=tk.Button(root,text="Analizar operacion matemática",command=numOpAction)
boton.place(x=280,y=50)

root.mainloop()