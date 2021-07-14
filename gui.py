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

""" def numOpAction():                        #Carlos Moncayo
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
    output.config(state="disabled") """

#Maria
""" 
def arrayOpAction():   
    lexicTokens = []
    data = str(input.get())
    main.lexer.input(data)
    lexerOutput.config(state="normal") #activa la caja
    lexerOutput.delete('1.0', tk.END) #limpia la caja
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

    #valida que sea un arreglo
    if(lexicTokens[3]=='OPEN_BRACKET' and lexicTokens[4]=='OPEN_BRACKET'):
        output.insert(tk.END, "Orden semántico incorrecto, no pueden haber 2 OPEN BRACKET \n")

    contador = 0
    for i in range(0,len(lexicTokens)):
        if lexicTokens[i] == "CLOSE_BRACKET":
            contador = contador +1

    if contador>1:
        output.insert(tk.END, "Orden semántico incorrecto, no puede haber más de 1 CLOSE BRACKET \n")

    for i in range(0, len(lexicTokens)):
        if lexicTokens[i] == "CLOSE_BRACKET":
            if lexicTokens[i + 1] != "SEMICOLON":
                output.insert(tk.END, "Orden semántico incorrecto, debe haber un semicolon al cerrar el array\n")

    #valida POP
    if 'POP' in lexicTokens:
        validarPopTemp = ['NAME', 'POINT', 'POP', 'OPEN_PARENTHESIS', 'CLOSE_PARENTHESIS', 'SEMICOLON']
        validarPop = validarPopTemp[::-1]
        validarPop1 = validarPop[0:6]
        validarPop2 = validarPop1[::-1]

        if(validarPop2 == validarPopTemp):
            output.insert(tk.END, "Orden semántico correcto \n")
        else:
            output.insert(tk.END, "Orden semántico incorrecto, así no se escribe una función\n")
 """
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