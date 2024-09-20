from Module_2_show_contacts import showContacts

def deleteContact(contactList:list):
    showContacts(contactList)
    selected = input(f'Informe o "Ind" do contato que deseja deletar: ')
    try:
        print()
        selectedIndex = int(selected) - 1
        deleteContact = contactList.pop(selectedIndex)
        print(f"Contato {selected} - {deleteContact['nome']} deletado.")
    except:
        print()
        print("Erro contato não encontrado.")
    
    return contactList
        