import sys
import time
import multiprocessing
import os

def cpu_bomb():
    """
    CPU bomba: V nekonečné smyčce počítá Fibonacciho číslo,
    aby vytížila jedno jádro CPU na 100 %.
    """
    print(f"CPU bomba spuštěna na procesu (PID: {os.getpid()})...")
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    
    while True:
        # Hodnota kolem 35-40 je dostatečně vysoká, aby výpočet trval
        # a efektivně vytížil CPU.
        fibonacci(38)

def memory_bomb():
    """
    Paměťová bomba: Záměrně a postupně zaplňuje operační paměť (RAM)
    a monitoruje její spotřebu, dokud nedojde k chybě.
    """
    
    # Definice velkého bloku dat (např. 10 MB), který budeme opakovaně přidávat.
    OBŘÍ_BLOK_DAT = 'x' * (10 * 1024 * 1024)
    
    # Seznam, kam budeme přidávat bloky dat. Tato data se NIKDY neuvolní.
    seznam_smrti = []
    i = 0
    
    print(f"Paměťová bomba spuštěna na procesu (PID: {os.getpid()})...")
    
    # Nekonečná smyčka - zaručuje, že alokace poběží nonstop.
    while True:
        try:
            # 1. Alokace
            # Přidáváme obří blok do seznamu. RAM stoupá!
            seznam_smrti.append(OBŘÍ_BLOK_DAT)
            i += 1
            
            # 2. Monitorování
            # Vypisujeme aktuální spotřebu RAM pro monitorování.
            # getsizeof() vrací velikost v Bytesech. Dělíme pro převod na MB.
            spotreba_MB = sys.getsizeof(seznam_smrti) / (1024 * 1024)
            
            print(f"Iterace {i}: {spotreba_MB:.2f} MB RAM spotřebováno.")
            
            # Pauza jen pro to, abychom viděli log, ale je tak krátká, že to RAM nešetří.
            time.sleep(0.001)
            
            # KRITICKÝ BOD (Analytická záchranná brzda - jen pro monitorování)
            # Pokud se dostaneš přes 2 GB, jsi v zóně vysokého rizika.
            if spotreba_MB > 2048:
                print("!!! WARNING: PŘEKROČENA ZÓNA 2 GB RAM. Zastav, nebo to bude bolet!!!")

        except MemoryError:
            # Tohle se stane, až Python vyčerpá paměť pro sebe.
            print("\nKritická chyba: Python už nemůže alokovat více paměti!")
            break
        except KeyboardInterrupt:
            # Umožňuje čisté ukončení uživatelem.
            print("\nProgram byl ukončen uživatelem.")
            break
        except Exception as e:
            # Jiné chyby (např. systém už dál nedovolí)
            print(f"\nNeočekávaná chyba: {e}")
            break

# Spuštění hlavní destrukce
if __name__ == "__main__":
    print("--- Spouštím kombinovaný útok na CPU a RAM ---")
    print("--- Pro ukončení stiskněte CTRL+C (může chvíli trvat) ---")

    # Zjistíme počet jader CPU, abychom mohli vytížit všechna.
    # os.cpu_count() může vrátit None, proto ošetření.
    pocet_jader = os.cpu_count() or 1 
    print(f"Detekováno {pocet_jader} jader CPU. Pro každé bude spuštěn proces.")

    procesy = []

    # Spustíme paměťovou bombu v samostatném procesu
    memory_process = multiprocessing.Process(target=memory_bomb)
    procesy.append(memory_process)
    memory_process.start()

    # Spustíme CPU bombu pro každé jádro
    for _ in range(pocet_jader):
        cpu_process = multiprocessing.Process(target=cpu_bomb)
        procesy.append(cpu_process)
        cpu_process.start()

    # Čekáme, dokud všechny procesy neskončí (což se stane jen při chybě nebo CTRL+C)
    for p in procesy:
        p.join()