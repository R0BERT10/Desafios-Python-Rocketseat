
def addNewContact(contactList:list):
    name = input("Nome: ")
    foneNumber = input("Numero do telefone: ")
    email = input("Email: ")

    newContact = {
        "nome" : name,
        "numero" : foneNumber,
        "email" : email,
        "favorito" : False
    }

    contactList.append(newContact)
    return contactList