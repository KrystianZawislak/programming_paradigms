contacts = {('Jan', 'Kowalski'):"123456789", 
            ('Adam', 'Nowak'):"987654321" ,
            ('Adam', 'Kowalski'): "600300900"}
            
print(contacts["Adam" ,"Nowak"])

for name, surname in contacts:
    if surname == "Kowalski":
        print(contacts[name, surname])
