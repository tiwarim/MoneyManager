# Money Manager

## Welcome to your personal money manager

### Are You Really Richer Then You Think?

* This project was created in 12 hours during the Scotiabank sHacks hackathon on August 18th 2018. The theme of the hackathon was to  "gamify" a bank process.
* All we need is your personal financials and our system caters the best mortagage value for you.
The system appraises your net worth after calculating all your past mortgages and your assets.

### Development

#### This project was built using python3

```
from threading import Timer
from tkinter import*
import random
import webbrowser
```

```
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
 ```
## Functionalities
* We used the timer module to create a function which to increase time exponentially. One minute in the game is one year in life.
* We used the tkinter module to a create a pop up window which asks for user's input. 
    ![input info](https://user-images.githubusercontent.com/35289522/44312870-dbbc3280-a3cc-11e8-980b-274fe3014066.PNG)
* After the input of all your personal financials, the pop-up window open to show the functionalities that the app performs.
    ![pop-up](https://user-images.githubusercontent.com/35289522/44312907-79affd00-a3cd-11e8-9995-5197007c51c1.PNG)
* If you click on "Housing" the system shows 3 houses which you can buy within your credentials and also whether you can buy them outright or with a loan.
* If you click "Personal Info" the system shows you how long you've been playing(in my case it's 0 years as 1 minute wasn't completed on the timer). It shows your credentials after you've bought a house, invested something on stocks. It keeps on changing your financial info as you go on buying something in the game. 
    ![input3](https://user-images.githubusercontent.com/35289522/44312968-41f58500-a3ce-11e8-99a9-f93d9f408e6f.PNG)
* If you click on the "stock investment" it will show you some popular stock options and their real time market value. We made use of the web browser functionality of python to connect the web links with our pop-up windows.
    ![stocks](https://user-images.githubusercontent.com/35289522/44313014-b29ca180-a3ce-11e8-8376-ab5e2360b83f.PNG)
* We also built a web link for Scotiabank mortgage calculator. 
    ![mortgage](https://user-images.githubusercontent.com/35289522/44313036-11fab180-a3cf-11e8-8cb8-1d532060e608.PNG)


# ProtoType

### As we only had 12 hours to make our web app, we used [Proto.io](https://proto.io/) for presentation at the end of the day to showcase how we envision our app to like with time and further development. The prototype is interactive and clickable.

**Welcome Screen**

![welcome](https://user-images.githubusercontent.com/35289522/44313064-a533e700-a3cf-11e8-900b-4666c5a203fb.PNG)

**Personal Info Screen** 

![personal info](https://user-images.githubusercontent.com/35289522/44313120-694d5180-a3d0-11e8-8c4a-b50820e54a59.PNG)

**Options Screen**

![options](https://user-images.githubusercontent.com/35289522/44313099-3c993a00-a3d0-11e8-984d-4751e46b3b9a.PNG)

**Houses You Can Buy**

![housing](https://user-images.githubusercontent.com/35289522/44313127-8da92e00-a3d0-11e8-8aa5-068a07223841.PNG)

**Your Personal Info After You've Played The Game For Some Time**

![game](https://user-images.githubusercontent.com/35289522/44313139-c2b58080-a3d0-11e8-8c7e-aa4b2142d9a5.PNG)

**Your Stock Investment File**

![stocks](https://user-images.githubusercontent.com/35289522/44313146-f395b580-a3d0-11e8-8de7-5782620e58bb.PNG)



# Built With Blood, Sweat, Tears and Coffee by 

* **Ather Hassan** Software Engineering McMaster University
* **Sara Abu Hattab** Software Engineering McMaster University
* **Mrinal Tiwari** Software Engineering McMaster University
* **Chitwan Sharma** Computer Science McMaster University

## Further Development

#### Looking forward to complete this project and have a final web app ready with all the functionalitites we envision our app to have.



## Thanks To
* Scotiabank for a great event!
* All the mentors present for helping us out and giving us many ideas!!

