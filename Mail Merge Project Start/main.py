#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
def make_letter(recipient_name, example_path,output_path):
    with open(example_path,"r") as example_file:
        content = example_file.read()
        new_content = content.replace("[name]",recipient_name)
    with open(output_path,"w") as final_letter:
        final_letter.write(new_content)

names = open("Input/Names/invited_names.txt","r")
temp = names.readlines()
list_names = []
for name in temp:
    list_names.append(name.strip())
for name in list_names:
    rec_name = f"{name}"
    ex_path = "Input/Letters/starting_letter.txt"
    out_path = f"Output/ReadyToSend/letter_for_{name}"
    make_letter(rec_name,ex_path,out_path)