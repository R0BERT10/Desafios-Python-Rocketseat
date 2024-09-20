from Module_2_show_contacts import showContacts

def toggleFavContact(contactList:list):
    showContacts(contactList)
    selected = input(f'Informe o "Ind" do contato que deseja adicionar ou remover dos favoritos: ')
    try:
        print()
        selectedIndex = int(selected) - 1
        selectedContact = contactList[selectedIndex]
        atualFavState = selectedContact["favorito"]
        selectedContact["favorito"] = not atualFavState

        msgFav = "removido dos favoritos" if (atualFavState) else "adicionado aos favoritos"
        print(f"Contato {selected} - {selectedContact['nome']} {msgFav}.")
    except:
        print()
        print("Erro contato não encontrado.")