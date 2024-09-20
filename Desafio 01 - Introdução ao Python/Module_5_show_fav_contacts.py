from Module_2_show_contacts import showContacts

def showFavContacts(contactList:list):
    favContacts = [ contact for contact in contactList if contact["favorito"] ]
    print("Contatos favoritos")
    showContacts(favContacts)