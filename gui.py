import tkinter as tk
from tkinter.constants import DISABLED
from tkinter.scrolledtext import ScrolledText
import ply.lex as lex
import main
import ply.yacc as yacc
import sintactical as sinc

root = tk.Tk()
root.title("Analizador Semántico")
root.config(width=800, height=600)

output = ScrolledText(root)
output.insert(tk.END, "hola esto es una prueba:\nodio a la tri")
output.config(state="disabled")
output.place(x=550, y=50,width=225,height=500)

input=tk.Entry(root)
input.place(x=50, y=50,width=225)

inputLabel=tk.Label(root,text="Entrada")
inputLabel.place(x=50,y=20)

outputLabel=tk.Label(root,text="Salida")
outputLabel.place(x=550,y=20)

boton=tk.Button(root,text="Analizar")
boton.place(x=280,y=50)

lexerLabel=tk.Label(root,text="Análisis léxico")
lexerLabel.place(x=50,y=120)

lexerOutput = ScrolledText(root)
#lexerOutput.insert(tk.END, "aqui va el lexer")
#lexerOutput.config(state="disabled")
lexerOutput.place(x=50, y=150,width=300,height=300)

data = ''' 89
"asdasdasd"
hola
""
"
pop
'''

# Give the lexer some input
main.lexer.input(data)
# Tokenize
while True:
    tok = main.lexer.token()
    if not tok:
        break  # No more input
    lexerOutput.insert(tk.END, str(tok)+"\n")
root.mainloop()