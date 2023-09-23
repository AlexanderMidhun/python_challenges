# Write Python code to open a file named Fileprogram.txt and write
# some random data into it.
file = open("Fileprogram.txt",'w')
file.write("Write Python code to open a file named Fileprogram.txt and write some random data into it. ")
print("_____________________________________________________________________________________________")

# Open the file, read the contents and display them as output.
file = open("Fileprogram.txt",'r')
content = file.read()
print(content)
print("_____________________________________________________________________________________________")

# Write python code to add additional text to the existing file on a new
# line without deleting the previous contents
file = open("Fileprogram.txt",'a')
file.write("\nAdding additional text to the existing file.")
file = open("Fileprogram.txt",'r')
added_content = file.read()
print(added_content)
file.close()

