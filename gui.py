import tkinter as tk
from tkinter.constants import DISABLED
from tkinter.scrolledtext import ScrolledText
import ply.lex as lex
import main
import ply.yacc as yacc
import sintactical as sinc

root = tk.Tk()         #Carlos Moncayo
root.title("Analizador Semántico")
root.config(width=1000, height=600)

output = ScrolledText(root)
output.place(x=550, y=50,width=425,height=500)
output.config(state="disabled")

input= ScrolledText(root)
input.place(x=50, y=50,width=375,height=200)

inputLabel=tk.Label(root,text="Entrada")
inputLabel.place(x=50,y=20)

outputLabel=tk.Label(root,text="Análisis léxico")
outputLabel.place(x=550,y=20)


lexerLabel=tk.Label(root,text="Análisis sintáctico-semántico")
lexerLabel.place(x=50,y=270)

lexerOutput = ScrolledText(root)
lexerOutput.place(x=50, y=300,width=375,height=250)
lexerOutput.config(state="disabled")

def analisis():
    data = str(input.get(1.0,tk.END))
    main.lexer.input(data)
    lexerOutput.config(state="normal") #activa la caja
    lexerOutput.delete('1.0', tk.END) #limpia la caja
    output.config(state="normal")
    output.delete('1.0', tk.END)

    while True:
        tok = main.lexer.token()
        if not tok:
            break  # No more input
        output.insert(tk.END, str(tok)+"\n")
        
    syntax=sinc.sintaxAnalisys(data)
    if len(sinc.errors)==0 and len(main.error)==0:
        lexerOutput.insert(tk.END,"\n"+"No syntax error!")
    else:
        for k in main.error:
            output.insert(tk.END, "\n"+k)
            lexerOutput.insert(tk.END, "\n"+"Unknown expression error")
        for i in sinc.errors:
            lexerOutput.insert(tk.END, "\n"+i)
    sinc.errors.clear()
    main.error.clear()
    lexerOutput.config(state="disabled")
    output.config(state="disabled")
#Carlos Moncayo
boton=tk.Button(root,text="Analizar",command=analisis)#,command=numOpAction
boton.place(x=435,y=50)


root.mainloop()