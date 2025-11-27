# --- Definice funkcí ---

def pozdrav_a_ziskej_jmeno():
    """
    Tato funkce se na začátku zeptá na jméno a pozdraví.
    Vrací jméno uživatele pro další použití.
    """
    print('Vítej v experimentálním pekelném programu pro sběr DUŠÍ .')
    # Zeptáme se na jméno a uložíme ho do proměnné
    jmeno = input('Nejdříve mi prosím řekni, jak ti mám říkat: ')
    # Pozdravíme uživatele s použitím jeho jména
    print(f'Díky, {jmeno}! Teď k věci...')
    print('---------------------------------------------------')
    return jmeno

def hlavni_logika_souhlasu(jmeno_uzivatele):
    """
    Toto je hlavní smyčka programu. Bude se ptát tak dlouho, dokud nedostane správnou odpověď.
    """
    while True: # Toto je "nekonečná" smyčka, která se opakuje pořád dokola
        print('věnujete svou duši experimntálnímu pekelnému progamu?')
        print('Pokud souhlasíte, napište ¨souhlasim¨ a pak ENTER.')
        print('Pokud nesouhlasíte, napište "nesouhlasim" a stiskněte ENTER.')
        
        # Získáme vstup od uživatele
        volba = input('Tvoje volba: ')

        # Podmínka, která zkontroluje, co uživatel zadal
        if volba == 'souhlasim':
            # Pokud zadal ¨souhlasim¨, vypíše se toto a smyčka skončí
            print(f'Skvělé, {jmeno_uzivatele}! Děkujeme za souhlas. Tvoje duše je teď naše.')
            break # Toto je klíčový příkaz, který PŘERUŠÍ a ukončí smyčku while
        
        elif volba.lower() == 'nesouhlasim':
            # .lower() převede text na malá písmena, takže je jedno, jak to uživatel napíše
            # Pokud zadal "nesouhlasim", vypíše se toto a smyčka skončí
            print('To je škoda. Tvá duše je i tak naše, jen to bude chvilku trvat. Užívej si to peklo tady...')
            break # Ukončíme smyčku i při nesouhlasu
            
        else:
            # Pokud zadal cokoliv jiného, vypíše se toto a smyčka se bude opakovat od začátku
            print('Nerozumím tvé volbě. Prosím, zkus to znovu.')
            print('---------------------------------------------------')

def rozlouceni():
    """
    Tato funkce se postará o konec programu, aby se okno hned nezavřelo.
    """
    print('---------------------------------------------------')
    input('Program nyní skončí. Stiskni Enter pro zavření okna.')


# --- Hlavní spuštění programu ---

# Teď postupně zavoláme naše připravené funkce v tom správném pořadí
jmeno = pozdrav_a_ziskej_jmeno()
hlavni_logika_souhlasu(jmeno)
rozlouceni()