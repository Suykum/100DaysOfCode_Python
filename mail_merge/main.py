
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()


with open("./Input/Letters/starting_letter.txt") as start_letter:
    s_letter = start_letter.read()

for n in range(0, len(names)):
    name = names[n].strip(".\n")
    with open(f"./Output/ReadyToSend/For_{name}.txt", "w") as letter:
        letter_with_name = s_letter.replace("[name]", name)
        letter.write(letter_with_name)


