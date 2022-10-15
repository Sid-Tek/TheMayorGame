import random
from random import randrange

# print("\033[1;29;38m") # Bold White
# print("\033[0;29;38m" # White

# print("\033[1;31;31m") # Bold Red
# print("\033[0;31;31m") # Red
# print("\033[1;34;48m") # Bold Blue
# print("\033[0;34;48m") # Blue

# print("\033[1;36;48m") # Bold Cyan
# print("\033[0;36;48m") # Cyan

# print("\033[1;35;48m") # Bold Purple
# print("\033[0;35;48m") # Purple

# print("\033[1;33;48m") # Bold Yellow
# print("\033[0;33;48m") # Yellow

# print("\033[0;32;48m]") #Green
# print("\033[1;32;48m]") #Bold Green

def boldWhiteText(x):
    return"\033[1;29;38m" + x + "\033[0;29;38m"
def boldRedText(x):
    return"\033[1;31;31m" + x + "\033[0;29;38m"
def redText(x):
    return"\033[0;31;31m" + x + "\033[0;29;38m"
def boldBlueText(x):
    return"\033[1;34;48m" + x + "\033[0;29;38m"
def blueText(x):
    return"\033[0;34;48m" + x + "\033[0;29;38m"
def boldCyanText(x):
    return"\033[1;36;48m" + x + "\033[0;29;38m"
def cyanText(x):
    return"\033[0;36;48m" + x + "\033[0;29;38m"
def boldPurpleText(x):
    return"\033[1;35;48m" + x + "\033[0;29;38m"
def purpleText(x):
    return"\033[0;35;48m" + x + "\033[0;29;38m"
def boldYellowText(x):
    return"\033[1;33;48m" + x + "\033[0;29;38m"
def yellowText(x):
    return"\033[0;33;48m" + x + "\033[0;29;38m"
def greenText(x):
    return"\033[0;32;48m" + x + "\033[0;29;38m"
def boldGreenText(x):
    return"\033[1;32;48m" + x + "\033[0;29;38m"

disasterCount = 0
MaleFirstNames = ["Collin", "Chadwick", "Dave", "Zack", "Corey", "Harlan", "Ollie",
                  "Freddy", "Phil", "Esteban", "Clifford", "Alexis", "Donn", "Isaiah",
                  "Orval", "Gil", "Rudolph", "Richard", "Wayne", "Elliott", "Guillermo",
                  "Jere", "James", "Dave", "Max", "Damon", "Erasmo", "Jeffry",
                  "Barry", "Blaine"]
FemaleFirstNames = ["Tracy", "Trisha", "Kellie", "Angelina", "Beth",
                    "Brooke", "Arlene", "Lynda", "Renee", "Amber",
                    "Hilary", "Shauna", "Mary", "Marian", "Roslyn",
                    "Carrie", "Barbra", "Rosa", "Hilda", "Lindsay",
                    "Crystal", "Selma", "Johanna", "Cathy", "Herminia",
                    "Tasha", "Erika", "Alyson", "Reva", "Megan"]
LastNames = ['Johns', 'Chase', 'Joyce', 'Bowen', 'Cole', 'Roberts', 'Vargas', 'Murillo', 'Ferguson', 'Acevedo',
             'Monroe',
             'Singh', 'Reeves', 'Cantrell', 'Ware', 'Stevenson', 'Bailey', 'Larsen', 'Garrett', 'Martin', 'Wilson',
             'Dickson', 'Boseman'
             'Dennis', 'Padilla', 'Morrison', 'Sullivan', 'Stokes', 'Goodwin', 'Holden', 'Simpson']

def create_Male():
    return MaleFirstNames[int(randrange(30))] + " " + LastNames[int(randrange(30))]
def create_Female():
    return FemaleFirstNames[int(randrange(30))] + " " + LastNames[int(randrange(31))]
def create_randName():
    x = int(randrange(1))
    if x == 0:
        return create_Male()
    else:
        return create_Female()

councilLeaning = ""
global councilOpinion
councilOpinion = 5
global publicSupport
publicSupport = 50


policy_Town = [
"Create a Town Website",                "Create a Free Town Wifi",       "Host a Job Fair for Businesses",         "Fund a Meals on Wheels Program", 
"Repair Aging Roads",                   "Create a Local Produce Market", "Build Affordable Housing",               "Renovate the Town Library", 
"Create a Town Recycling Program",      "Renovate the Town Square",      "Build a Community College",              "Develop a Bike Share Program",
"Fund a Firefighter Volunteer Program", "Host a Music Festival",         "Install Solar Panels on the Town Hall",  "Fund Public Bus Transportation",
"Host a Blood Drive",                   "Establish School Gardens",      "Fund a Books on Wheels Program",         "Build a Museum"]

policy_TownCost = [
'50000', '100000', '30000', '20000', 
'70000', '35000', '200000' ,'150000', 
'15000', '75000', "1500000", "45000",
"25000", "50000", "65000", "150000",
"10000", "15000", "40000", "1000000"]

oldProposals = ["",""]

townAgenda = [policy_Town[int(randrange(len(policy_Town)))]]

def checkOldTownProposal(policy):
    global policy_Town
    global oldProposals
    n = 0
    while n < len(oldProposals):
        if policy == oldProposals[n]:
            return True
        else:
            n += 1
    return False

def chooseTownAgenda():
    randNum = int(random.randrange(0, len(policy_Town)))
    agenda = policy_Town[randNum]
    while checkOldTownProposal(agenda) == True:
        randNum = int(random.randrange(0, len(policy_Town)))
        agenda = policy_Town[randNum]
    agenda = "".join(agenda)
    return agenda

taxPropertyRate = 5.0
taxSalesRate = 5.0
taxIncomeRate = 5.0
taxBusinessRate = 5.0

yearlyPassedPolicies = []

def calculateAnnualIncome():
    return int(1200*((population * taxPropertyRate/100) + (population * taxSalesRate/100) + (population * taxIncomeRate/100) + (population * taxBusinessRate/100)))

def displayMoney(x):
    string = str(x)
    if '.' in string:
        periodPosition = string.find('.')
        n = periodPosition
        n -= 3
        while n > 0:
            if string[n - 1] != '-':
                string = string[:n] + "," + string[n:]
            n -= 3
        return string
    else:
        n = len(string) - 3
        while n > 0:
            if string[n-1] != '-':
                string = string[:n] + "," + string[n:]
            n -= 3
        return string

funds = 50000
population = 5000
annualIncome = calculateAnnualIncome()


department_FireFundStates = [10*population, 20*population, 30*population]#RED
department_PoliceFundStates = [10*population, 20*population, 30*population]#BLUE
department_EducationFundStates = [10*population, 20*population, 30*population]#PURPLE
department_HealthFundStates = [20*population, 30*population, 40*population]#WHITE
department_RecreationalFundStates = [5*population, 10*population, 20*population]#GREEN
department_InfrastructureFundStates = [10*population, 20*population, 30*population]#YELLOW

department_FireFunding = department_FireFundStates[1]
department_PoliceFunding = department_PoliceFundStates[1]
department_EducationFunding = department_EducationFundStates[1]
department_HealthFunding = department_HealthFundStates[1]
department_RecreationalFunding = department_RecreationalFundStates[1]
department_InfrastructureFunding = department_InfrastructureFundStates[1]

currentFireState = department_FireFundStates[2]
newFireState = department_FireFundStates[2]
currentPoliceState = department_PoliceFundStates[2]
newPoliceState = department_PoliceFundStates[2]

currentHealthState = department_HealthFundStates[2]
newHealthState = department_HealthFundStates[2]

currentEducationState = department_EducationFundStates[2]
newEducationState = department_EducationFundStates[2]

currentRecState = department_RecreationalFundStates[2]
newRecState = department_RecreationalFundStates[2]

currentInfrastructureState = department_InfrastructureFundStates[2]
newInfrastructureState = department_InfrastructureFundStates[2]

mission = ''

month = ["January", "May", "September"]
monthCounter = 0
year = 1

missionAccepted = 0

def inputToNumber(str):
    newString = str.replace("$","")
    newString = newString.replace(",","")
    return newString

def chooseRandDepartment():
    x = int(randrange(0,5))
    if x == 0:
        return 'Fire Department'
    if x == 1:
        return 'Police Department'
    if x == 2:
        return 'Health Department'
    if x == 3:
        return 'Education Department'
    if x == 4:
        return 'Infrastructure Department'
    if x == 5:
        return 'Rec Department'

def changePublicSupport(x):
    global publicSupport
    publicSupport += x
    if publicSupport > 100:
        publicSupport = 100
    if publicSupport < 0:
        publicSupport = 0

def changeCouncilOpinion(x):
    global councilOpinion
    councilOpinion += x
    if councilOpinion > 10:
        councilOpinion = 10
    if councilOpinion < 0:
        councilOpinion = 0

def findTownProposalCost():
    n = 0
    while ''.join(policy_Town[n]) != ''.join(townAgenda):
        n += 1
    return "".join(policy_TownCost[n])

def nextDate():
    global monthCounter
    global year
    monthCounter += 1
    if monthCounter == 3:
        year += 1
        monthCounter = 0

def giveDate():
    return boldWhiteText(str((month[monthCounter] + ", Year " + str(year))))

def findDepartmentFundingLevel(x):
    if x == 'fire':
        if department_FireFunding <= department_FireFundStates[0]:
            return 'Underfunded'
        if department_FireFunding <= department_FireFundStates[1]:
            return 'Funded'
        else:
            return 'Well-Funded'
    if x == 'police':
        if department_PoliceFunding <= department_PoliceFundStates[0]:
            return 'Underfunded'
        if department_PoliceFunding <= department_PoliceFundStates[1]:
            return 'Funded'
        else:
            return 'Well-Funded'
    if x == 'education':
        if department_EducationFunding <= department_EducationFundStates[0]:
            return 'Underfunded'
        if department_EducationFunding <= department_EducationFundStates[1]:
            return 'Funded'
        else:
            return 'Well-Funded'
    if x == 'health':
        if department_HealthFunding <= department_HealthFundStates[0]:
            return 'Underfunded'
        if department_HealthFunding <= department_HealthFundStates[1]:
            return 'Funded'
        else:
            return 'Well-Funded'
    if x == 'rec':
        if department_RecreationalFunding <= (department_RecreationalFundStates[0]):
            return 'Underfunded'
        if department_RecreationalFunding <= department_RecreationalFundStates[1]:
            return 'Funded'
        else:
            return 'Well-Funded'
    if x == 'infrastructure':
        if department_InfrastructureFunding <= department_InfrastructureFundStates[0]:
            return 'Underfunded'
        if department_InfrastructureFunding <= department_InfrastructureFundStates[1]:
            return 'Funded'
        else:
            return 'Well-Funded'

def TE_DepartmentFunding():
    global publicSupport
    
    if department_FireFunding == 'Underfunded':
        print("An " + redText('underfunded') + " Fire Department has found it harder to deal with fires, and people are noticing.")
        print("Public support has " + redText('fallen') + " by 10%")
        changePublicSupport(-10)
        input("Public support is now " + str(publicSupport) + ".\n")

    if department_PoliceFunding == 'Underfunded':
        print("An " + redText('underfunded') + " Police Department has found it harder to deal with crime, and people are noticing.")
        print("Public support has " + redText('fallen') + " by 10%")
        changePublicSupport(-10)
        input("Public support is now " + str(publicSupport) + ".\n")
                    
    if department_HealthFunding == 'Underfunded':
        print("An " + redText('underfunded') + " Health Department has found it harder to help provide healthcare, and people are noticing.")
        print("Public support has " + redText('fallen') + " by 10%")
        changePublicSupport(-10)
        input("Public support is now " + str(publicSupport) + ".\n")
                    
    if department_EducationFunding == 'Underfunded':
        print("An " + redText('underfunded') + " Education Department has been forced to make cuts in school spending, and people are noticing.")
        print("Public support has " + redText('fallen') + " by 10%")
        changePublicSupport(-10)
        input("Public support is now " + str(publicSupport) + ".\n")
                    
    if department_InfrastructureFunding == 'Underfunded':
        print("An " + redText('underfunded') + " Infrastructure Department has found it harder to maintain roads, and people are noticing.")
        print("Public support has " + redText('fallen') + " by 10%")
        changePublicSupport(-10)
        input("Public support is now " + str(publicSupport) + ".\n")
                    
    if department_RecreationalFunding == 'Underfunded':
        print("An " + redText('underfunded') + " Recreation Department has found it harder to maintain parks, and people are noticing.")
        print("Public support has " + redText('fallen') + " by 10%")
        changePublicSupport(-10)
        input("Public support is now " + str(publicSupport) + ".\n")
                    
    if department_FireFunding == 'Well-Funded':
        print("A " + greenText('well-funded') + " Fire Department has been able to deal with fires in record time, and people are noticing.")
        print("Public support has " + greenText('risen') + " by 10%")
        changePublicSupport(10)
        input("Public support is now " + str(publicSupport) + ".\n")
                    
    if department_PoliceFunding == 'Well-Funded':
        print("A " + greenText('well-funded') + " Police Department has been able to lower the crime rate, and people are noticing.")
        print("Public support has " + greenText('risen') + " by 10%")
        changePublicSupport(10)
        input("Public support is now " + str(publicSupport) + ".\n")
                    
    if department_HealthFunding == 'Well-Funded':
        print("A " + greenText('well-funded') + " Health Department has been able to provide better quality healthcare, and people are noticing.")
        print("Public support has " + greenText('risen') + " by 10%")
        changePublicSupport(10)
        input("Public support is now " + str(publicSupport) + ".\n")
                    
    if department_EducationFunding == 'Well-Funded':
        print("A " + greenText('well-funded') + " Education Department has been able to fund improvements for local schools, and people are noticing.")
        print("Public support has " + greenText('risen') + " by 10%")
        changePublicSupport(10)
        input("Public support is now " + str(publicSupport) + ".\n")
                    
    if department_InfrastructureFunding == 'Well-Funded':
        print("A " + greenText('well-funded') + " Fire Department has been able to deal with fires in record time, and people are noticing.")
        print("Public support has " + greenText('risen') + " by 10%")
        changePublicSupport(10)
        input("Public support is now " + str(publicSupport) + ".\n")
                    
    if department_RecreationalFunding == 'Well-Funded':
        print("A " + greenText('well-funded') + " Recreation Department has been able improve local parks, and people are noticing.")
        print("Public support has " + greenText('risen') + " by 10%")
        changePublicSupport(10)
        input("Public support is now " + str(publicSupport) + ".\n")
    return""

def displayDepartmentFunding():
    print(redText("Fire Department") + ': ' + greenText('$') + greenText(displayMoney(department_FireFunding)) + ". Funding level: " + findDepartmentFundingLevel('fire'))
    print(blueText("Police Department") + ': ' + greenText('$') + greenText(displayMoney(department_PoliceFunding)) + ". Funding level: " + findDepartmentFundingLevel('police'))
    print("Health Department: $" + greenText(displayMoney(department_HealthFunding)) + ". Funding level: " + findDepartmentFundingLevel('health'))
    print(purpleText("Education Department") + ': ' + greenText('$')+ greenText(displayMoney(department_EducationFunding)) + ". Funding level: " + findDepartmentFundingLevel('education'))
    print(yellowText("Infrastructure Department") + ': ' + greenText('$') + greenText(displayMoney(department_InfrastructureFunding)) + ". Funding level: " + findDepartmentFundingLevel('infrastructure'))
    print(greenText('Parks and Recreation Department') + ': ' + greenText('$') + greenText(displayMoney(department_RecreationalFunding)) + ". Funding level: " + findDepartmentFundingLevel('rec'))

councilMissions = []

def chooseCouncilMission():
    global councilMissions
    councilMissions = []
    if taxIncomeRate > 10:
        councilMissions.append('incomeLower')
    if taxSalesRate > 10:
        councilMissions.append('salesLower')
    if taxBusinessRate > 10:
        councilMissions.append('businessLower')
    if taxPropertyRate > 10:
        councilMissions.append('propertyLower')
    if findDepartmentFundingLevel('fire') != 'Well-Funded':
        councilMissions.append('fireFunding')
    if findDepartmentFundingLevel('police') != 'Well-Funded':
        councilMissions.append('policeFunding')
    if findDepartmentFundingLevel('health') != 'Well-Funded':
        councilMissions.append('healthFunding')
    if findDepartmentFundingLevel('education') != 'Well-Funded':
        councilMissions.append('educationFunding')
    if findDepartmentFundingLevel('infrastructure') != 'Well-Funded':
        councilMissions.append('infrastructureFunding')
    if findDepartmentFundingLevel('rec') != 'Well-Funded':
        councilMissions.append('recFunding')
    else:
        councilMissions.append('none')
    return""

def decideCouncilProposal():
    global councilOpinion
    global funds
    global mission
    global missionAccepted
    global name
    global councilMissions
    print("The " + boldPurpleText('town council') + " has sent you a letter. " + "\033[0;03;48m")
    chooseCouncilMission()
    mission = random.choice(councilMissions)
    mission = "".join(mission)
    if mission == 'incomeLower':
        print("Dear " + str(name) + ":\n" + "   Reduce the income tax rate to at least 10%")
        mission = 'incomeLower'
    if mission == 'salesLower':
        print("Dear " + str(name) + ":\n" + "   Reduce the sales tax rate to at least 10%")
        mission = 'salesLower'
    if mission == 'businessLower':
        print("Dear " + str(name) + ":\n" + "   Reduce the business tax rate to at least 10%")
        mission = 'businessLower'
    if mission == 'propertyLower':
        print("Dear " + str(name) + ":\n" + "   Reduce the property tax rate to at least 10%")
        mission = 'propertyLower'
    if mission == 'fireFunding':
        print("Dear " + str(name) + ":\n" + "   Increase the Fire Department's funding level")
        mission = 'fireFunding'
    if mission == 'policeFunding':
        print("Dear " + str(name) + ":\n" + "   Increase the Police Department's funding level")
        mission = 'policeFunding'
    if mission == 'healthFunding':
        print("Dear " + str(name) + ":\n" + "   Increase the Health Department's funding level")
        mission = 'healthFunding'
    if mission == 'educationFunding':
        print("Dear " + str(name) + ":\n" + " Increase the Education Department's funding level")
        mission = 'educationFunding'
    if mission == 'infrastructureFunding':
        print("Dear " + str(name) + ":\n" + "   Increase the Infrastructure Department's funding level")
        mission = 'infrastructureFunding'
    if mission == 'recFunding':
        print("Dear " + str(name) + ":\n" + "   Increase the Parks and Recreation Department's funding level")
        mission = 'recFunding'
    if mission == 'none':
        print("Dear " + str(name) + ":\n" + "   You're doing a good job running this town. Keep it up!")
        mission = 'none'
        changeCouncilOpinion(2)
        input("Council opinion has " +  greenText('increased') + " by 2. It is now " + str(councilOpinion) + "\n")
    
    while 1==1:
        if mission == 'none':
            break
        decision = str(input("\033[0;32;38m" + "To promise the council that you'll " + purpleText(returnCouncilProposal()) + ", type 1. To reject it, type 2.\n"))
        if (decision != '1') and (decision != '2'):
            print("Input not recognized")
            continue
        if decision == '1':
            input("You have " + greenText('accepted') + " the council's task\n")
            missionAccepted = 1
            break
        if decision == '2':
            print("You have decided " + redText('not') + " to "  + str(returnCouncilProposal()))
            changeCouncilOpinion(-1)
            input("Council opinion has " +  redText('fallen') + " by 1. It is now " + str(councilOpinion) + "\n")
            missionAccepted = 0
            break
def returnTownProposal():
    return "".join(townAgenda)

def decideTownProposal():
    global publicSupport
    global funds
    global townAgenda
    global oldProposals
    name = str(create_randName())
    townAgenda = chooseTownAgenda() 
    oldProposals.append(townAgenda) 
    print(blueText('Local Citizen ') + name + " has proposed to " + blueText(returnTownProposal()) + ".")
    print("The cost of this proposal is estimated to be " + greenText('$') + greenText(str(displayMoney(findTownProposalCost())) + "\n"))
    print("Your funds: " + greenText(displayMoney(funds)))
    while 1==1:
        decision = str(input("To approve the proposal, type 1. To reject it, type 2.\n"))
        if (decision != '1') and (decision != '2'):
            print("Input not recognized")
            continue
        if decision == '1':
            if funds >= int(findTownProposalCost()):
                print("You have " + greenText('supported') + " the proposal to " + returnTownProposal())
                increase = 0
                if int(findTownProposalCost()) >= 1000000:
                    increase = 10
                elif int(findTownProposalCost()) >= 500000:
                    increase = 8
                else:
                    increase = 5
                publicSupport += increase
                funds -= int(findTownProposalCost())
                print("Your now have " + greenText('$') + greenText(str(displayMoney(funds)) + " left"))
                input("Public support has increased by " + greenText(str(increase)) + "%. It is now " + str(publicSupport) + "%\n")
                yearlyPassedPolicies.append(returnTownProposal())
                break
            else:
                print('You do not have enough funds to afford this proposal')
                continue
        if decision == '2':
            print("You have " + redText('rejected') + " the proposal to " + returnTownProposal())
            publicSupport -= 5
            input("Public support has fallen by 5%. It is now " + str(publicSupport) + "%\n")
            break
    return''

def TE_CouncilChangesSupport():
    global publicSupport
    global councilOpinion
    if monthCounter == 0:
        if councilOpinion > 6 or councilOpinion < 4:
            if councilOpinion > 6:
                print("A happy council has led to increased public support!")
                changePublicSupport(int(1.2*(5 + councilOpinion)))
                print("Public support has increased by " + str(int(1.2*councilOpinion)) + "%")
                input("Public support is now at " + str(publicSupport) + "%\n")
            if councilOpinion < 4:
                print("An unhappy council has led to decreased public support!")
                changePublicSupport(-1 * int(1.2*(5 - councilOpinion)))
                print("Public support has decreased by " + str(int(1.2*councilOpinion)) + "%")
                input("Public support is now at " + str(publicSupport) + "%\n")

def returnCouncilProposal():
    if mission == 'incomeLower':
        return"Lower the Income Tax Rate to at least 10%"
    if mission == 'salesLower:':
        return"Lower the Sales Tax Rate to at least 10%"
    if mission == 'businessLower':
        return"Lower the Business Tax Rate to at least 10%"
    if mission == 'propertyLower':
        return"Lower the Property Tax Rate to at least 10%"
    if mission == 'fireFunding':
        return"Increase the Fire Department's funding level"
    if mission == 'policeFunding':
        return"Increase the Police Department's funding level"
    if mission == 'healthFunding':
        return"Increase the Health Department's funding level"
    if mission == 'educationFunding':
        return"Increase the Education Department's funding level"
    if mission == 'infrastructureFunding':
        return"Increase the Infrastructure Department's funding level"
    if mission == 'recFunding':
        return"Increase the Parks and Recreation Department's funding level"

def displayTaxes():
    print("Property Tax: " + str(taxPropertyRate) + "%")
    print("Sales Tax: " + str(taxSalesRate) + "%")
    print("Income Tax: " + str(taxIncomeRate) + "%")
    print("Business Tax: " + str(taxBusinessRate) + "%")

def findRevenue():
    global funds
    revenue = calculateAnnualIncome()
    costs = department_FireFunding + department_PoliceFunding + department_HealthFunding + department_InfrastructureFunding + department_EducationFunding + department_RecreationalFunding
    total = revenue - costs
    return total

change = 0
changeValue = 'neg'

def findTaxSupportEffect():
    global taxIncomeRate
    global taxPropertyRate
    global taxBusinessRate
    global taxSalesRate
    global publicSupport
    global change
    global changeValue

    iT = taxIncomeRate - 5
    pT = taxPropertyRate - 5
    bT = taxBusinessRate - 5
    sT = taxSalesRate - 5

    change = (iT + pT + sT + bT) #How much public support decreases
    print("")
    if change > 0:
        changeValue = 'neg'
        return("With the current tax rates, public support will " + redText('decrease') + " by " + redText(str(change)) + "%.")
    if change < 0:
        changeValue = 'pos'
        change = change * -1
        return("With the current tax rates, public support will " + blueText('increase') + " by " + blueText(str(change)) + "%.")
    else:
        return("With the current tax rates, public support will remain the same.")

def displayBudget():
    global funds
    revenue = calculateAnnualIncome()
    costs = department_FireFunding + department_PoliceFunding+ department_HealthFunding + department_InfrastructureFunding + department_EducationFunding + department_RecreationalFunding
    total = revenue - costs

    if funds >= 0:
        print("Current Funds: $" + greenText(displayMoney(str(funds))))
    else:
        print("Current Funds: " + redText(str(funds)))
    print("Revenue: $" + greenText(displayMoney(revenue)))
    print("Costs: $" + redText(displayMoney(costs)))
    print("Currently we would make $" + boldGreenText(displayMoney(total)) + " this year")
    if total < 0:
        boldRedText(print("We would be gaining debt under this budget!"))

def manageBudget():
    global funds
    global taxPropertyRate
    global taxSalesRate
    global taxBusinessRate
    global taxIncomeRate
    global department_FireFunding
    global department_PoliceFunding
    global department_EducationFunding
    global department_HealthFunding
    global department_RecreationalFunding
    global department_InfrastructureFunding
    global currentFireState
    global newFireState
    global currentPoliceState
    global newPoliceState
    global currentHealthState
    global newHealthState
    global currentEducationState
    global newEducationState
    global currentInfrastructureState
    global newInfrastructureState
    global currentRecState
    global newRecState
    global publicSupport
    global changeValue

    currentFireState = findDepartmentFundingLevel('fire')
    currentPoliceState = findDepartmentFundingLevel('police')
    currentHealthState = findDepartmentFundingLevel('health')
    currentEducationState = findDepartmentFundingLevel('education')
    currentRecState = findDepartmentFundingLevel('red')
    currentInfrastructureState = findDepartmentFundingLevel('infrastructure')

    input("It is time to determine the " + greenText('budget') + " for this year!\n")
    while 1==1:
        displayTaxes()
        print("\n")
        displayDepartmentFunding()
        print('\n')
        displayBudget()
        if year > 1 and missionAccepted == 1:
            print("Council Mission: " + purpleText(str(returnCouncilProposal())))
        print("\n")

        decision = str(input("To change tax rates, type '1'. To determine department funding, type '2'\n"
                             "To confirm the year's budget, type 'end'\n"))
        if decision == '1':
            decision = str(input("To change the property tax, type 1. To change the sales tax, type 2. "
                                 "To change the income tax, type 3. To change the business tax, type 4\n"))
            if decision == '1':
                decision = str(input("What will the new property tax rate be? Type what the new percent rate is. Input a whole number from 0 to 100.\n"))
                if decision.isnumeric() and 0 <= float(decision) <= 100:
                    taxPropertyRate = float(decision)
                    print("Property tax changed! It is now " + str(taxPropertyRate) + "%")
                    continue
                else:
                    print("Please input a whole number from 0 to 100")
                    continue
            if decision == '2':
                decision = str(input("What will the new sales tax rate be? Type what the new percent rate is. Input a whole number from 0 to 100.\n"))
                if decision.isnumeric() and 0 <= float(decision) <= 100:
                    taxSalesRate = float(decision)
                    print("Sales tax changed! It is now " + str(taxSalesRate) + "%")
                    continue
                else:
                    print("Please input a whole number from 0 to 100")
                    continue
            if decision == '3':
                decision = str(input("What will the new income tax rate be? Type what the new percent rate is. Input a whole number from 0 to 100.\n"))
                if decision.isnumeric() and 0 <= float(decision) <= 100:
                    taxIncomeRate = float(decision)
                    print("Income tax changed! It is now " + str(taxIncomeRate) + "%")
                    continue
                else:
                    print("Please input a whole number from 0 to 100")
                    continue
            if decision == '4':
                decision = str(input("What will the new business tax rate be? Type what the new percent rate is. Input a whole number from 0 to 100.\n"))
                if decision.isnumeric() and 0 <= float(decision) <= 100:
                    taxBusinessRate = float(decision)
                    print("Business tax changed! It is now " + str(taxBusinessRate) + "%")
                    continue
                else:
                    print("Please input a whole number from 0 to 100")
                    continue
        if decision == '2':
            displayDepartmentFunding()
            while 1==1:
                decision = str(input("\nTo change funding for the Fire Department, type 1. "
                                     "To change funding for the Police Department, type 2.\n"
                                     "To change funding for the Health Department, type 3. "
                                     "To change funding for the Education Department, type 4.\n"
                                     "To change funding for the Infrastructure Department, type 5. "
                                     "To change funding for the Parks and Recreation Department, type 6.\n"))
                if decision == '1':
                    decision = (inputToNumber(input("What will the new funding for the Fire Department be?. It is currently given $" +
                                         displayMoney(department_FireFunding) + ", making the department " + str(findDepartmentFundingLevel('fire'))+"\n")))
                    if decision.isnumeric():
                        department_FireFunding = float(decision)
                        print("The new funding for the Fire Department is $" + displayMoney(department_FireFunding) + "\n")
                        break
                    else:
                        print("Input not recognized")
                        continue
                if decision == '2':
                    decision = (inputToNumber(input("What will the new funding for the Police Department be?. It is currently given $" +
                                         displayMoney(department_PoliceFunding) + ", making the department " + str(findDepartmentFundingLevel('police'))+"\n")))
                    if decision.isnumeric():
                        department_PoliceFunding = int(decision)
                        print("The new funding for the Police Department is $" + displayMoney(department_PoliceFunding) + "\n")
                        break
                    else:
                        print("Input not recognized")
                        continue
                if decision == '3':
                    decision = (inputToNumber(input("What will the new funding for the Health Department be?. It is currently given $" +
                                         displayMoney(department_HealthFunding) + ", making the department " + str(findDepartmentFundingLevel('health'))+"\n")))
                    if decision.isnumeric():
                        department_HealthFunding = int(decision)
                        print("The new funding for the Health Department is $" + displayMoney(department_HealthFunding) + "\n")
                        break
                    else:
                        print("Input not recognized")
                        continue
                if decision == '4':
                    decision = (inputToNumber(input("What will the new funding for the Education Department be?. It is currently given $" +
                                         displayMoney(department_EducationFunding) + ", making the department " + str(findDepartmentFundingLevel('education'))+"\n")))
                    if decision.isnumeric():
                        department_EducationFunding = int(decision)
                        print("The new funding for the Education Department is $" + displayMoney(department_EducationFunding) + "\n")
                        break
                    else:
                        print("Input not recognized")
                        continue
                if decision == '5':
                    decision = (inputToNumber(input("What will the new funding for the Infrastructure Department be?. It is currently given $" +
                                         displayMoney(department_InfrastructureFunding) + ", making the department " + str(findDepartmentFundingLevel('infrastructure'))+"\n")))
                    if decision.isnumeric():
                        department_InfrastructureFunding = int(decision)
                        print("The new funding for the Infrastructure Department is $" + displayMoney(department_InfrastructureFunding) + "\n")
                        break
                    else:
                        print("Input not recognized")
                        continue
                if decision == '6':
                    decision = (inputToNumber(input("What will the new funding for the Parks and Recreation Department be?. It is currently given $" +
                                         displayMoney(department_RecreationalFunding) + ", making the department " + str(findDepartmentFundingLevel('rec'))+"\n")))
                    if decision.isnumeric():
                        department_RecreationalFunding = int(decision)
                        print("The new funding for the Parks and Recreation Department is $" + displayMoney(department_FireFunding) + "\n")
                        break
                    else:
                        print("Input not recognized")
                        continue
                continue

        if decision == 'end':
            print(findTaxSupportEffect())
            decision = input('To confirm the budget change, type 1. To go back, type 2.\n\n')
            if decision == '1':
                newFireState = findDepartmentFundingLevel('fire')
                newPoliceState = findDepartmentFundingLevel('police')
                newHealthState = findDepartmentFundingLevel('health')
                newEducationState = findDepartmentFundingLevel('education')
                newRecState = findDepartmentFundingLevel('red')
                newInfrastructureState = findDepartmentFundingLevel('infrastructure')

                print("The budget for this year has been confirmed!")
                if changeValue == 'neg':
                    publicSupport -= change
                else:
                    publicSupport += change
                print("Public support is now " + str(publicSupport) + "%")
                revenue = calculateAnnualIncome()
                costs = department_FireFunding + department_PoliceFunding + department_HealthFunding + department_InfrastructureFunding + department_EducationFunding + department_RecreationalFunding
                total = revenue - costs
                funds += total
                print("\n")
                break
        if decision == '2':
            print("")
            continue

def TE_populationChange():
    global population
    global publicSupport
    if publicSupport > 60:
        boldWhiteText("Population Change:")
        print("A happy population has attracted more people to the town!")
        population += (publicSupport*2)
        print("The population has rose by " + str(publicSupport*2))
        input("Total population is now " + str(population) + ".\n")
    if publicSupport < 40:
        boldWhiteText("Population Change:")
        print("An unhappy population has resulted in people leaving the town!")
        population -= (publicSupport * 2)
        print("The population has fallen by " + str(publicSupport * 2))
        input("Total population is now " + str(population) + ".\n")
    return''

def TE_debt():
    global funds
    global publicSupport
    if funds < 0:
        input("With your town " + redText('mired in debt') + ", the public is " + redText('losing faith') + " in your administration!\n")
        print("Public support has " + redText('fallen') + " by 5%!")
        publicSupport -= 5
        input("Public support is now " + str(publicSupport) + "%.\n")

def disaster():
    global disasterCount
    global publicSupport
    global funds
    #Fire, Flooding, Building Collapse, Bridge Collapse, Tornado, Water Line Broke, Gas Line Broke, Telecom Towers Collapse (wind)
    x = random.randrange(0,9)
    if x < 3 and disasterCount < 2:
        disasterCount += 1
        y = random.randrange(0,3)
        if y == 0:
            department = chooseRandDepartment()
            payAmount = 250000
            input(boldRedText("DISASTER!\n"))
            input("A " + redText('devastating fire') + ' has badly damaged the ' + str(department) + "!\n")
            while 1 == 1:
                decision = str(input("It will cost $" + greenText(str(payAmount)) + " to repair the department. To fund the repairs, type 1. To not fund the repairs, type 2. However, not repairing the department"
                                                                       " will have consequences\n"))
                if decision == '1':
                    if funds >= payAmount:
                        funds -= payAmount
                        print("The " + str(department) + " has been repaired! Public support has increased thanks to your decisive action!")
                        print("Public support has increased by 10%")
                        publicSupport += 10
                        print("Public support is now " + str(publicSupport) + "%")
                        input("You now have $" + greenText(str(funds)) + " left\n")
                        break
                    else:
                        print("You don't have enough funds.")
                        continue
                if decision == '2':
                    print("You have decided not to fund repairs for the " + str(department) + ". The public is outraged!")
                    print("Public support has decreased by 20%")
                    publicSupport -= 20
                    input("Public support is now " + str(publicSupport) + "%\n")
                    break
                else:
                    print("Input not recognized")
        if y == 1:
            department = chooseRandDepartment()
            payAmount = 250000
            input(boldRedText("DISASTER!\n"))
            input("A " + redText('devastating flood') + ' has badly damaged the ' + str(department) + "!\n")
            while 1 == 1:
                decision = str(input("It will cost $" + greenText(str(payAmount)) + " to repair the department. To fund the repairs, type 1. To not fund the repairs, type 2. However, not repairing the department"
                                 " will have consequences\n"))
                if decision == '1':
                    if funds >= payAmount:
                        funds -= payAmount
                        print("The " + str(department) + " has been repaired! Public support has increased thanks to your decisive action!")
                        print("Public support has increased by 10%\n")
                        publicSupport += 10
                        print("Public support is now " + str(publicSupport) + "%")
                        input("You now have $" + greenText(str(funds)) + " left\n")
                        break
                    else:
                        print("You don't have enough funds.")
                        continue
                if decision == '2':
                    print("You have decided not to fund repairs for the " + str(department) + ". The public is outraged!")
                    print("Public support has decreased by 20%")
                    publicSupport -= 20
                    input("Public support is now " + str(publicSupport)+ "%\n")
                    break
                else:
                    print("Input not recognized")
        if y == 2:
            department = chooseRandDepartment()
            payAmount = 250000
            input(boldRedText("DISASTER!\n"))
            input("The town's residential water line has " + redText('broke') + ", and many residents now lack access to drinking water!\n")
            while 1 == 1:
                decision = str(input("It will cost $" + greenText(str(payAmount)) + " to repair the water line. To fund the repairs, type 1. To not fund the repairs, type 2. However, not repairing the water line"
                                 " will have consequences\n"))
                if decision == '1':
                    if funds >= payAmount:
                        funds -= payAmount
                        print("The water line has been repaired! Public support has increased thanks to your decisive action!")
                        print("Public support has increased by 10%")
                        publicSupport += 10
                        print("Public support is now " + str(publicSupport) + "%")
                        input("You now have $" + greenText(str(funds)) + " left\n")
                        break
                    else:
                        print("You don't have enough funds.")
                        continue
                if decision == 2:
                    print("You have decided not to fund repairs for the water line. The public is outraged!")
                    print("Public support has decreased by 20%")
                    publicSupport -= 20
                    input("Public support is now " + str(publicSupport)+ "%\n")
                    break
                else:
                    print("Input not recognized")
        if y == 3:
            input(boldRedText("DISASTER!\n"))
            input("The town's gas line has " + redText('broke') + ", and many residents now can't heat their homes or cook their food!\n")
            payAmount = 250000
            while 1 == 1:
                decision = str(input("It will cost $" + greenText(str(payAmount)) + " to repair the gas line. To fund the repairs, type 1. To not fund the repairs, type 2. However, not repairing the department"
                                 " will have consequences\n"))
                if decision == '1':
                    if funds >= payAmount:
                        funds -= payAmount
                        print("The gas line has been repaired! Public support has increased thanks to your decisive action!")
                        print("Public support has increased by 10%\n")
                        publicSupport += 10
                        print("Public support is now " + str(publicSupport))
                        input("You now have $" + greenText(str(funds)) + "% left\n")
                        break
                    else:
                        print("You don't have enough funds.")
                        continue
                if decision == '2':
                    print("You have decided not to fund repairs for the gas line. The public is outraged!")
                    print("Public support has decreased by 20%")
                    publicSupport -= 20
                    input("Public support is now " + str(publicSupport) + "%")
                    break
                else:
                    print("Input not recognized")
    else:
        return''
def checkCouncilMission():
    global mission
    global councilOpinion
    if missionAccepted == 1:
        if mission == 'incomeLower':
            if taxIncomeRate <= 10:
                print("You have done what the council has asked, and reduced the income tax rate! The council is pleased.")
                changeCouncilOpinion(1)
                input("Council opinion has increased by 1. It is now " + str(councilOpinion)+ "\n")
                return()
            else:
                print("You have failed to reduce the income tax rate enough! The council is displeased.")
                changeCouncilOpinion(-3)
                input("Council opinion has decreased by 3. It is now " + str(councilOpinion)+ "\n")
                return()
        if mission == 'salesLower':
            if taxSalesRate <= 10:
                print("You have done what the council has asked, and reduced the sales tax rate! The council is pleased.")
                changeCouncilOpinion(1)
                input("Council opinion has increased by 1. It is now " + str(councilOpinion)+ "\n")
                return()
            else:
                print("You have failed to reduce the sales tax rate enough! The council is displeased.")
                changeCouncilOpinion(-3)
                input("Council opinion has decreased by 3. It is now " + str(councilOpinion)+ "\n")
                return()
        if mission == 'businessLower':
            if taxBusinessRate <= 10:
                print("You have done what the council has asked, and reduced the business tax rate! The council is pleased.")
                changeCouncilOpinion(1)
                input("Council opinion has increased by 1. It is now " + str(councilOpinion)+ "\n")
                return()
            else:
                print("You have failed to reduce the business tax rate enough! The council is displeased.")
                changeCouncilOpinion(-3)
                input("Council opinion has decreased by 3. It is now " + str(councilOpinion)+ "\n")
                return()
        if mission == 'propertyLower':
            if taxPropertyRate <= 10:
                print("You have done what the council has asked, and reduced the property tax rate! The council is pleased.")
                changeCouncilOpinion(1)
                input("Council opinion has increased by 1. It is now " + str(councilOpinion)+ "\n")
                return()
            else:
                print("You have failed to reduce the property tax rate enough! The council is displeased.")
                changeCouncilOpinion(-3)
                input("Council opinion has decreased by 3. It is now " + str(councilOpinion)+ "\n")
                return()
        if mission == 'fireFunding':
            if (currentFireState == 'Underfunded' and newFireState == 'Funded') or (currentFireState == 'Funded' and newFireState == 'Well-Funded'):
                print("You have done what the council has asked, and increased the Fire Department's funding level! The council is pleased.\n")
                changeCouncilOpinion(1)
                input("Council opinion has increased by 1. It is now " + str(councilOpinion)+ "\n")
                return()
            else:
                print("You have failed to increase the Fire Department's funding level! The council is displeased.")
                changeCouncilOpinion(-3)
                input("Council opinion has decreased by 3. It is now " + str(councilOpinion)+ "\n")
                return()
        if mission == 'policeFunding':
            if (currentPoliceState == 'Underfunded' and newPoliceState == 'Funded') or (currentPoliceState == 'Funded' and newPoliceState == 'Well-Funded'):
                print("You have done what the council has asked, and increased the Police Department's funding level! The council is pleased.\n")
                changeCouncilOpinion(1)
                input("Council opinion has increased by 1. It is now " + str(councilOpinion)+ "\n")
                return()
            else:
                print("You have failed to increase the Police Department's funding level! The council is displeased.")
                changeCouncilOpinion(-3)
                input("Council opinion has decreased by 3. It is now " + str(councilOpinion)+ "\n")
                return()
        if mission == 'healthFunding':
            if (currentHealthState == 'Underfunded' and newHealthState == 'Funded') or (currentHealthState == 'Funded' and newHealthState == 'Well-Funded'):
                print("You have done what the council has asked, and increased the Health Department's funding level! The council is pleased.\n")
                changeCouncilOpinion(1)
                input("Council opinion has increased by 1. It is now " + str(councilOpinion)+ "\n")
                return()
            else:
                print("You have failed to increase the Health Department's funding level! The council is displeased.")
                changeCouncilOpinion(-3)
                input("Council opinion has decreased by 3. It is now " + str(councilOpinion)+ "\n")
                return()
        if mission == 'educationFunding':
            if (currentEducationState == 'Underfunded' and newEducationState == 'Funded') or (currentEducationState == 'Funded' and newEducationState == 'Well-Funded'):
                print("You have done what the council has asked, and increased the Education Department's funding level! The council is pleased.\n")
                changeCouncilOpinion(1)
                input("Council opinion has increased by 1. It is now " + str(councilOpinion)+ "\n")
                return()
            else:
                print("You have failed to increase the Education Department's funding level! The council is displeased.")
                changeCouncilOpinion(-3)
                input("Council opinion has decreased by 3. It is now " + str(councilOpinion)+ "\n")
                return()
        if mission == 'infrastructureFunding':
            if (currentInfrastructureState == 'Underfunded' and newInfrastructureState == 'Funded') or (currentInfrastructureState == 'Funded' and newInfrastructureState == 'Well-Funded'):
                print("You have done what the council has asked, and increased the Infrastructure Department's funding level! The council is pleased.\n")
                changeCouncilOpinion(1)
                input("Council opinion has increased by 1. It is now " + str(councilOpinion)+ "\n")
                return()
            else:
                print("You have failed to increase the Infrastructure Department's funding level! The council is displeased.")
                changeCouncilOpinion(-3)
                input("Council opinion has decreased by 3. It is now " + str(councilOpinion)+ "\n")
                return()
        if mission == 'recFunding':
            if (currentRecState == 'Underfunded' and newRecState == 'Funded') or (currentRecState == 'Funded' and newRecState == 'Well-Funded'):
                print("You have done what the council has asked, and increased the Parks and Recreation Department's funding level! The council is pleased.\n")
                changeCouncilOpinion(1)
                input("Council opinion has increased by 1. It is now " + str(councilOpinion)+ "\n")
                return()
            else:
                print("You have failed to increase the Parks and Recreation Department's funding level! The council is displeased.")
                changeCouncilOpinion(-3)
                input("Council opinion has decreased by 3. It is now " + str(councilOpinion)+ "\n")
                return()

def doTurn():
    global councilAgenda
    global townAgenda
    global monthCounter
    global yearlyPassedPolicies
    print(giveDate())
    if monthCounter == 0:
        manageBudget()
        yearlyPassedPolicies = []
        if year > 1:
            checkCouncilMission()
        decideCouncilProposal()
    else:
        decideTownProposal()

    if monthCounter == 2:
        disaster()
        TE_CouncilChangesSupport()

    TE_DepartmentFunding()
    TE_debt()
    TE_populationChange()
    nextDate()

def tutorial():
    boldYellowText("Tutorial:")
    input("In the mayor game, your main goal is to keep the " + purpleText('town council') + " and the " + blueText('public') + " happy.")
    print("At the start of each year, you will be able to change the " + greenText('town budget') + ". This means you can change taxes and allocate department funding.")
    print("The " + purpleText('town council') + " will also send you a mission, which you can accept or deny to do.")
    print("Denying or not following through on accepted mission will " + redText('decrease') + " the council's opinion of you, so be careful!")
    input("The " + greenText('public') + " will also ask you to do pay for proposals. Accepting them is a sure way to increase support, but be careful that you have enough funds!")
    input("At the end of your 4-year term, if you have a majority of public support, you " + yellowText('win') + " the game!")
    input("That's all for the tutorial. Enjoy the game!\n")
name = ''

while 1==1:
    name = input("Welcome to the Mayor Game! Before we start, what's your name? Type it below and press the enter key.\n")
    if name != '':
        break
    else:
        print("You didn't enter anything. Type it your name!")
        continue
while 1==1:
    doTutorial = input("Hi " + name + "! To see the tutorial, press 1 and press the enter key. To skip it, press 2.\n")
    if doTutorial == '1':
        tutorial()
        break
    if doTutorial == '2':
        input("Tutorial skipped. Let's start!\n")
        break
    else:
        print("Input not recognized. Please type 1 or 2.")
        continue

win = ''

def theEnd():
    global publicSupport
    global councilOpinion
    global win
    win = 'yes'
    input("Alright " + str(name) + ". It's been 4 years, and " + yellowText('your term is up!') + '\n')
    if publicSupport >= 90:
        input("Congratulations! Thanks to overwhelming public support, you have been " + greenText('reelected in a landslide victory') + '!\n')
    elif publicSupport >= 70:
        input("Congratulations! Thanks to high public support, you have been " + greenText('reelected') + '!\n')
    elif publicSupport >= 50:
        input("Congratulations! With public support high enough, you have been " + greenText('reelected') + '!\n')
    elif publicSupport >= 30:
        input("Oh no! With public support not high enough, you have " + redText("not been reelected")+ '!\n')
        win = 'no'
    else:
        input("Oh no! With overwhelming public opposition, you have " + redText("not been reelected")+ '!\n')
        win = 'no'
    if win == 'yes':
        print("You have " + yellowText('WON') + ' the game! Good job!')
    else:
        print("You have " + redText("LOST") + ' the game! Tough luck!')

def calculateScore():
    global population
    global publicSupport
    global councilOpinion
    global win
    global funds
    boldCyanText("Final Score:")
    print("Population: " + cyanText(str(population)))
    print("Public Support times 20: " + cyanText(str(publicSupport*20)))
    print("Council Opinion times 30: " + cyanText(str(councilOpinion*30)))
    print("Remaining Funds: " + cyanText(str(funds / 1000)))
    if win == 'yes':
        print("Won Game: " + cyanText(str(5000)))
        finScore = 5000
    else:
        print("Lost Game: " + cyanText(str(0)))
        finScore = 0

    councilScore = councilOpinion * 30    
    pubScore = publicSupport*20
    popScore = population
    fundScore = funds/1000
    
    score = councilScore + pubScore + popScore + fundScore + finScore
    print("Final Score: " + cyanText(str(score)))

while year != 5:
    doTurn()
  
theEnd()
calculateScore()
print("To play again, restart the program.\n")