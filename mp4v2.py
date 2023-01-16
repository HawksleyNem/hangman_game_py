import os

attempt = 7
word_list = []
masked_word = []
n = 0

# On demande au joueur de saisir un mot
word_list = input("Joueur 1 - Saisissez un mot : ")
# Conversion de la liste en plusieurs caractères
word = list(word_list)
# On efface la console pour cacher le mot saisi par le joueur 1
os.system("cls")
# Affichage du nombre de lettres dans le mot
for i in word[0:len(word)]:
    masked_word.append("_")
print(f"{masked_word[0:]}\n")

# Tours du joueur 2
while masked_word != word or attempt != 0:
    letter = input("Joueur 2 - Saisissez une lettre : ")
    for i in word[0:]:
        if letter == (i):
            masked_word.pop(n)
            masked_word.insert(n,word(i))
            n += 1
            attempt -= 1
            print(f"{masked_word}\n")
    attempt -= 1