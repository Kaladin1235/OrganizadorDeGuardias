from functools import reduce

def shuffle(surgeonLst):
   surgeonsLeft = list(surgeonLst)
   
   surgeonsFinal=[]
   for i in range(9):
     if surgeonsLeft == []:
        break
     min = reduce(lambda x, y: x if x.num0+x.num1+x.num2+x.num3+x.num4+x.num5+x.num6 < y.num0+y.num1+y.num2+y.num3+y.num4+y.num5+y.num6 else y, surgeonsLeft).num0+reduce(lambda x, y: x if x.num0+x.num1+x.num2+x.num3+x.num4+x.num5+x.num6 < y.num0+y.num1+y.num2+y.num3+y.num4+y.num5+y.num6 else y, surgeonsLeft).num1+reduce(lambda x, y: x if x.num0+x.num1+x.num2+x.num3+x.num4+x.num5+x.num6 < y.num0+y.num1+y.num2+y.num3+y.num4+y.num5+y.num6 else y, surgeonsLeft).num2+reduce(lambda x, y: x if x.num0+x.num1+x.num2+x.num3+x.num4+x.num5+x.num6 < y.num0+y.num1+y.num2+y.num3+y.num4+y.num5+y.num6 else y, surgeonsLeft).num3+reduce(lambda x, y: x if x.num0+x.num1+x.num2+x.num3+x.num4+x.num5+x.num6 < y.num0+y.num1+y.num2+y.num3+y.num4+y.num5+y.num6 else y, surgeonsLeft).num4+reduce(lambda x, y: x if x.num0+x.num1+x.num2+x.num3+x.num4+x.num5+x.num6 < y.num0+y.num1+y.num2+y.num3+y.num4+y.num5+y.num6 else y, surgeonsLeft).num5+reduce(lambda x, y: x if x.num0+x.num1+x.num2+x.num3+x.num4+x.num5+x.num6 < y.num0+y.num1+y.num2+y.num3+y.num4+y.num5+y.num6 else y, surgeonsLeft).num6

     for i in range(len(surgeonsLeft)):
        if surgeonsLeft[i].num0+surgeonsLeft[i].num1+surgeonsLeft[i].num2+surgeonsLeft[i].num3+surgeonsLeft[i].num4+surgeonsLeft[i].num5+surgeonsLeft[i].num6 == min:
           surgeonsFinal.append(surgeonsLeft[i])
           surgeonsLeft.pop(i)
           break
   return surgeonsFinal
      
def orderSurgeons(surgeons, week, day):

        min012 = reduce(lambda x, y: x if x.num0+x.num1+x.num2 < y.num0+y.num1+y.num2 and x.calManager.calendar[week][day] == 0 else y, surgeons).num0 + reduce(lambda x, y: x if x.num0+x.num1+x.num2 < y.num0+y.num1+y.num2 and x.calManager.calendar[week][day] == 0 else y, surgeons).num1 + reduce(lambda x, y: x if x.num0+x.num1+x.num2 < y.num0+y.num1+y.num2 and x.calManager.calendar[week][day] == 0 else y, surgeons).num2

        min3 = reduce(lambda x, y: x if x.num3 < y.num3 and x.calManager.calendar[week][day] == 0 else y, surgeons).num3

        min46 = reduce(lambda x, y: x if x.num4+x.num6 < y.num4+y.num6 and x.calManager.calendar[week][day] == 0 else y, surgeons).num4 + reduce(lambda x, y: x if x.num4+x.num6 < y.num4+y.num6 and x.calManager.calendar[week][day] == 0 else y, surgeons).num6
        
        min5 = reduce(lambda x, y: x if x.num5 < y.num5 and x.calManager.calendar[week][day] == 0 else y, surgeons).num5
        
        return min012, min3, min46, min5
def locOrderSurgeons(surgeons, week, day):
    min012 = reduce(lambda x, y: x if x.lnum0+x.lnum1+x.lnum2 < y.lnum0+y.lnum1+y.lnum2 and x.locCalManager.calendar[week][day] == 0 else y, surgeons).lnum0 + reduce(lambda x, y: x if x.lnum0+x.lnum1+x.lnum2 < y.lnum0+y.lnum1+y.lnum2 and x.locCalManager.calendar[week][day] == 0 else y, surgeons).lnum1 + reduce(lambda x, y: x if x.lnum0+x.lnum1+x.lnum2 < y.lnum0+y.lnum1+y.lnum2 and x.locCalManager.calendar[week][day] == 0 else y, surgeons).lnum2

    min3 = reduce(lambda x, y: x if x.lnum3 < y.lnum3 and x.locCalManager.calendar[week][day] == 0 else y, surgeons).lnum3

    min46 = reduce(lambda x, y: x if x.lnum4+x.lnum6 < y.lnum4+y.lnum6 and x.locCalManager.calendar[week][day] == 0 else y, surgeons).lnum4 + reduce(lambda x, y: x if x.lnum4+x.lnum6 < y.lnum4+y.lnum6 and x.locCalManager.calendar[week][day] == 0 else y, surgeons).lnum6

    min5 = reduce(lambda x, y: x if x.lnum5 < y.lnum5 and x.locCalManager.calendar[week][day] == 0 else y, surgeons).lnum5

    return min012, min3, min46, min5

def OrderDay(z, day, surgeonLst):
    surgeons = surgeonLst
    surgeons = shuffle(surgeons)
    if day == 0:
        min012, _, _, _ = orderSurgeons(surgeons, z, day)
        for i in surgeons:
         if i.num0 + i.num1 + i.num2 == min012 and i.calManager.calendar[z][0] == 0:
              i.calManager.calendar[z][0] = 1
              if len(i.calManager.calendar[z]) > 1:
                i.calManager.calendar[z][1] = -1
              i.num0 += 1
              break

    elif day == 1:
        min012, _, _, _ = orderSurgeons(surgeons, z, day)
        for i in surgeons:
         if i.num0 + i.num1 + i.num2 == min012 and i.calManager.calendar[z][1] == 0:
              i.calManager.calendar[z][1] = 1
              if len(i.calManager.calendar[z])>2:
                i.calManager.calendar[z][2] = -1
              i.num1 += 1
              break

    elif day == 2:
        min012, _, _, _ = orderSurgeons(surgeons, z, day)
        for i in surgeons:
         if i.num0 + i.num1 + i.num2 == min012 and i.calManager.calendar[z][2] == 0:
              i.calManager.calendar[z][2] = 1
              if len(i.calManager.calendar[z])>3:
                i.calManager.calendar[z][3] = -1
              i.num2 += 1
              break
         
    elif day == 3:
        _, min3, _, _ = orderSurgeons(surgeons, z, day)
        for i in surgeons:
         if i.num3 == min3 and i.calManager.calendar[z][3] == 0:
              i.calManager.calendar[z][3] = 1
              if len(i.calManager.calendar[z])>4:
                if len(i.calManager.calendar[z]) > 4:
                  i.calManager.calendar[z][4] = -1
                if len(i.calManager.calendar[z]) > 5:
                  i.calManager.calendar[z][5] = -1
                if len(i.calManager.calendar[z]) > 6:
                  i.calManager.calendar[z][6] = -1
              i.num3 += 1
              break

    elif day == 4:
        _, _, min46, _ = orderSurgeons(surgeons, z, day)
        for i in surgeons:
         if i.num4 + i.num6 == min46 and i.calManager.calendar[z][4] == 0:
             i.calManager.calendar[z][4] = 1
             if len(i.calManager.calendar[z]) >= 6:
               i.calManager.calendar[z][5] = -1
               i.locCalManager.calendar[z][5] = 1
             if len(i.calManager.calendar[z]) >= 7:
               i.calManager.calendar[z][6] = 1
             if len(i.calManager.calendar) >= z+2:
               i.calManager.calendar[z+1][0] = -1

             i.num4 += 1
             i.num6 += 1
             break
         
    elif day == 5:
        _, _, _, min5 = orderSurgeons(surgeons, z, day)
        for i in surgeons:
         if i.num5 == min5 and i.calManager.calendar[z][5] == 0:
              i.calManager.calendar[z][5] = 1

              i.locCalManager.calendar[z][4] = 1
              if len(i.calManager.calendar[z]) >= 7:
               i.locCalManager.calendar[z][6] = 1
              i.num5+= 1
              break
    
    elif day == 6:
        _, _, min46, _ = orderSurgeons(surgeons, z, day)
        for i in surgeons:
         if i.num6 + i.num4 == min46 and i.calManager.calendar[z][6] == 0 and i.calManager.calendar[z][4] == "--":
              i.calManager.calendar[z][6] = 1
              i.calManager.calendar[z+1][0] = -1
              i.num6 += 1
              break
def locOrderDay(z, day, surgeonLst):
    surgeons = surgeonLst
    surgeons = shuffle(surgeons)
    if day == 0:
        min012, _, _, _ = locOrderSurgeons(surgeons, z, day)
        for i in surgeons:
         if i.lnum0 + i.lnum1 + i.lnum2 == min012 and i.locCalManager.calendar[z][0] == 0 and i.calManager.calendar[z][0] == 0:
              i.locCalManager.calendar[z][0] = 1
              i.lnum0 += 1
              break

    elif day == 1:
        min012, _, _, _ = locOrderSurgeons(surgeons, z, day)
        for i in surgeons:
         if i.lnum0 + i.lnum1 + i.lnum2 == min012 and i.locCalManager.calendar[z][1] == 0 and i.calManager.calendar[z][1] == 0:
              i.locCalManager.calendar[z][1] = 1
              i.lnum1 += 1
              break

    elif day == 2:
        min012, _, _, _ = locOrderSurgeons(surgeons, z, day)
        for i in surgeons:
         if i.lnum0 + i.lnum1 + i.lnum2 == min012 and i.locCalManager.calendar[z][2] == 0 and i.calManager.calendar[z][2] ==0:
              i.locCalManager.calendar[z][2] = 1
              i.lnum2 += 1
              break
         
    elif day == 3:
        _, min3, _, _ = locOrderSurgeons(surgeons, z, day)
        for i in surgeons:
         if i.lnum3 == min3 and i.locCalManager.calendar[z][3] == 0 and i.calManager.calendar[z][3] ==0:
              i.locCalManager.calendar[z][3] = 1
              i.lnum3 += 1
              break

def classify(calendar, surgeons):
    allCalendars = calendar.calendar
    for i in range(len(allCalendars)):
        surgeons = shuffle(surgeons)
        for a in range(len(allCalendars[i])):
            if allCalendars[i][a] != "--" and allCalendars[i][a] != None:
              OrderDay(i, a, surgeons)
def locClassify(calendar, surgeons):
    allCalendars = calendar.calendar
    for i in range(len(allCalendars)):
        surgeons = shuffle(surgeons)
        for a in range(len(allCalendars[i])):
            if allCalendars[i][a] != "--":
              locOrderDay(i, a, surgeons)