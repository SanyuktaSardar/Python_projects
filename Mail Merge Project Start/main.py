#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
from importlib.resources import contents

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
contents = ""
with open("./Input/Letters/starting_letter.txt") as letter:
    contents = letter.read()
    print(contents)

names_list = []

with open("./Input/Names/invited_names.txt","r") as names:
    names = names.read()
    for name in names.splitlines():
        names_list.append(name)

for name in names_list:
    if '[name]' in contents:
        letter_writing = contents.replace("[name]",f"{name}")
        with open(f'./Output/ReadyToSend/{name}.txt','w') as file:
            file.write(letter_writing)
