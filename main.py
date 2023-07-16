import classifier
from functools import reduce

class Calendar():
    def __init__(self, daysInMonth, initialDay, skipDay):
        numFullWeeks = (daysInMonth - daysInMonth % 7)/7
        calendar = []
        if initialDay == 0:
            for i in range(int(numFullWeeks)):
                calendar.append([0,0,0,0,0,0,0])
            lst = []
            for i in range(daysInMonth%7):
                lst.append(0)
            calendar.append(lst)
        else:
            count = []
            for i in range(7-initialDay):
                count.append(0)
            calendar.append(count)

            for i in range(int((daysInMonth-7+initialDay)/7)):
                calendar.append([0,0,0,0,0,0,0])

            lst = []
            for i in range(daysInMonth-((len(calendar)-1)*7)-7+initialDay):
                lst.append(0)
            
            calendar.append(lst)
            if initialDay == 4:
                calendar.pop(-1)

        skipCount = 0
        for i in range(len(calendar)-1):
            if len(calendar[i]) != 7:
                skipCount = 7 - len(calendar[i])
                for a in range(7):
                    calendar[i].insert(0, "--")
                    if len(calendar[i]) == 7:
                        break
        self.initSkip = skipCount
        self.calendar = calendar

        for a in range(len(calendar)):
            for b in range(len(calendar[a])):
                if calendar[a][b] == -1:
                    calendar[a][b] = 0
        sd = 0
        if skipDay == -2:
            sd = False
        else:
            sd = skipDay

        if sd:
            for i in range(len(self.calendar)):
                if i == 0:
                    if skipDay > self.initSkip:
                        self.calendar[0][skipDay]
                elif len(self.calendar[i]) > skipDay:
                    self.calendar[i][skipDay] = -1

class Surgeon:
    def __init__(self, name, mday, iday, skipDay):
        self.name = name
        self.calManager = Calendar(mday, iday, skipDay)

        self.num0 = 0
        self.num1 = 0
        self.num2 = 0
        self.num3 = 0
        self.num4 = 0
        self.num5 = 0
        self.num6 = 0

        self.locCalManager = Calendar(mday, iday, False)
        self.lnum0 = 0
        self.lnum1 = 0
        self.lnum2 = 0
        self.lnum3 = 0
        self.lnum4 = 0
        self.lnum5 = 0
        self.lnum6 = 0
    
    def eliminateDays(self, days=[]):
        lens = []
        for i in self.calManager.calendar:
            lens.append(len(i))

        

        for i in days:
            if i + self.calManager.initSkip > lens[4] + lens[3] + lens[2] + lens[1] + lens[0]:
                self.calManager.calendar[5][i-lens[0]-lens[1]-lens[2]-lens[3]-lens[4]-1 + self.calManager.initSkip] = -1
                self.locCalManager.calendar[5][i-lens[0]-lens[1]-lens[2]-lens[3]-lens[4]-1 + self.calManager.initSkip] = -1
            elif i + self.calManager.initSkip > lens[3] + lens[2] + lens[1] + lens[0]:
                self.calManager.calendar[4][i-lens[0]-lens[1]-lens[2]-lens[3]-1 + self.calManager.initSkip] = -1
                self.locCalManager.calendar[4][i-lens[0]-lens[1]-lens[2]-lens[3]-1 + self.calManager.initSkip] = -1
            elif i + self.calManager.initSkip > lens[2] + lens[1] + lens[0]: 
                self.calManager.calendar[3][i-lens[0]-lens[1]-lens[2]-1 + self.calManager.initSkip] = -1
                self.locCalManager.calendar[3][i-lens[0]-lens[1]-lens[2]-1 + self.calManager.initSkip] = -1
            elif i + self.calManager.initSkip > lens[1] + lens[0]:
                self.calManager.calendar[2][i-lens[0]-lens[1]-1 + self.calManager.initSkip] = -1
                self.locCalManager.calendar[2][i-lens[0]-lens[1]-1 + self.calManager.initSkip] = -1
            elif i + self.calManager.initSkip > lens[0]:
                self.calManager.calendar[1][i-lens[0]-1 + self.calManager.initSkip] = -1
                self.locCalManager.calendar[1][i-lens[0]-1 + self.calManager.initSkip] = -1
            else:
                self.calManager.calendar[0][i-1 + self.calManager.initSkip] = -1
                self.locCalManager.calendar[0][i-1 + self.calManager.initSkip] = -1

    def setDays(self, days=[], surgeonLst=[], calendar=[]):
        lens = []
        for i in self.calManager.calendar:
            lens.append(len(i))

        def elseMinus1(surgeons, surgeonIndex, day, week):
            for i in range(len(surgeons)):
                if i != surgeonIndex:
                    calendar.calendar[week][day] = None

        for i in days:
            if i + self.calManager.initSkip > lens[4] + lens[3] + lens[2] + lens[1] + lens[0]:
                self.calManager.calendar[5][i-lens[0]-lens[1]-lens[2]-lens[3]-lens[4]-1 + self.calManager.initSkip] = 1
                self.locCalManager.calendar[5][i-lens[0]-lens[1]-lens[2]-lens[3]-lens[4]-1 + self.calManager.initSkip] = -1
                elseMinus1(surgeonLst, surgeonLst.index(self), i-lens[0]-lens[1]-lens[2]-lens[3]-lens[4]-1 + self.calManager.initSkip, 5)
            elif i + self.calManager.initSkip > lens[3] + lens[2] + lens[1] + lens[0]:
                self.calManager.calendar[4][i-lens[0]-lens[1]-lens[2]-lens[3]-1 + self.calManager.initSkip] = 1
                self.locCalManager.calendar[4][i-lens[0]-lens[1]-lens[2]-lens[3]-1 + self.calManager.initSkip] = -1
                elseMinus1(surgeonLst, surgeonLst.index(self), i-lens[0]-lens[1]-lens[2]-lens[3]-1 + self.calManager.initSkip, 4)
            elif i + self.calManager.initSkip > lens[2] + lens[1] + lens[0]: 
                self.calManager.calendar[3][i-lens[0]-lens[1]-lens[2]-1 + self.calManager.initSkip] = 1
                self.locCalManager.calendar[3][i-lens[0]-lens[1]-lens[2]-1 + self.calManager.initSkip] = -1
                elseMinus1(surgeonLst, surgeonLst.index(self), i-lens[0]-lens[1]-lens[2]-1 + self.calManager.initSkip, 3)
            elif i + self.calManager.initSkip > lens[1] + lens[0]:
                self.calManager.calendar[2][i-lens[0]-lens[1]-1 + self.calManager.initSkip] = 1
                self.locCalManager.calendar[2][i-lens[0]-lens[1]-1 + self.calManager.initSkip] = -1
                elseMinus1(surgeonLst, surgeonLst.index(self), i-lens[0]-lens[1]-1 + self.calManager.initSkip, 2)
            elif i + self.calManager.initSkip > lens[0]:
                self.calManager.calendar[1][i-lens[0]-1 + self.calManager.initSkip] = 1
                self.locCalManager.calendar[1][i-lens[0]-1 + self.calManager.initSkip] = -1
                elseMinus1(surgeonLst, surgeonLst.index(self), i-lens[0]-1 + self.calManager.initSkip, 1)
            else:
                self.calManager.calendar[0][i-1 + self.calManager.initSkip] = 1
                self.locCalManager.calendar[0][i-1 + self.calManager.initSkip] = -1
                elseMinus1(surgeonLst, i-1 + self.calManager.initSkip, 5)

    def LocSetDays(self, days=[], surgeonLst=[], calendar=[]):
        lens = []
        for i in self.calManager.calendar:
            lens.append(len(i))

        def elseMinus1(surgeons, surgeonIndex, day, week):
            for i in range(len(surgeons)):
                if i != surgeonIndex:
                    calendar.calendar[week][day] = None

        for i in days:
            if i + self.calManager.initSkip > lens[4] + lens[3] + lens[2] + lens[1] + lens[0]:
                self.calManager.calendar[5][i-lens[0]-lens[1]-lens[2]-lens[3]-lens[4]-1 + self.calManager.initSkip] = -1
                self.locCalManager.calendar[5][i-lens[0]-lens[1]-lens[2]-lens[3]-lens[4]-1 + self.calManager.initSkip] = 1
                elseMinus1(surgeonLst, surgeonLst.index(self), i-lens[0]-lens[1]-lens[2]-lens[3]-lens[4]-1 + self.calManager.initSkip, 5)
            elif i + self.calManager.initSkip > lens[3] + lens[2] + lens[1] + lens[0]:
                self.calManager.calendar[4][i-lens[0]-lens[1]-lens[2]-lens[3]-1 + self.calManager.initSkip] = -1
                self.locCalManager.calendar[4][i-lens[0]-lens[1]-lens[2]-lens[3]-1 + self.calManager.initSkip] = 1
                elseMinus1(surgeonLst, surgeonLst.index(self), i-lens[0]-lens[1]-lens[2]-lens[3]-1 + self.calManager.initSkip, 4)
            elif i + self.calManager.initSkip > lens[2] + lens[1] + lens[0]: 
                self.calManager.calendar[3][i-lens[0]-lens[1]-lens[2]-1 + self.calManager.initSkip] = -1
                self.locCalManager.calendar[3][i-lens[0]-lens[1]-lens[2]-1 + self.calManager.initSkip] = 1
                elseMinus1(surgeonLst, surgeonLst.index(self), i-lens[0]-lens[1]-lens[2]-1 + self.calManager.initSkip, 3)
            elif i + self.calManager.initSkip > lens[1] + lens[0]:
                self.calManager.calendar[2][i-lens[0]-lens[1]-1 + self.calManager.initSkip] = -1
                self.locCalManager.calendar[2][i-lens[0]-lens[1]-1 + self.calManager.initSkip] = 1
                elseMinus1(surgeonLst, surgeonLst.index(self), i-lens[0]-lens[1]-1 + self.calManager.initSkip, 2)
            elif i + self.calManager.initSkip > lens[0]:
                self.calManager.calendar[1][i-lens[0]-1 + self.calManager.initSkip] = -1
                self.locCalManager.calendar[1][i-lens[0]-1 + self.calManager.initSkip] = 1
                elseMinus1(surgeonLst, surgeonLst.index(self), i-lens[0]-1 + self.calManager.initSkip, 1)
            else:
                self.calManager.calendar[0][i-1 + self.calManager.initSkip] = -1
                self.locCalManager.calendar[0][i-1 + self.calManager.initSkip] = 1
                elseMinus1(surgeonLst, surgeonLst.index(self), i-1 + self.calManager.initSkip, 5)

md = int(input("Cuantos días tiene el mes?\n"))

id = int(input("Qué dia de la semana es el primero del mes? (0 = lunes, 1 = martes... 6 = domingo)\n"))
print("Pon -1 para indicar que el cirujano no tiene consulta ese mes")
conDay1 = int(input("Qué dia de la semana es en el que tiene consulta Álvaro?"))-1
conDay2 = int(input("Qué dia de la semana es en el que tiene consulta Israel?"))-1
conDay3 = int(input("Qué dia de la semana es en el que tiene consulta Covadonga?"))-1
conDay4 = int(input("Qué dia de la semana es en el que tiene consulta Elena?"))-1
conDay5 = int(input("Qué dia de la semana es en el que tiene consulta Stefan?"))-1
conDay6 = int(input("Qué dia de la semana es en el que tiene consulta Pipe?"))-1
conDay7 = int(input("Qué dia de la semana es en el que tiene consulta Leticia?"))-1
conDay8 = int(input("Qué dia de la semana es en el que tiene consulta Andrés?"))-1
conDay9 = int(input("Qué dia de la semana es en el que tiene consulta Teresa?"))-1

conDays = [conDay1, conDay2, conDay3, conDay4, conDay5, conDay6, conDay7, conDay8, conDay9]
for i in range(len(conDays)):
    if conDays[i] == -1:
        conDays[i] = 6
    if conDays[i] == -2:
        conDays[i] = False

calendar = Calendar(md,id, False) 
locCalendar = Calendar(md, id, False)
Surgeon1 = Surgeon("Álvaro",md,id, conDay1)
Surgeon2 = Surgeon("Israel",md,id, conDay2)
Surgeon3 = Surgeon("Covadonga",md,id, conDay3)
Surgeon4 = Surgeon("Elena",md,id, conDay4)
Surgeon5 = Surgeon("Stefan",md,id, conDay5)
Surgeon6 = Surgeon("Pipe",md,id, conDay6)
Surgeon7 = Surgeon("Leticia",md,id, conDay7)
Surgeon8 = Surgeon("Andrés",md,id, conDay8)
Surgeon9 = Surgeon("Teresa",md,id, conDay9)
surgeons = [Surgeon1, Surgeon2, Surgeon3, Surgeon4, Surgeon5, Surgeon6, Surgeon7, Surgeon8, Surgeon9]

def convCalendars(type):
    if type == "g":
        for i in surgeons:
            for a in range(len(i.calManager.calendar)):
                for b in range(len(i.calManager.calendar[a])):
                    if i.calManager.calendar[a][b] == 1:
                        calendar.calendar[a][b] = i.name
    if type == "l":
        for i in surgeons:
            for a in range(len(i.locCalManager.calendar)):
                for b in range(len(i.locCalManager.calendar[a])):
                    if i.locCalManager.calendar[a][b] == 1:
                        locCalendar.calendar[a][b] = i.name
def addSeed(seed):
    lst = seed
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    surgeons[0].num0 = lst[0]
    surgeons[0].num1 = lst[1]
    surgeons[0].num2 = lst[2]
    surgeons[0].num3 = lst[3]
    surgeons[0].num4 = lst[4]
    surgeons[0].num5 = lst[5]
    surgeons[0].num6 = lst[6]
    
    surgeons[1].num0 = lst[7]
    surgeons[1].num1 = lst[8]
    surgeons[1].num2 = lst[9]
    surgeons[1].num3 = lst[10]
    surgeons[1].num4 = lst[11]
    surgeons[1].num5 = lst[12]
    surgeons[1].num6 = lst[13]
    
    surgeons[2].num0 = lst[14]
    surgeons[2].num1 = lst[15]
    surgeons[2].num2 = lst[16]
    surgeons[2].num3 = lst[17]
    surgeons[2].num4 = lst[18]
    surgeons[2].num5 = lst[19]
    surgeons[2].num6 = lst[20]
    
    surgeons[3].num0 = lst[21]
    surgeons[3].num1 = lst[22]
    surgeons[3].num2 = lst[23]
    surgeons[3].num3 = lst[24]
    surgeons[3].num4 = lst[25]
    surgeons[3].num5 = lst[26]
    surgeons[3].num6 = lst[27]
    
    surgeons[4].num0 = lst[28]
    surgeons[4].num1 = lst[29]
    surgeons[4].num2 = lst[30]
    surgeons[4].num3 = lst[31]
    surgeons[4].num4 = lst[32]
    surgeons[4].num5 = lst[33]
    surgeons[4].num6 = lst[34]
    
    surgeons[5].num0 = lst[35]
    surgeons[5].num1 = lst[36]
    surgeons[5].num2 = lst[37]
    surgeons[5].num3 = lst[38]
    surgeons[5].num4 = lst[39]
    surgeons[5].num5 = lst[40]
    surgeons[5].num6 = lst[41]
    
    surgeons[6].num0 = lst[42]
    surgeons[6].num1 = lst[43]
    surgeons[6].num2 = lst[44]
    surgeons[6].num3 = lst[45]
    surgeons[6].num4 = lst[46]
    surgeons[6].num5 = lst[47]
    surgeons[6].num6 = lst[48]
    
    surgeons[7].num0 = lst[49]
    surgeons[7].num1 = lst[50]
    surgeons[7].num2 = lst[51]
    surgeons[7].num3 = lst[52]
    surgeons[7].num4 = lst[53]
    surgeons[7].num5 = lst[54]
    surgeons[7].num6 = lst[55]
    
    surgeons[8].num0 = lst[56]
    surgeons[8].num1 = lst[57]
    surgeons[8].num2 = lst[58]
    surgeons[8].num3 = lst[59]
    surgeons[8].num4 = lst[60]
    surgeons[8].num5 = lst[61]
    surgeons[8].num6 = lst[62]




    surgeons[0].lnum0 = lst[0+63]
    surgeons[0].lnum1 = lst[1+63]
    surgeons[0].lnum2 = lst[2+63]
    surgeons[0].lnum3 = lst[3+63]
    surgeons[0].lnum4 = lst[4+63]
    surgeons[0].lnum5 = lst[5+63]
    surgeons[0].lnum6 = lst[6+63]
    
    surgeons[1].lnum0 = lst[7+63]
    surgeons[1].lnum1 = lst[8+63]
    surgeons[1].lnum2 = lst[9+63]
    surgeons[1].lnum3 = lst[10+63]
    surgeons[1].lnum4 = lst[11+63]
    surgeons[1].lnum5 = lst[12+63]
    surgeons[1].lnum6 = lst[13+63]
    
    surgeons[2].lnum0 = lst[14+63]
    surgeons[2].lnum1 = lst[15+63]
    surgeons[2].lnum2 = lst[16+63]
    surgeons[2].lnum3 = lst[17+63]
    surgeons[2].lnum4 = lst[18+63]
    surgeons[2].lnum5 = lst[19+63]
    surgeons[2].lnum6 = lst[20+63]
    
    surgeons[3].lnum0 = lst[21+63]
    surgeons[3].lnum1 = lst[22+63]
    surgeons[3].lnum2 = lst[23+63]
    surgeons[3].lnum3 = lst[24+63]
    surgeons[3].lnum4 = lst[25+63]
    surgeons[3].lnum5 = lst[26+63]
    surgeons[3].lnum6 = lst[27+63]
    
    surgeons[4].lnum0 = lst[28+63]
    surgeons[4].lnum1 = lst[29+63]
    surgeons[4].lnum2 = lst[30+63]
    surgeons[4].lnum3 = lst[31+63]
    surgeons[4].lnum4 = lst[32+63]
    surgeons[4].lnum5 = lst[33+63]
    surgeons[4].lnum6 = lst[34+63]
    
    surgeons[5].lnum0 = lst[35+63]
    surgeons[5].lnum1 = lst[36+63]
    surgeons[5].lnum2 = lst[37+63]
    surgeons[5].lnum3 = lst[38+63]
    surgeons[5].lnum4 = lst[39+63]
    surgeons[5].lnum5 = lst[40+63]
    surgeons[5].lnum6 = lst[41+63]
    
    surgeons[6].lnum0 = lst[42+63]
    surgeons[6].lnum1 = lst[43+63]
    surgeons[6].lnum2 = lst[44+63]
    surgeons[6].lnum3 = lst[45+63]
    surgeons[6].lnum4 = lst[46+63]
    surgeons[6].lnum5 = lst[47+63]
    surgeons[6].lnum6 = lst[48+63]
    
    surgeons[7].lnum0 = lst[49+63]
    surgeons[7].lnum1 = lst[50+63]
    surgeons[7].lnum2 = lst[51+63]
    surgeons[7].lnum3 = lst[52+63]
    surgeons[7].lnum4 = lst[53+63]
    surgeons[7].lnum5 = lst[54+63]
    surgeons[7].lnum6 = lst[55+63]
    
    surgeons[8].lnum0 = lst[56+63]
    surgeons[8].lnum1 = lst[57+63]
    surgeons[8].lnum2 = lst[58+63]
    surgeons[8].lnum3 = lst[59+63]
    surgeons[8].lnum4 = lst[60+63]
    surgeons[8].lnum5 = lst[61+63]
    surgeons[8].lnum6 = lst[62+63]

def order():
    classifier.classify(calendar, surgeons)
    classifier.locClassify(locCalendar, surgeons)
    convCalendars("g")
    import csv

    with open("G output.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SÁBADO", "DOMINGO"])
        writer.writerows(calendar.calendar)

    print()
    print()

    convCalendars("l")
    with open("L output.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SÁBADO", "DOMINGO"])
        writer.writerows(locCalendar.calendar)
    print()
    print()

    seed = []
    surgeons[0] = Surgeon1
    surgeons[1] = Surgeon2
    surgeons[2] = Surgeon3
    surgeons[3] = Surgeon4
    surgeons[4] = Surgeon5
    surgeons[5] = Surgeon6
    surgeons[6] = Surgeon7
    surgeons[7] = Surgeon8
    surgeons[8] = Surgeon9

    for i in range(9):
        seed.append([surgeons[i].num0, surgeons[i].num1, surgeons[i].num2, surgeons[i].num3, surgeons[i].num4, surgeons[i].num5, surgeons[i].num6])
    for i in range(9):
        seed.append([surgeons[i].lnum0, surgeons[i].lnum1, surgeons[i].lnum2, surgeons[i].lnum3, surgeons[i].lnum4, surgeons[i].lnum5, surgeons[i].lnum6])

    strseed = str(seed).replace("[", "").replace("]", "").replace(",", "")
    print("\n\n\nSEED: ", strseed)
