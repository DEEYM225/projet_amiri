COEFS = (0.4, 0.6)
SEUIL_ADMISSION = 10

etudiants = {
 1001: {"nom": "Ben Ali", "prenom": "Ahmed", "cc": 14, "examen": 16.0, "clubs": ("Robotique", "Theatre")},
 1002: {"nom": "Trabelsi", "prenom": "Sarra", "cc": 18.0, "examen": 17.0, "clubs": ("Robotique", "IA")},
 1003: {"nom": "Gharbi", "prenom": "Mohamed", "cc": 8.0, "examen": 9.5, "clubs": ("Football",)},
 1004: {"nom": "Jebali", "prenom": "Nour", "cc": 12.5, "examen": 13.0, "clubs": ("IA", "Theatre")},
}

# A) Ajout d'un etudiant par saisie - VERSION OFFICIELLE PDF
mat = int(input("Matricule : "))
nom_saisi = input("Nom : ").strip().title()
prenom_saisi = input("Prenom : ").strip().title()
notes = input("Notes CC Examen : ").split()
cc_saisi = float(notes[0])
ex_saisi = float(notes[1])
clubs_saisis = set(input("Clubs (separes par ,) : ").split(","))

etudiants[mat] = {"nom": nom_saisi, "prenom": prenom_saisi, "cc": cc_saisi, "examen": ex_saisi, "clubs": tuple(clubs_saisis)}

# B) Moyennes
coef_cc, coef_examen = COEFS
etudiants[1001]["moyenne"] = round(etudiants[1001]["cc"]*coef_cc + etudiants[1001]["examen"]*coef_examen, 2)
etudiants[1002]["moyenne"] = round(etudiants[1002]["cc"]*coef_cc + etudiants[1002]["examen"]*coef_examen, 2)
etudiants[1003]["moyenne"] = round(etudiants[1003]["cc"]*coef_cc + etudiants[1003]["examen"]*coef_examen, 2)
etudiants[1004]["moyenne"] = round(etudiants[1004]["cc"]*coef_cc + etudiants[1004]["examen"]*coef_examen, 2)
etudiants[mat]["moyenne"] = round(etudiants[mat]["cc"]*coef_cc + etudiants[mat]["examen"]*coef_examen, 2)

# C) Affichage
print(f"Total : {len(etudiants)} etudiants")

# D) Stats
moyennes = [etudiants[1001]["moyenne"], etudiants[1002]["moyenne"], etudiants[1003]["moyenne"], etudiants[1004]["moyenne"], etudiants[mat]["moyenne"]]
print(f"Moy promo : {sum(moyennes)/len(moyennes):.2f}")
print(f"Meilleure : {max(moyennes)}")
print(f"Triees : {sorted(moyennes, reverse=True)}")
print(f"Mediane : {sorted(moyennes, reverse=True)[len(moyennes)//2]}")

# E) Clubs
tous = set(etudiants[1001]["clubs"]) | set(etudiants[1002]["clubs"]) | set(etudiants[1003]["clubs"]) | set(etudiants[1004]["clubs"]) | set(etudiants[mat]["clubs"])
commun = set(etudiants[1001]["clubs"]) & set(etudiants[1004]["clubs"])
print(f"Clubs : {sorted(tous)}")
print(f"Communs Ahmed/Nour : {sorted(commun)}")
print(f"Sarra IA : {'IA' in etudiants[1002]['clubs']}")

# F) Mises a jour
etudiants[1003]["moyenne"] = round(11.0*0.4 + 12.0*0.6, 2)
sup = etudiants.pop(1004)
print(f"Supprime : {sup['prenom']} {sup['nom']}")
print(f"Restants : {sorted(etudiants.keys())}")

# G) CSV
print(", ".join([str(1002), etudiants[1002]["nom"], etudiants[1002]["prenom"], str(etudiants[1002]["moyenne"])]))