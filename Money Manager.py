
# coding: utf-8

# In[ ]:


from threading import Timer
from tkinter import*
import random
import webbrowser
Years = 0
bankrupt=False
income=-1
expenses=-1
creditScore=-1
debt=-1
netWorth=0
asset=0
money=0
ownedHomes=[]
def main():
    t = Timer(120.0, incrementYear)    
    t.start()
    introScreen()
    mainPage()
    
## adds to the year and changes the value of any assets( assets have to auto update their value)
def incrementYear():
    global Years
    global income
    global exepnses
    global asset
    global ownedHomes
    global money
    Years+=1
    money+=income
    money-=expenses
    if(len(ownedHomes)!=0):
        for i in len(ownedHomes):
            if (ownedHomes[i][2]>0):
                money-=ownedHomes[i][3]
            ownedHomes[i][2]=0.96*ownedHomes[i][2]
            ownedHomes[i][1]=1.05*ownedHomes[i][1]
    asset=asset*1.05
    t = Timer(120.0, incrementYear)    
    t.start()
def updateFinances():
    netWorth=money+asset-debt
def useLink():
    webbrowser.open("https://www.scotiabank.com/mortgage/payment/en/payment.html")

def mainPage():
    main=Tk()
    housing=Button(main,text="Housing",command=createHouses)
    housing.place(relx=0.5,rely=0.1,anchor=CENTER)
    
    personalInfo=Button(main,text="Personal Info",command=getPersonalInfo)
    personalInfo.place(relx=0.5,rely=0.3,anchor=CENTER)
    
    loans=Button(main,text="Loans",command=loanWindow)
    loans.place(relx=0.5,rely=0.5,anchor=CENTER)
    
    webLink=Button(main,text="Click to compare scotiabank \nmortgage to your mortgage!",command=useLink)
    webLink.place(relx=0.5,rely=0.9,anchor=CENTER)
    
    stocks=Button(main,text="Stock Investment",command=showStocks)
    stocks.place(relx=0.5,rely=0.7,anchor=CENTER)
    
    
    mainloop()
def showStocks():
    main=Tk()
    def StarbucksLink():
        webbrowser.open("https://www.google.ca/search?q=NASDAQ:SBUX&e=4112296&tbm=fin&biw=1366&bih=662#scso=uid_Grt4W9e5BcK0jwSwwK24BA_5:0")
        main.destroy()
    def ScotiaBankLink():
        webbrowser.open("https://www.google.ca/search?q=TSE:BNS&e=4112296&tbm=fin&biw=681&bih=642#scso=uid_T8V4W62_FYPjjwT8ga6oDQ_5:0")
        main.destroy()
    def AppleLink():
        webbrowser.open("https://www.google.ca/search?q=NASDAQ:AAPL&e=4112296&tbm=fin&biw=681&bih=642#scso=uid_o8V4W8LiO4HPjwSUjr3QBA_5:0")
        main.destroy()
    starLink=Button(main,text="Click to see Starbucks stock graph",command=StarbucksLink)
    starLink.place(relx=0.5,rely=0.2,anchor=CENTER)
    
    Link1=Button(main,text="Click to see ScotiaBank stock graph",command=ScotiaBankLink)
    Link1.place(relx=0.5,rely=0.5,anchor=CENTER)
    
    Link2=Button(main,text="Click to see Apple stock graph",command=AppleLink)
    Link2.place(relx=0.5,rely=0.8,anchor=CENTER)
    mainloop()

    


#Randomly generate 3 options for housing within the clients gross income level, gives the option to purchase outright or with loan
def createHouses():
    global ownedHomes
    global debt
    global netWorth
    global money
    houses=Tk()
    houses.geometry("500x500")
    updateFinances()
    print(money)
    userRange=int(1.5*netWorth)
    if(userRange>60000):
        
        def loanBuy1():
            global asset
            global debt
            debt+=choice1
            asset+=choice1
            ownedHomes.append(["house",choice1,choice1,0.06*choice1])
            houses.destroy()
        def buy1():
            global asset
            global money
            money-=choice1
            asset+=choice1
            ownedHomes.append(["house",choice1,choice1,0.06*choice1])
            houses.destroy()
        def loanBuy2():
            global asset
            global debt
            debt+=choice2
            asset+=choice2
            ownedHomes.append(["house",choice2,choice2,0.06*choice2])
            houses.destroy()
        def buy2():
            global asset
            global money
            money-=choice2
            asset+=choice2
            ownedHomes.append(["house",choice2,choice2,0.06*choice2])
            houses.destroy()
        def loanBuy3():
            global asset
            global debt
            debt+=choice3
            asset+=choice3
            ownedHomes.append(["house",choice3,choice3,0.06*choice3])
            houses.destroy()
        def buy3():
            global asset
            global money
            money-=choice3
            asset+=choice3
            ownedHomes.append(["house",choice3,choice3,0.06*choice3])
            houses.destroy()
        
        title=Label(houses,text=("Houses in your mortgage range are"))
        title.place(relx=0.5,rely=0.2,anchor=CENTER)
        
        choice1=random.randint(60000,userRange)
        house1=Label(houses,text="house 1 for $"+str(choice1))
        house1.place(relx=0.2,rely=0.4,anchor=CENTER)
        house1Bl=Button(houses,text="buy with loan",command=loanBuy1)
        house1Bl.place(relx=0.2,rely=0.6,anchor=CENTER)
        if(money>=choice1):
            house1B=Button(houses,text="buy outright",command=buy1)
            house1B.place(relx=0.2,rely=0.8,anchor=CENTER)
       
    
        choice2=random.randint(60000,userRange)
        house2=Label(houses,text="house 2 for $"+str(choice2))
        house2.place(relx=0.5,rely=0.4,anchor=CENTER)
        house2Bl=Button(houses,text="buy with loan",command=loanBuy2)
        house2Bl.place(relx=0.5,rely=0.6,anchor=CENTER)
        if(money>=choice2):
            house2B=Button(houses,text="buy outright",command=buy2)
            house2B.place(relx=0.5,rely=0.8,anchor=CENTER)
        
        choice3=random.randint(60000,userRange)
        house3=Label(houses,text="house 3 for $"+str(choice3))
        house3.place(relx=0.8,rely=0.4,anchor=CENTER)
        house3Bl=Button(houses,text="buy with loan",command=loanBuy3)
        house3Bl.place(relx=0.8,rely=0.6,anchor=CENTER)
        if(money>=choice3):
            house3B=Button(houses,text="buy outright",command=buy3)
            house3B.place(relx=0.8,rely=0.8,anchor=CENTER)
        
    else:
        print("level up your range")
def getPersonalInfo():
    updateFinances()
    personal= Tk()
    personal.geometry("1000x1000")
    yearsPlayed=Label(personal,text="Years played "+str(Years))
    yearsPlayed.place(relx= 0.2,rely=0.2,anchor=CENTER)
    
    incomeText=Label(personal,text="Income $"+str(income))
    incomeText.place(relx= 0.4,rely=0.2,anchor=CENTER)
    
    expensesText=Label(personal,text="Expenses $"+str(expenses))
    expensesText.place(relx= 0.6,rely=0.2,anchor=CENTER)
    
    creditScoreText=Label(personal,text="Credit Score "+str(creditScore))
    creditScoreText.place(relx= 0.8,rely=0.2,anchor=CENTER)
    
    debtText=Label(personal,text="Debt $"+str(debt))
    debtText.place(relx= 0.2,rely=0.4,anchor=CENTER)
    
    netWorthText=Label(personal,text="Net Worth $"+str(netWorth))
    netWorthText.place(relx= 0.4,rely=0.4,anchor=CENTER)
    
    assetText=Label(personal,text="Asset value $"+str(asset))
    assetText.place(relx= 0.6,rely=0.4,anchor=CENTER)
    
    ownieHomie=Label(personal,text="Homes Owned "+str(len(ownedHomes)))
    ownieHomie.place(relx= 0.8,rely=0.4,anchor=CENTER)
    
    def sellHouse1():
        money+=ownedHomes[0][1]
        del ownedHomes[0]
    if(len(ownedHomes)>0):
        ownedHome1=Button(personal,text="Sell home #1 \nfor $"+str(ownedHomes[0][1]),command=sellHouse1)
        ownedHome1.place(relx=0.2,rely=0.7,anchor=CENTER)
    def sellHouse2():
        money+=ownedHomes[1][1]
        del ownedHomes[1]
    if(len(ownedHomes)>1):
        ownedHome2=Button(personal,text="Sell home #2 \nfor $"+str(ownedHomes[1][1]),command=sellHouse2)
        ownedHome2.place(relx=0.5,rely=0.7,anchor=CENTER)
    def sellHouse3():
        money+=ownedHomes[2][1]
        del ownedHomes[2]
    if(len(ownedHomes)>2):
        ownedHome3=Button(personal,text="Sell home #3 \nfor $"+str(ownedHomes[2][1]),command=sellHouse3)
        ownedHome3.place(relx=0.8,rely=0.7,anchor=CENTER)
    
    
        
        
def loanWindow():
    print("no owe")
def introScreen():
    
    def getInfo():
        global infoButton
        global income
        global netWorth
        global money
        while(income<0):
            try:
                income = int(input('Enter your gross income: '))
            except ValueError:
                print( "Please input a number dawgg")
                income = int(input('Enter your gross income: '))    
        global expenses        
        while(expenses<0):
            try:
                expenses = int(input('Enter your yearly expenses: '))
            except ValueError:
                print( "Please input a number dawgg")
                expenses = int(input('Enter your yearly expenses: '))
        global debt     
        while(debt<0):
            try:
                debt = int(input('Enter any debts you have: '))
            except ValueError:
                print( "Please input a number dawgg")  
                debt = int(input('Enter any debts you have: '))     
        global creditScore        
        while(creditScore<0):
            try:
                creditScore = int(input('Enter your credit score: '))
            except ValueError:
                 print( "Please input a number dawgg")  
                 creditScore = int(input('Enter your credit score: '))
        money=income
        netWorth=money+asset-debt
        intro.destroy()

    intro=Tk()
    infoButton=Button(intro,text="Input Info",command=getInfo)
    infoButton.place(relx=0.5,rely=0.5,anchor=CENTER)
    mainloop()
    
main()

