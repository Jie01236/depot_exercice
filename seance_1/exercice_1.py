data = {
    "annee_naissance": "1966",
    "nom": "Dupont",
    "prenom": "Jean"
}

class Personne:
    def __init__(self, data):
        self.data = data
        self.prenom = data['prenom']
        self.nom = data['nom']
        self.annee_naissance = data['annee_naissance']

    def etat_civil(self):
        return f"{self.prenom} {self.nom}"
    
    def age(self):
        current_year = 2023
        return current_year - int(self.annee_naissance)

personne = Personne(data)

print("Case 1: Personne(data).data")
print(personne.data)

print("\nCase 2: Personne(data).etat_civil()")
print(personne.etat_civil())

print("\nCase 3: Personne(data).age()")
print(personne.age())