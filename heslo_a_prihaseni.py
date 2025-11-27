# WHILE True, BREAK a Slovník
# CÍL: Opakovaně žádat o přihlášení, dokud není správné, nebo dokud uživatel nezadá 'konec'.

# 1. Definice Konstant (Správné přihlašovací údaje ve SLOVNÍKU)
# Používáme slovník, protože to je robustnější než dvě samostatné proměnné.
PRAVIDLA = {
    "uzivatelske_jmeno": "uzivatel",
    "heslo": "heslo123"
}
# WHILE TRUE: Cyklus běží, dokud není splněna jedna z ukončovacích podmínek (konec nebo správné heslo).
while True:
    
    # 2. Získání Uživatelského Jména a Kontrola Ukončení
    jmeno = input("Zadejte uživatelské jméno nebo 'konec' pro ukončení programu: ").lower()

    # LOGIKA UKONČENÍ: Uživatel zadal "konec"
    if jmeno == "konec":
        print("Program byl ukončen!")
        break # Okamžité opuštění cyklu a ukončení programu
        
    # 3. Získání Hesla
    heslo = input("Zadejte heslo: ")

    # 4. Logika Ověření (Analytická kontrola)
    # Zkontrolujeme, zda zadané jméno a heslo odpovídají hodnotám ve SLOVNÍKU.
    if jmeno == PRAVIDLA["uzivatelske_jmeno"] and heslo == PRAVIDLA["heslo"]:
        
        # Scénář 1: Přihlášení ÚSPĚŠNÉ
        print("Vítejte, přihlášení proběhlo úspěšně.")
        break # Okamžité opuštění cyklu po úspěchu
        
    else:
        # Scénář 2: Přihlášení NEÚSPĚŠNÉ
        print("Špatně zadané přihlašovací jméno nebo heslo!")
        
        # Cyklus se automaticky opakuje od začátku