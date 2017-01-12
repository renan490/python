#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# -*- coding: cp1252 -*-
#Este arquivo chama-se agenda.py
#Tkinter é uma biblioteca para interface gráfica.
from Tkinter import *
import tkSimpleDialog
import tkMessageBox
import io
#Muda o botão 1
def press_b1():
    b1['text']='Olá'
def press_b2():
    b2['text']='Adicionar contato'
    nome = tkSimpleDialog.askstring('Nome','Nome do novo contato?')
    telefone = tkSimpleDialog.askstring('Telefone','Telefone do novo contato?')
    quadro.insert(END,"Nome: "+nome+"    Telefone: "+telefone)
    arquivo = open('agenda.txt', 'a')
    arquivo.write("Nome: "+nome.encode('utf8')+"    Telefone: "+telefone+"\n")
    arquivo.close()
def press_b3():
    b3['text']='Remover contato'
    nome = tkSimpleDialog.askstring('Nome','Nome do contato a ser removido?')
    arquivo = open('agenda.txt', 'r')
    Linhas = arquivo.readlines()
    arquivo.close()
    arquivo = open('agenda.txt', 'w')
    for linha in Linhas:
        if nome in linha:
            pass
        else:arquivo.write(linha)
    arquivo.close()
    quadro.delete(0, END)
    try:
        arquivo = open("agenda.txt","r")
        for linha in arquivo:
            quadro.insert(END,linha)
    except:
        print('File cannot be opened: agenda')
    arquivo.close()

    tkMessageBox.showinfo("OK!", "O contato " + nome + " foi removido com sucesso!")
def press_b4():
    b3['text']='Buscar contato'
    nome = tkSimpleDialog.askstring('Nome','Nome do contato a ser pesquisado?')
    arquivo = open('agenda.txt', 'r')
    Linhas = arquivo.readlines()
    for linha in Linhas:
        if nome in linha:
            nome = linha;break
    arquivo.close()
    tkMessageBox.showinfo("OK!", nome)
def press_b5():
    b3['text']='Atualizar contato'
    nome = tkSimpleDialog.askstring('Nome','Nome do contato a ser atualizado?')
    arquivo = open('agenda.txt', 'r')
    Linhas = arquivo.readlines()
    arquivo.close()
    arquivo = open('agenda.txt', 'w')
    for linha in Linhas:
        if nome in linha:
            pass
        else:arquivo.write(linha)
    arquivo.close()
    quadro.delete(0, END)
    try:
        arquivo = open("agenda.txt","r")
        for linha in arquivo:
            quadro.insert(END,linha)
    except:
        print('File cannot be opened: agenda')
    arquivo.close()
    nome = tkSimpleDialog.askstring('Nome','Nome do novo contato?')
    telefone = tkSimpleDialog.askstring('Telefone','Telefone do novo contato?')
    quadro.insert(END,"Nome: "+nome+"    Telefone: "+telefone)
    arquivo = open('agenda.txt', 'a')
    arquivo.write("Nome: "+nome.encode('utf8')+"    Telefone: "+telefone+"\n")
    arquivo.close()
    tkMessageBox.showinfo("OK!", "O contato " + nome + " foi atualizado com sucesso!")
#Criando o frame
frame = Frame()
frame.pack()

cor = 'deepskyblue'
#Botão Clique em mim
b1=Button(frame,text="Clique em mim!",bg=cor,command=press_b1)
b1.pack(side=LEFT)
#Botão Adicionar Contato
b2=Button(frame,text="Adicionar contato",bg=cor,command=press_b2)
b2.pack(side=LEFT)
#Botão Remover Contato
b3=Button(frame,text="Remover contato",bg=cor,command=press_b3)
b3.pack(side=LEFT)
#Botão Pesquisar Contato
b4=Button(frame,text="Pesquisar contato",bg=cor,command=press_b4)
b4.pack(side=LEFT)
#Botão Atualizar Contato
b5=Button(frame,text="Atualizar contato",bg=cor,command=press_b5)
b5.pack(side=LEFT)

#Botão sair
sair = Button(text="Sair",bg=cor, command=quit)
sair.pack(side=BOTTOM)
#O listbox - irá listar os contatos
quadro = Listbox(font="Arial 24",bg='dodgerblue')
quadro.pack(side=LEFT,expand=True,fill="both")
sb = Scrollbar(bg='gray')
sb.pack(side=RIGHT,fill="y")
sb.configure(command=quadro.yview)
quadro.configure(yscrollcommand=sb.set)
#Ler o arquivo e inserir no listbox
try:
    arquivo = open("agenda.txt")
    for linha in arquivo:
        quadro.insert(END,linha)
except:
    print('File cannot be opened: agenda')
arquivo.close()

mainloop()
