from Phonebook import *

   
pb = []  
pb.append(Phonebook("Иванов Петр Степанович", "88005553535", "Москва"))
pb.append(Phonebook("Медведев Степан Петрович", "0987342321", "Петербург"))
pb.append(Phonebook("Тимофеев Валерий Александрович", "89574547888", "Н.Новгород"))
        
        
    
def show_addressbook():
    for i in pb:
        print (i.get_name(), i.get_phone(), i.get_city())

    
    
        