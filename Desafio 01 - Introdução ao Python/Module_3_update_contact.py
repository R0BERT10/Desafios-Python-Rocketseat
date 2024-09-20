from Module_2_show_contacts import showContacts

def updateContact(contactList:list):
    showContacts(contactList)
    selected = input(f'Informe o "Ind" do contato que deseja atualizar: ')

    try:
        print()
        print("Campos deixado vazio não será alterado.")
        selectedIndex = int(selected) - 1
        selectedContact = contactList[selectedIndex]
        
        print(f"Nome: {selectedContact['nome']}")
        newName = input("Novo nome: ")
        
        print(f"Numero: {selectedContact['numero']}")
        newFoneNumber = input("Novo numero: ")

        print(f"Email: {selectedContact['email']}")
        newEmail = input("Novo email: ")

        newContact = {
            "nome" : newName if newName != "" else selectedContact["nome"],
            "numero" : newFoneNumber if newFoneNumber != "" else selectedContact["numero"],
            "email" : newEmail if newEmail != "" else selectedContact["email"],
            "favorito" : selectedContact["favorito"]
        }
        
        contactList[selectedIndex] = newContact
        print(f"Contato {selected} - {contactList[selectedIndex]['nome']} foi atualizado.")
    except:
        print()
        print("Erro contato não encontrado.")


