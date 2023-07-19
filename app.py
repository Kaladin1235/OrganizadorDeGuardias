import main
# some info

# it has a chance of 0.0255010965471515% of printing random things like zeros (on months with 30 or 31 days) on the output calendar. In case that happens, run the program again. Oh, and the chances increase if you eliminate a lot of days for surgeons.
# if you run the program with unrealistic data (like saying the month has 60 days, or putting an 8 on the initial day)the program throw an error, ignore you or add random movie characters to the surgeon list


def menu():
    print("¿Qué quieres hacer?")
    print("1: Añadir días que no puede hacer algún cirujano\n2: Añadir guardias que tiene que hacer un cirujano\n3: Añadir locas que tiene que hacer un cirujano\n4: Añadir semilla (se imprimen en consola cada vez que se organiza el mes)\n5: Organizar el mes")
    num = int(input())
    
    if num == 1:
        print("¿Quién se va a coger días libres?")

        print("1: Álvaro \n2: Israel\n3: Covadonga\n4: Elena\n5: Stefan\n6: Pipe\n7: Leticia\n8: Andrés\n9: Teresa")
        lnum = int(input())

        print("¿Qué días te vas a poner libres? (debes separados por espacios. Por ejemplo: 7 8 23)")
        linput = input().split(" ")
        ldays = []
        for i in range(len(linput)):
            ldays.append(int(linput[i]))

        if lnum == 1:
            main.surgeons[0].eliminateDays(ldays)

        if lnum == 2:
            main.surgeons[1].eliminateDays(ldays)
        if lnum == 3:
            main.surgeons[2].eliminateDays(ldays)
        if lnum == 4:
            main.surgeons[3].eliminateDays(ldays)
        if lnum == 5:
            main.surgeons[4].eliminateDays(ldays)
        if lnum == 6:
            main.surgeons[5].eliminateDays(ldays)
        if lnum == 7:
            main.surgeons[6].eliminateDays(ldays)
        if lnum == 8:
            main.surgeons[7].eliminateDays(ldays)
        if lnum == 9:
            main.surgeons[8].eliminateDays(ldays)
        print("\n\n")
        menu()

    if num == 2:
        print("¿Quién va a ser obligado a hacer días?")

        print("1: Álvaro \n2: Israel\n3: Covadonga\n4: Elena\n5: Stefan\n6: Pipe\n7: Leticia\n8: Andrés\n9: Teresa")
        lnum = int(input())

        print("¿Qué días te vas a poner de guardia? (debes separados por espacios. Por ejemplo: 5 30 22)")
        linput = input().split(" ")

        ldays = []
        for i in range(len(linput)):
            ldays.append(int(linput[i]))

        if lnum == 1:
            main.surgeons[0].setDays(ldays, main.surgeons, main.calendar)
        if lnum == 2:
            main.surgeons[1].setDays(ldays, main.surgeons, main.calendar)
        if lnum == 3:
            main.surgeons[2].setDays(ldays, main.surgeons, main.calendar)
        if lnum == 4:
            main.surgeons[3].setDays(ldays, main.surgeons, main.calendar)
        if lnum == 5:
            main.surgeons[4].setDays(ldays, main.surgeons, main.calendar)
        if lnum == 6:
            main.surgeons[5].setDays(ldays, main.surgeons, main.calendar)
        if lnum == 7:
            main.surgeons[6].setDays(ldays, main.surgeons, main.calendar)
        if lnum == 8:
            main.surgeons[7].setDays(ldays, main.surgeons, main.calendar)
        if lnum == 9:
            main.surgeons[8].setDays(ldays, main.surgeons, main.calendar)
        print("\n\n")
        menu()

    if num == 3:
        print("¿Quién va a ser obligado a hacer días?")

        print("1: Álvaro \n2: Israel\n3: Covadonga\n4: Elena\n5: Stefan\n6: Pipe\n7: Leticia\n8: Andrés\n9: Teresa")
        lnum = int(input())

        print("¿Qué días te vas a poner de guardia? (debes separados por espacios. Por ejemplo: 5 30 22)")
        linput = input().split(" ")

        ldays = []
        for i in range(len(linput)):
            ldays.append(int(linput[i]))

        if lnum == 1:
            main.surgeons[0].LocSetDays(ldays, main.surgeons, main.calendar)
        if lnum == 2:
            main.surgeons[1].LocSetDays(ldays, main.surgeons, main.calendar)
        if lnum == 3:
            main.surgeons[2].LocSetDays(ldays, main.surgeons, main.calendar)
        if lnum == 4:
            main.surgeons[3].LocSetDays(ldays, main.surgeons, main.calendar)
        if lnum == 5:
            main.surgeons[4].LocSetDays(ldays, main.surgeons, main.calendar)
        if lnum == 6:
            main.surgeons[5].LocSetDays(ldays, main.surgeons, main.calendar)
        if lnum == 7:
            main.surgeons[6].LocSetDays(ldays, main.surgeons, main.calendar)
        if lnum == 8:
            main.surgeons[7].LocSetDays(ldays, main.surgeons, main.calendar)
        if lnum == 9:
            main.surgeons[8].LocSetDays(ldays, main.surgeons, main.calendar)
        print("\n\n")
        menu()

    if num == 4:
        seed = input("Pega la semilla: ").split(" ")
        main.addSeed(seed)
        menu()

    if num == 5:
        main.order()

    if num < 1 or num > 5:
        print("Yo quiero marcha marcha")
        print("Yo quiero marcha marcha")
        print("Tú quieres...")
        print("MARCHA!")
        print()
        print("""     / \__
    (    @\___
    /         O
   /   (_____/
  /_____/   U""")
        julien = main.Surgeon("King Julien XIII", main.md, main.id)
        kowalski = main.Surgeon("Kowalski", main.md, main.id)
        skipper = main.Surgeon("Skipper", main.md, main.id)
        Rico = main.Surgeon("Rico", main.md, main.id)
        Privet = main.Surgeon("Privet", main.md, main.id)
        main.surgeons.append(julien)
        main.surgeons.append(kowalski)
        main.surgeons.append(skipper)
        main.surgeons.append(Rico)
        main.surgeons.append(Privet)
        menu()

menu()