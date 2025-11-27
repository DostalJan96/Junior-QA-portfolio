# Náhrada s kontrolou existence (QA princip)
# CÍL: Nahradit prvek jen v případě, že se v seznamu nachází.

def main():
    """
    Hlavní logika: Čte vstupy, a používá try-except k bezpečnému nalezení indexu 
    a provedení náhrady.
    """
    # 1. Definice Seznamu a Získání Vstupu
    muj_seznam_ovoce = ['jablko', 'hruška', 'banán', 'pomeranč', 'kiwi']
    print(f"Původní seznam ovoce: {muj_seznam_ovoce}")
    
    # Získání vstupu
    ovoce_k_odstraneni = input("Napište název ovoce, které chcete odstranit: ")
    ovoce_k_vlozeni = input("Napište ovoce, které chcete vložit do seznamu: ")

    # 2. Bezpečná Náhrada (TRY-EXCEPT blok)
    try:
        # 2a: Nalezení Indexu
        # Index() je vložena do try bloku, protože hrozí pád s ValueError.
        index_nahrazovaneho = muj_seznam_ovoce.index(ovoce_k_odstraneni)
        
        # 2b: Přímá Náhrada
        muj_seznam_ovoce[index_nahrazovaneho] = ovoce_k_vlozeni
        
        # 3. Výstup Úspěch
        print(f"Můj aktualizovaný seznam ovoce: {muj_seznam_ovoce}")
        
    except ValueError:
        # Scénář Chyby: Prvek k odstranění v seznamu neexistuje.
        print(f"CHYBA: Prvek '{ovoce_k_odstraneni}' se v seznamu nenachází. Náhrada neproběhla.")


if __name__ == "__main__":
    main()