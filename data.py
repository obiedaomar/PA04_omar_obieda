from contact import Contact
from contact_book import ContactBook

# create contact for Cookie Monster

cookie = Contact("Cookie", "Monster")
cookie.add_phone("12345678", "Work")
cookie.add_phone("00123456", "Cookie Line")
cookie.add_label("Cookie")
cookie.add_label("Friend")

# call update_name() on cookie
# cookie.update_name(lname="Monster Too")
# cookie.update_name(fname="Yummy Cookie")
# cookie.update_name(fname="Yummy Cookie", lname="Monster Too")
# print(cookie)

# create contact for Don Music

don = Contact("Don", "Music")

# call add lebal
don.add_label("Music")
don.add_label("Friend")

# call add phone numbers
don.add_phone("0788878888","IT")
print(don)
# create contact for Roosevelt Franklin
roosevelt = Contact("Roosevelt", "Franklin")
# call add email
roosevelt.add_email("nana1196@hotmail.com")
roosevelt.add_email("lolo895@hotmail.com")
# roosevelt.print_list_emails()

print(type(roosevelt))
# create a contact book
sesame_street = ContactBook()

# add contacts to contact book
sesame_street.add(cookie)
sesame_street.add(don)
sesame_street.add(roosevelt)
sesame_street.search_by_label("Music")
sesame_street.print_book()
#print(sesame_street.search_by_label("Music"))
# print the number of contacts in contact book
print(len(sesame_street.contacts))

# print all contacts
sesame_street.print_all_contacts()


# using decorator  
fullname=sesame_street.pretty_name
print(fullname(roosevelt))

# call save_info method 
sesame_street.save_file()

# call method read_file to read contact information and print total loaded contacts
sesame_street.read_data()
sesame_street.load_data()

# export file by user choose and print file info and error hundling if user enter invalid file
sesame_street.export_file()
# create object check if contatt include or not 
smesm=Contact("jeorge","khorye")
sesame_street.handling_error(smesm)
sesame_street.handling_error(don) 

# call method to add file from terminal
#sesame_street.add_contact_info(sesame_street)
sesame_street.save_file()
#sesame_street.add_contact_info()
sesame_street.save_file()

sesame_street.add(smesm)
smesm.add_email("sesime_street@pixcer.com")
smesm.add_phone("gamer","23456")
# call method to delete contact from terminal
sesame_street.del_contact_info()

# call method generate_report()
sesame_street.generate_report()

# delet_contact = input("should contact be delete")
# sesame_street.del_contact(cookie)

# # call delete_contact()
# sesame_street.delete_contact(roosevelt)
# sesame_street.delete_contact(roosevelt)

# with open('collection_data.csv','w',newline="") as f:
#     filewriter=csv.writer(f,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
#     filewriter.writerow(['Name','phone','Email'])
#     filewriter.writerow(['jeorge','0534958373427','jeorgeqrdahi@gmail.com'])
#     filewriter.writerow(['rawan','0455645645646','rawan.odeh@gmail.com'])
#     filewriter.writerow(['rama','054564645664','rama.alramhi@gmail.com'])
#     filewriter.writerow(['hamza','05453455664','hamza.almzar@gmail.com'])
    
#     f.close()
# os.startfile('account-statement.csv')
# with open('collection_data.csv', 'w') as csv_file:
#  csv_writer = csv.writer(csv_file, delimiter=',')
#  csv_writer.writerow(self.contacts)

# with open('collection_data.csv','r') as f:
#     filereader=csv.reader(f,dialect='excel')
    
    
#     for row in filereader:
#         print(row)
#     else:
#         print('Done')

# with open('collection_data.csv', "r") as f:
#  filereader = f.readlines()
 
# for line in filereader:
#     ff = filereader.split(",")
#     print (ff) 




