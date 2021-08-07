import os
import time

print("""
██╗░░██╗███████╗██╗░░██╗██╗░░░██╗███████╗  ░█████╗░██████╗░██╗░░░██╗███████╗███╗░░██╗████████╗██╗░░░██╗██████╗░███████╗
██║░░██║██╔════╝╚██╗██╔╝╚██╗░██╔╝██╔════╝  ██╔══██╗██╔══██╗██║░░░██║██╔════╝████╗░██║╚══██╔══╝██║░░░██║██╔══██╗██╔════╝
███████║█████╗░░░╚███╔╝░░╚████╔╝░█████╗░░  ███████║██║░░██║╚██╗░██╔╝█████╗░░██╔██╗██║░░░██║░░░██║░░░██║██████╔╝█████╗░░
██╔══██║██╔══╝░░░██╔██╗░░░╚██╔╝░░██╔══╝░░  ██╔══██║██║░░██║░╚████╔╝░██╔══╝░░██║╚████║░░░██║░░░██║░░░██║██╔══██╗██╔══╝░░
██║░░██║███████╗██╔╝╚██╗░░░██║░░░███████╗  ██║░░██║██████╔╝░░╚██╔╝░░███████╗██║░╚███║░░░██║░░░╚██████╔╝██║░░██║███████╗
╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝  ╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚══════╝

░██████╗░░█████╗░███╗░░░███╗███████╗
██╔════╝░██╔══██╗████╗░████║██╔════╝
██║░░██╗░███████║██╔████╔██║█████╗░░
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝""")
a = input("SCEGLI DOVE ANDARE SINISTRA: S DESTRA: D\n")
if a == "S":
    asa = input("Prosegui verso NORD: N SUD: S\n")
    if asa == "N":
        print("Sei stato colpito da un'ondata di freddo e ti sei congelato")
        os.system("python3 main.py")
        exit()
    elif asa == "S":
        asas = input("Hai incontrato un precipizio e devi aggirarlo, dove vai? SINISTRA: S DESTRA: D\n")
        if asas == "S":
            print("Sei finito su un'autostrada e sei stato investito da un'auto")
            os.system("python3 main.py")
            exit()
        elif asas == "D":
            asasd = input("Ti trovi in una foresta e e vedi una casa, ENTRA: E VATTENE: V\n")
            if asasd == "E":
                print("Nella casa ci vive una strega che ti lancia un incantesimo e vieni paralizzato")
                os.system("python3 main.py")
                exit()
            elif asasd == "V":
                asasdv = input("Ti ritrovi di fronte ad un fiume, cosa fa? NUOTI: N AGGIRI: A\n")
                if asasdv == "A":
                    print("Mentre te ne vai un lupo ti trova e ti mangia.")
                elif asasdv == "N":
                    asasdvn = input("Sei proprio lì, c'è il portale per tornare alla realtà però ci sono due guardie, a quale parli? DESTRA: D SINISTRA: S\n")
                    if asasdvn == "D":
                        print("Hai parlato con la guardia cattiva, provi a spiegargli perchè vuoi entrare nel portale ma la guardia non ti fa passare.")
                        os.system("python3 main.py")
                        exit()
                    elif asasdvn == "S":
                        print("Hai parlato con la guardia buona, ti ha fatto passare e sei finalmente tornato alla realtà!")
                        print("Grazie per aver giocato")
                        exit()
elif a == "D":
    ada = input("Incontri una montagna SCALALA: S AGGIRALA: A\n")
    if ada == "A":
        print("Aggiri la montagna, ma incontri un vicolo cieco.")
        os.system("python3 main.py")
        exit()
    elif ada == "S":
        adas = input("Scali la montagna ed incontri uno gnomo armato di ascia, CALCIALO: C SCAPPA: S\n")
        if adas == "C":
            print("Lo gnomo schiva il tuo calcio e ti decapita con l'ascia")
            os.system("python3 main.py")
            exit()
        elif adas == "S":
            adass = input("Sei riuscito a fuggire, hai un castello di fronte e sei molto assetato, ENTRA: E AGGIRALO: A\n")
            if adass == "E":
                adasse = input("Entri, riesci ad ottenere un bicchiedere d'acqua da parte di un principe, una volta uscito vai avanti ed incontri una roccia che ti blocca il passaggio, SPOSTALA: S AGGIRALA: A\n")
                if adasse == "S":
                    print("Stai spostando la roccia.")
                    time.sleep(1)
                    print("Stai spostando la roccia..")
                    time.sleep(1)
                    print("Stai spostando la roccia...")
                    time.sleep(1)
                    print("Ancora un ultimo sforzo...")
                    time.sleep(1)
                    print("Hai spostato la roccia! Inoltre hai raccolto una spada che si trovava sotto la roccia")
                    adasses = input("Scegli dove andare EST: E OVEST: O\n")
                    if adasses == "E":
                        print("Incontri un orco affamato che ti mangia")
                        os.system("python3 main.py")
                        exit()
                    elif adasses == "O":
                        adasseso = input("Incontri una tigre, la trafiggi con la tua spada e sei proprio lì, hai di fronte il portale che ti riporterà alla realtà, ma ci sono due guardie davanti, a quale parli? SINISTA: S DESTRA: D\n")
                        if adasseso == "S":
                            print("Hai parlato con la guardia buona, la guardia accetta e ti fa finalmente tornare nella realtà.\n\n")
                            print("Grazie per aver giocato!")
                        elif adasseso == "D":
                            print("Hai parlato con la guardia cattiva, provi a spiegargli perchè vuoi andare nel portale ma la guardia rifiuta.")
                            os.system("python3 main.py")
                            exit()
                elif adasse == "A":
                    print("Aggiri la roccia passando all'interno di un cespuglio, incontri un serpente velenoso che ti morde.")
                    os.system("python3 main.py")
                    exit()
            elif adass == "A":
                print("Sei riuscito ad aggirare il castello, però la strada era molto lunga e una volta arrivato sei morto di fame.")
                os.system("python3 main.py")
                exit()
elif a != "S" and a != "D":
    print("La direzione scelta non è valida")
