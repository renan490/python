# encoding: utf-8

lista=set()
def adicionar():
    lista.add(raw_input("Digite o nome do disco para adicionar: "))
def remover():
    lista.discard(raw_input("Digite o nome do disco para remover: "))
def buscar():
    if raw_input("Digite o nome do Álbum para buscar: ") in lista:print"O item está incluso na lista!"
    else:print"O item não está incluso na lista!"
def editar():
    editar=raw_input("Digite o nome do Álbum para editar: ")
    album=""
    if editar in lista:
        print"Editar \'"+editar+"\':";album=raw_input()
        if album!="":lista.discard(editar);lista.add(album)
def listar():
    if lista!=[]:
        print"Seus Álbuns:\n"
        for i in lista:
            print i
while 1:
    print"\nMenu: \n"
    opcao=input("1. Adicionar elemento\n2. Remover elemento\n3. Buscar\n4. Editar\n5. Listar\n0. Sair\nOpção: ")
    print
    if opcao==1:adicionar()
    if opcao==2:remover()
    if opcao==3:buscar()
    if opcao==4:editar()
    if opcao==5:listar()
    if opcao==0:break
