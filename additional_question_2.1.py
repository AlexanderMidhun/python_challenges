# To create a new list from an existing list using string format

existing_list = ['One' , 'Two' , 'Three' , 'Four' , 'Five' , 'Six' , 'Seven']

#Slicing
print("Slicing:")
print(existing_list)
new_slicing_list = existing_list[1:4]
print(new_slicing_list)
print("______________________________________________________________________________")

#List comprehension
print("List comprehension:")
new_list = ['Twenty {}'.format(list_key) for list_key in existing_list]
print(new_list)