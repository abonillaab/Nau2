from Nau import Nau

def menu():
    print("w- Moure amunt")
    print("a- Moure equerre")
    print("d- Moure dreta")
    print("s- Moure avall")    
    print("0- Sortir")

def main():

    menu()
    
    nau = Nau(0,0)

    sortir=False
    while not sortir:
        
        nau.mostrar()
    
        op = input("Entra una opció: ")
        if op=='d':
            nau.moure_dreta()
	        pass
        elif op=='a':
            nau.moure_esquerre()
            pass
        elif op=='w':
            nau.moure_amunt()
            pass
        elif op=='s':
            nau.moure_avall()
            pass
        elif op=='0':
            sortir=True
            print("Has sortit de l'avió")
               
if __name__ == "__main__":
    main()

