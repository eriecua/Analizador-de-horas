def mostrar_menu():
    print("------------------------------------------")
    print("Option (1): Hours Converted")
    print("Option (2): Minutes Converted")
    print("Option (3): Exit")
    print("------------------------------------------")
while True:
    options = int(input("Chose your option: "))
    if options == 1:
        MINUTOS_POR_HORA = 60
        while True:
            horas = int(input("Type hours: "))
            minutos = int(input("Type minutes: "))
            if horas > 0 and minutos >= 0:
                break
            if horas <= 0:
                print("The hours must be greater than zero. Try again.")
            if minutos < 0:
                print("The minutes must be greater than zero. Try again.")
        total = horas * MINUTOS_POR_HORA + minutos
        print(f"The total minutes is: {total} minutes")
    elif options == 2:
        minutes = 0
        count = 0
        while True:
            number = int(input("Type minutes: "))
            if number == 0:
                break            
            count += 1
            minutes += number
            if number == 0:
                break
        inter, decimal  = divmod((minutes/60), 1)
        print("------------------------------------------")
        print(f"Total Time: {int(inter)} hours and {int(round((decimal * 60)))} minutes.")
        print("------------------------------------------")
        print(f"You type {count} numbers")
    elif options == 3:
        print("Thanks for use, bye")
        break
    else:
        print("Invalid option. Please, try again")



