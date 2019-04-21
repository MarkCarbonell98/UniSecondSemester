# aufgabe 2a)
# insgesamt gibt es 14 Moglichkeiten:
# Falls es kein Schaltjahr ist, gibt es immer 7 Moglichkeiten zum Anfang des Jahres in Januar, Entweder Montag, Dienstag, Mittwoch, Donnerstag, Freitag, Samstag oder Sonntag. Genauso gilt das für die Schaltjahre. Wenn man alle Moglichkeiten addiert dann sind insgesamt 14.
# Der Anzahl der Schaltjahre seit dem Jahr 0 ergibt sich durch math.floor(aktuellesJahr/4). Die ist gleichzeitig die Anzahl an Tage dass pro Jahr addiert werden sollten, damit die Wochentage von dieses Jahr mit den von Vorherige Jahre korrekt zustimmen.


# aufgabe 2b)
def generateYear(isLeapYear):
    months = ["January", "February", "March","April", "May", "June", "July", "August", "September", "October", "November", "December"]
    totalDays = [31, 29, 31, 30, 31, 30, 31,31,30,31,30,31] if isLeapYear else [31, 28, 31, 30, 31, 30, 31,31,30,31,30,31]
    year = dict(zip(months, totalDays))
    return year

def generateYearWithStartingDay(isLeapYear, yearsFirstDay = "Monday"):
    return {"year": generateYear(isLeapYear), "firstDay": yearsFirstDay, "isLeapYear": isLeapYear}

def generateMonth(year, month, firstDayOfTheMonth, daysOfTheWeek):
    monthlyCalendar, i, firstDayIndex = [], 1, daysOfTheWeek.index(firstDayOfTheMonth)
    while year[month] >= i:
        currentDay = daysOfTheWeek[(firstDayIndex + i - 1)  % 7], i
        monthlyCalendar.append(currentDay)
        i += 1
    return monthlyCalendar 

def generateFullCalendarYear(year):
    daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    yearlyCalendar, firstDayOfTheMonth = {}, year['firstDay']
    for month in year['year']:
        if month != "January":
            lastMonth = yearlyCalendar[list(yearlyCalendar)[-1]]
            lastDayOfTheLastMonth = lastMonth[len(lastMonth)-1][0]
            firstDayOfTheNextMonth = daysOfTheWeek[(daysOfTheWeek.index(lastDayOfTheLastMonth) + 1) % 7]
            yearlyCalendar[month] = generateMonth(year['year'], month, firstDayOfTheNextMonth, daysOfTheWeek)
        else:
            yearlyCalendar[month] = generateMonth(year['year'], month, firstDayOfTheMonth, daysOfTheWeek)
    return yearlyCalendar

def generateAllPossibleYears():
    daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    isLeapYear = [True, False]
    allPossibilities = [(x,y) for x in daysOfTheWeek for y in isLeapYear]
    allPossibleYears = []
    for firstDayOfTheYear,leapYear in allPossibilities:
        newlyAddedYear = generateYearWithStartingDay(leapYear, firstDayOfTheYear)
        allPossibleYears.append(newlyAddedYear)
    return allPossibleYears

def friday13th():
    allPossibleYearsCalendar, totalCount = [], []
    allPossibleYears = generateAllPossibleYears()
    for year in allPossibleYears:
        allPossibleYearsCalendar.append(generateFullCalendarYear(year))

    for year in allPossibleYearsCalendar:
        allFriday13thInThisYear = 0
        for month in year:
            for day,date in year[month]:
                if day == "Friday" and date == 13:
                    allFriday13thInThisYear += 1
        totalCount.append(allFriday13thInThisYear)
    
    for i in range(len(allPossibleYears)):
        currentYear = allPossibleYears[i]
        print(f"Starting day: {currentYear['firstDay']}, is leap year {currentYear['isLeapYear']}, and the amount of Fridays 13th is: {totalCount[i]}")
    
# friday13th()
    
# aufgabe 2c)

import datetime

now = datetime.datetime.now()

def calculateYearlyDifference(day, month, year):
    daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    yearlyDifference = now.year - year
    allYearsOfDifference = []
    theActualDay = datetime.date(year = year, month = month, day = day)
    firstDayOfTheYear = daysOfTheWeek[(int(str(theActualDay - datetime.date(year = year, month = 1, day = 1))[0:2]) - 1) % 7]

    # firstDayOfTheYear = daysOfTheWeek[(str(theActualDay - datetime.date(year = year, month = 1, day = 1))[0:2] + 0) % 7]
    print(firstDayOfTheYear)
    newYearToAppend, lastDayOfTheYearFirstYear = None, None
    for i in range(yearlyDifference):
        if i == 0:
            if (year + i) % 4 == 0:
                newYearToAppend = generateYearWithStartingDay(True, daysOfTheWeek[(day -1) % 7])
            else:
                newYearToAppend = generateYearWithStartingDay(False, daysOfTheWeek[(day -1) % 7])
            allYearsOfDifference.append(generateFullCalendarYear(newYearToAppend))
            lastDayOfTheYearFirstYear = allYearsOfDifference[-1]["December"][30][0]
        else:
            firstDayOfTheYear = (daysOfTheWeek.index(lastDayOfTheYearFirstYear) + 1) % 7 if i == 1 else (firstDayOfTheYear+1) % 7
            print(lastDayOfTheYearFirstYear, firstDayOfTheYear)
            if (year + i) % 4 == 0:
                newYearToAppend = generateYearWithStartingDay(True, daysOfTheWeek[firstDayOfTheYear])
            else:
                newYearToAppend = generateYearWithStartingDay(False, daysOfTheWeek[firstDayOfTheYear])
            allYearsOfDifference.append(generateFullCalendarYear(newYearToAppend))
            

    if len(allYearsOfDifference) == 0:
        if year % 4 == 0:
            newYearToAppend = generateYearWithStartingDay(True, daysOfTheWeek[(day-1) % 7])
        else:
            newYearToAppend = generateYearWithStartingDay(False, daysOfTheWeek[(day-1) % 7])
        allYearsOfDifference.append(generateFullCalendarYear(newYearToAppend))

    return allYearsOfDifference

def friday13thSince(day, month, year):
    if datetime.datetime(year=year, month=month,day=day) > now:
        raise ValueError("The date you entered is not valid")
    
    return calculateYearlyDifference(day, month, year)


difference = friday13thSince(20,1,2019)
print(difference)
# for month in difference:
#     print(month, "\n")



