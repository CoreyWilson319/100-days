#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
PLACEHOLDER = "[name]"

with open('Input/Names/invited_names.txt') as names:
    names = names.readlines()

with open('Input/Letters/starting_letter.txt') as letter:
    letter = letter.read()
    for name in names:
        stripped_name = name.strip()
        with open(f'Output/ReadyToSend/letter_for_{name}', mode="w") as ready_to_send_letter:
            modified_letter = letter.replace(PLACEHOLDER, stripped_name)
            ready_to_send_letter.write(modified_letter)
