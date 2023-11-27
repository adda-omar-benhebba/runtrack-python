def my_long_word(taille_min, phrase):
    mots = []
    mot = ''
    for char in phrase:
        if char != ' ':
            mot += char
        else:
            if len(mot) > taille_min:
                mots.append(mot)
            mot = ''
    if len(mot) > taille_min:
        mots.append(mot)
    return ' '.join(mots)

resultat = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")
print("Output:", resultat)
