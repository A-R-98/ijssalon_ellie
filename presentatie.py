from helper import onderstreep

def presenteer(d,totaal):
    for k,v in d.items():
       print(k,":",v)
    uitvoer=onderstreep("                          ")
    for el in uitvoer:
        print(el)
    print(f"Totaal : {totaal} euro" )

