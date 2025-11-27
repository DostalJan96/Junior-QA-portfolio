# Cyklus WHILE, Hledání v Listu, Break/Continue
# CÍL: Opakovaně hledat jméno v seznamu, dokud uživatel nezadá 'k' (konec).

"""
Hlavní logika: Definuje seznam a pomocí cyklu WHILE a operátoru 'in' hledá prvek.
"""
    
    # 1. Definice Seznamu Zaměstnanců (Testovací Data)
muj_seznam_zamestnancu = ['Karel', 'David', 'Petr', 'Standa']
    
print(f"Můj seznam zaměstnanců: {muj_seznam_zamestnancu}")
    
    # 2. WHILE Cyklus pro Opakované Dotazování (Řídící proměnná)
pokracovat = "p" # Počáteční stav: 'p' (pokračovat)
    
while pokracovat == "p":
        
        # 2a. Získání Vstupu (Jméno, které chceme najít)
        hledane_jmeno = input("\nNapište jméno zaměstnance, kterého hledáte: ")
        
        # 2b. Logika Hledání a Zjištění Indexu
        # OPERÁTOR 'IN': První kontrola - je prvek v seznamu?
        if hledane_jmeno in muj_seznam_zamestnancu:
            
            # Index: Použijeme metodu .index() pro zjištění přesné pozice.
            index = muj_seznam_zamestnancu.index(hledane_jmeno)
            
            # VÝSTUP 1: Nalezeno
            print(f"Zaměstnanec {hledane_jmeno} je v seznamu zaměstnanců na indexu {index}.")
            
        else:
            
            # VÝSTUP 2: Nenalezeno
            print(f"Zaměstnanec {hledane_jmeno} není v seznamu zaměstnanců")
            
            # 2c. Logika Pokračování
            # Dotaz na ukončení cyklu
            ukonceni = input("Pokud chcete pokračovat, napište 'p', pro konec programu napište 'k': ").lower()
            
            # Nastavíme řídící proměnnou podle vstupu
            if ukonceni == "k":
                pokracovat = "k" # To ukončí cyklus WHILE

    
    # 3. Ukončení (Cyklus skončil)
print("Program byl ukončen.")


