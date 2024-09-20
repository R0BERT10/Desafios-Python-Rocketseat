
def showContacts(contactList:list):
    print()
    print('Ind - Fav - Nome - Numero - Email')
    for index, contact in enumerate(contactList):
        fav = "*" if(contact["favorito"]) else " "
        print(f'{str(index+1).zfill(3)} - ({fav}) - {contact["nome"]} - {contact["numero"]} - {contact["email"]}')
    if len(contactList) == 0:
        print("     <vazio>")