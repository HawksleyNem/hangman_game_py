import os
from time import process_time_ns

attempt = 7
word_list = []
masked_word = []


word_list = input("Joueur 1 - Saisissez un mot : ")                # On demande au joueur de saisir un mot
os.system("cls")                                                  # On efface la console pour cacher le mot saisi par le joueur 1
word = list(word_list)

print(word)
# Affichage du nombre de lettres dans le mot
masked_word.append(len(word)*"_")
print(masked_word[0:])

letter = input("Joueur 2 - Saisissez une lettre : \n")  # Tours du joueur 2

while masked_word != word:
    for i in word[0:]:
        # Si la lettre est présente dans le mot
        if letter == word(i):
        # S'il manque encore des lettres
            masked_word.append(word(i))
            attempt -= 1
        # Si la lettre n'est pas présente dans le mot
        else:
            attempt -= 1
            # S'il ne reste aucune tentative au joueur 2
            if attempt == 0:
                print("C'est perdu...")
                masked_word = word
                print(f"Le mot était {word}.")
            # S'il lui reste une ou plusieurs tentatives
            else:
                print(f"Raté ! Il vous reste {attempt} tentatives.\n")

print("C'est gagné !")