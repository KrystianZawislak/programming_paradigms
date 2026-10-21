contacts = {('Jan', 'Kowalski'):"123456789", 
            ('Adam', 'Nowak'):"987654321" ,
            ('Adam', 'Kowalski'): "600300900"}
            
print(contacts["Adam" ,"Nowak"])

for a in contacts:
    name, surname = a
    if surname == "Kowalski":
        print(contacts[a])
