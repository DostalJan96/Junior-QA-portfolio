# Práce s Množinami (set) a Slovníkem (dict)
# CÍL: Demonstrovat deklaraci množin a jejich uložení do slovníku.

# 1. Deklarace Množin (Set)
# Množiny jsou neuspořádané, bez duplicit. Jsou ideální pro rychlou kontrolu existence.
mnozina_cisel = {1, 3, 5, 7, 9}
mnozina_retezcu = {'a', 'd', 'b', 'e', 'c'}

# 2. Vytvoření Slovníku
# Slovník: Ukládáme data v párech klíč:hodnota, kde hodnotou může být i jiná struktura (Množina).
slovnik_mnozin = {
    'typ objektu': 'množina',
    # Ukládáme reference na naše množiny
    'objekt 1': mnozina_cisel, 
    'objekt 2': mnozina_retezcu
}

# 3. Výstup
print("-" * 30)
print(f"Množina čísel: {mnozina_cisel}")
print(f"Množina řetězců: {mnozina_retezcu}")
print("-" * 30)
print(f"Slovník: {slovnik_mnozin}")