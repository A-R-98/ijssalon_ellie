from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    uitvoer=f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs-(prijs*korting)} euro."
    return uitvoer
print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten, btw):
    uitvoer=f"Het totaal van alle inkomsten van deze week is {sum(inkomsten)} euro, waarover {(sum(inkomsten))*btw} euro btw betaald dient te worden."
    return uitvoer
print (inkomsten_totaal([220,430,125,160,205,90,345], 0.09))

def hoog_en_laag(mijn_lijst):
    uitvoer= [max(mijn_lijst), min(mijn_lijst)]
    return uitvoer
print (hoog_en_laag([220,430,125,160,205,90,345]))

def gemiddelde(mijn_lijst):
    uitvoer= f"De gemiddelde inkomsten deze week zijn {(sum(mijn_lijst))/(len(mijn_lijst))} euro."
    return uitvoer
print (gemiddelde([220,430,125,160,205,90,345]))

def meervoudig(invoer_lijst):
    uitvoer=(hoog_en_laag(invoer_lijst))
    return uitvoer
print (meervoudig([10,5,3,2,1,2,9]))

def combinatie(invoer_lijst_2):
    korte_lijst = hoog_en_laag(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
print (combinatie([220,430,125,160,205,90,345]))
