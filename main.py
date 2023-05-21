def taux_évolution():
    Vi = float( input("Veuillez rentrer la valeur initiale (de départ): "))
    Vf = float( input("Veuillez rentrer la valeur finale (fin): "))
    taux_évolution = float((Vf - Vi)/Vi)
    taux_évolution_pourcentage = taux_évolution *100
    if taux_évolution < 0:
        print("le taux diminue: "+ str(taux_évolution_pourcentage) + "%")
    else:
        print("Le taux augmente: "+ str(taux_évolution_pourcentage) + "%")
    print(taux_évolution)
taux_évolution()