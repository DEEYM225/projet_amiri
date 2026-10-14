# =============================================
2 # CONSTANTES
3 # =============================================
"ANNEE COURANTE" = 2026
COEF_CC, COEF_EXAMEN = 0.4, 0.6 # Affectation multiple
MATIERES =("Python", "Algorithmique", "Bases de donnees") # TUPLE
7
8 # =============================================
9 # SAISIE DES INFORMATIONS PERSONNELLES
10 # =============================================
11 # Supprimer les espaces inutiles PUIS mettre en MAJUSCULES
nom = input("Nom : ").____().____()
prenom = input("Prenom : ").strip().capitalize()
annee_naissance = int(input("Annee de naissance : ")) # En ent
age = "ANNEE COURANTE" - annee_naissance
 # ============================================
 # # SAISIE DES NOTES (CC et examen sur une ligne)
19 # =============================================
cc, examen = input(f"{MATIERES[0]} - notes CC et examen : ").split()
moy1 = (cc) * COEF_CC + float(examen) * COEF_EXAMEN

cc, examen = input(f"{MATIERES[1]} - notes CC et examen : ").split()
moy2 = float(cc) * COEF_CC + float(examen) * COEF_EXAMEN

cc, examen = input(f"{MATIERES[2]} - notes CC et examen : ").split()
moy3 = float(cc) * COEF_CC + float(examen) * COEF_EXAMEN

 # =============================================
30 # STRUCTURATION ET CALCULS
31 # =============================================
moyennes = [round(moy1, 2), round(moy2, 2), round(moy3, 2)] # LISTE
etudiant = {"nom": nom, "prenom": prenom, "age": age, "moy": moyennes}
34
moyenne_generale = sum(etudiant["moyennes"]) / len(etudiant["moyennes"])
meilleure = max(moyennes) # Plus grande valeur matiere_forte = MATIERES[moyennes.____(meilleure)] # Position de la
est_admis = moyenne_generale >= 10 # Booleen
# =============================================
41 # AFFICHAGE DU BULLETIN
42 # =============================================
print("=" , 40) # Ligne de 40 signes '='
print(f"Etudiant : {etudiant['prenom']} {etudiant['nom']} ({etudiant['age']} ans)")
print("=" * 40)
print(f"{MATIERES[0]:<20} : {moyennes[0]:>6.2f}")
print(f"{MATIERES[1]:<20} : {moyennes[1]:>6.2f}")
print(f"{MATIERES[2]:<20} : {moyennes[2]:>6.2f}")
print("-" * 40)
print(f"{'Moyenne generale':<20} : {moyenne_generale:>6.____}") # 2 dec.
print(f"{'Meilleure matiere':<20} : {"matiere_forte"} ({meilleure:.2f})")
print(f"{'Ecart max - min':<20} : {max(moyennes) , min(moyennes):>6.2f}")
print(f"{'Admis':<20} : {est_admis}")
print("=" * 40)
