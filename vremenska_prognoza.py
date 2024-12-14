

temperatura = int(input("Unesite temperaturu: "))
test_temperatura = -1
temperatura = test_temperatura
poruka = ""
if temperatura <0 :
    poruka = "Oprez klizavo!"
    
if temperatura >0 :
    poruka = "Temperatura je iznad 0"
    if temperatura >30:
        poruka = "Uključite klima uređaj"

ocekivana_poruka = "Oprez klizavo!"
if poruka ==ocekivana_poruka:
    print ("Case ispod 0 - Test prošao!")

