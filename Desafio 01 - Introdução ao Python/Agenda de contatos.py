from Module_1_add_new_contact import addNewContact 
from Module_2_show_contacts import showContacts
from Module_3_update_contact import updateContact
from Module_4_toggle_fav_contact import toggleFavContact
from Module_5_show_fav_contacts import showFavContacts
from Module_6_delete_contact import deleteContact

contacts = []

while True:
    print()
    print('''
Bem vindo ao seu gerenciador de contatos!!
O que voce quer fazer?
1 - Adicionar novo contato
2 - Visualizar contatos
3 - Atualizar contato existente
4 - Marcar contato como favorito
5 - Ver lista de favoritos
6 - Apagar um contato.
7 - Sair do gerenciador
          ''')
    prompt = input("Digite o numero que corresponde a opção escolhida: ")

    if prompt == "1":
        contacts = addNewContact(contacts)
    elif prompt == "2":
        showContacts(contacts)
    elif prompt == "3":
        updateContact(contacts)
    elif prompt == "4":
        toggleFavContact(contacts)
    elif prompt == "5":
        showFavContacts(contacts)
    elif prompt == "6":
        contacts == deleteContact(contacts)
    elif prompt == "7":
        break
    else:
        print("Opção invalida")