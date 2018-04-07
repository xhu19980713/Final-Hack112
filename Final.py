
import os
import pygame

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\Users\\Diane_HU\\Desktop\\API_Credential.json'


            

class PygameGame(object):
   
    # Helpers
    # Init functions
    def initColor(self):
        self.white = (255,255,255)
        self.black= (0,0,0)

        #self.deepBlue= (68,118,192)
        #self.darkBlue  = (51,87,117)
        self.grey=(99,99,112)
        self.orange=(222,141,71)
        
        self.blueGray = self.hex_to_rgb("#343f51")
        self.deepBlueGray = self.hex_to_rgb("#2e3242")
        self.darkBlueGray = self.hex_to_rgb("#1b2331")
        
        self.lightOrange=(240,190,98)
        self.orange = (255,135,0)  #normal
        self.darkOrange = (221,111,15)   #motion
        self.deepOrange = self.hex_to_rgb("#c16112") #pressed
    
    def within(self,left,down,width,height,x,y):
        return left < x < left+width and down < y < down +height

    def hex_to_rgb(self,value):
        """Return (red, green, blue) for the color given as #rrggbb."""
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
        
    def loadFont(self):
        self.regularFont = pygame.font.SysFont("Arvo-Bold.ttf",35)
        self.topicFont=pygame.font.SysFont("Arvo-Bold.ttf",60)
        self.buttonFont = pygame.font.SysFont("Arvo-Bold.ttf",30)
        self.calendarFont=pygame.font.SysFont("Arvo-Bold.ttf",25)
        self.weekFont=pygame.font.SysFont("Arvo-Bold.ttf",20)
        self.cuteFont = pygame.font.SysFont("EastSeaDokdo-Regular.ttf",30)

#############################
#all button
#############################

    def signButtons(self):
        width= 300
        height = 40
        gap = 20
        self.signInBtn = [118,475,width,height, self.orange] 
        self.signUpBtn = [118,475+gap+height,width,height,self.orange] 

    def interestButtons(self):
        gap=10
        btnHeight=35
        self.interestButtonList=[]
        for i in range(0,len(self.interestList)):
            lenText=len(self.interestList[i])
            self.interestButtonList+=InterestBox(43,30+btnHeight*i+gap*i,\
                                                lenText*10+20,btnHeight,\
                                                self.interestList[i])
                                                
    def mainButtons(self):
        width=150
        gap=20
        self.mainEvent1=[43,140,450,width,self.white]
        self.mainEvent2=[43,140+width+gap,450,width,self.white]
        self.mainEvent3=[43,140+width*2+gap*2,450,width,self.white]
        self.mainCircle=[self.orange,218,779,70]
        self.mainCommunityBtn=[0,739,188,80,self.orange]
        self.mainCalendarBtn=[348,739,241,80,self.orange]
        
        
    def handButtons(self):
        self.titleInput()
        self.dateInput()
        self.beginTimeInput()
        self.endTimeInput()
        self.locationInput()
        self.descriptionInput()
        
    
    def buttons(self):
        self.interestInput()
        self.signButtons()
        self.interestButtons()
        self.mainButtons()
        self.handButtons()
        self.importButtons=[self.orange,(268,500),200]
        self.friendEventBtn=[118,100,300,200,self.orange]
        self.localEventBtn=[118,350,300,200,self.orange]
        self.preferenceBtn=[118,475,300,40,self.orange]
        self.handCircle=[self.orange,(160,679),40]
        self.libraryInputCircle=[self.orange,(268,639),40]
        self.cameraCircle=[self.orange,(376,679),40]
    
      
##############################
#text input boxes
##############################
    def interestInput(self):
        #text input box at interest input page
        self.interestList=[]
        self.interestInput=""
        boxWidth=450
        boxHeight=35
        self.interestInputBox=[43,150,boxWidth,boxHeight,self.orange]
        
    def titleInput(self):
        self.titleText=""
        boxWidth=450
        boxHeight=35
        self.titleInputBox=[43,150,boxWidth,boxHeight,self.orange]
        
    def dateInput(self):
        self.dateText=""
        boxWidth=200
        boxHeight=35
        self.dateInputBox=[43,245,boxWidth,boxHeight,self.orange]
        
    def beginTimeInput(self):
        self.beginTimeText=""
        boxWidth=100
        boxHeight=35
        self.beginTimeInputBox=[43,340,boxWidth,boxHeight,self.orange]
    
    def endTimeInput(self):
        self.endTimeText=""
        boxWidth=100
        boxHeight=35
        self.endTimeInputBox=[158,340,boxWidth,boxHeight,self.orange]
    
    def locationInput(self):
        self.locationText=""
        boxWidth=200
        boxHeight=35
        self.locationInputBox=[43,435,boxWidth,boxHeight,self.orange]

#########################
### Main Framework ######
#########################
    def init(self):
        self.mode = "sign"
        self.currentPos=(-1,-1)
        self.initColor()
        self.signButtons()
        self.loadFont()
        self.w = 0
        self.h1 = 0
        self.h2 = 0
        self.h3 = 0
        self.h4 = 0
        self.h5 = 0
        self.num = 0
        self.calendarColor = []
        for row in range(5): self.calendarColor += [[1]*7]
        #14 modes 
        self.modeLst=["sign","interest","main","hand","libraryInput","camera"\
                      "calendar","working","finish","calendarYes","calendarNo",\
                      "calendarMarch","calendarMay","community"\
                      "communityFriends","threeIcon"]
        self.path = None
        self.buttons()
        self.week = ['Sun','Mon','Tus','Wed','Thr','Fri','Sat']
        self.day = []
        for row in range(5): self.day += [[0]*7]
        self.userImg = pygame.image.load('orange.png')
        self.instaImg = pygame.image.load('instagram.png')
        self.snapImg = pygame.image.load('snapchat1.png')
        self.fbImg = pygame.image.load('fb1.png')
        self.oImg = pygame.image.load('o.png')
        self.friendImg = pygame.image.load('login1.png')
        self.messageImg = pygame.image.load('bubble.png')
        self.backImg = pygame.image.load('back4.png')
        self.addImg = pygame.image.load('add3.png')
        self.doneImg = pygame.image.load('done2.png')
        self.mannualImg = pygame.image.load('manual2.png')
        self.searImg = pygame.image.load('search1.png')
        self.setImg = pygame.image.load('set2.png')
        self.calImg = pygame.image.load('calendar1.png')
        self.comImg = pygame.image.load('community1.png')
        self.camImg = pygame.image.load('camera2.png')
        self.libImg = pygame.image.load('lib1.png')
        self.info=[]
        self.numList=[]
        self.handInput=[self.titleText,self.dateInput,self.beginTimeText,self.endTimeText,self.locationText]
        
        
        #self.loadLogo()  xh
        #self.loadShareLogo() xh

#### MousePressed ####
    def mousePressedSign(self,x,y):
        if self.mode=="sign":
            #signInBtn
            surface= self.signInBtn
            if self.within(surface[0],surface[1],surface[2],surface[3],x,y):
                surface[4]=self.deepOrange
            #signUpBtn
            surface=self.signUpBtn
            if self.within(surface[0],surface[1],surface[2],surface[3],x,y):
                surface[4]=self.deepOrange
                
    def mousePressedMain(self,x,y):
        if self.mode=="main":
            if (x-268)**2+(y-779)**2<=6400 and y<819:
                self.mainCircle[0]=self.deepOrange
            btn=self.mainCommunityBtn
            if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                btn[4]=self.deepOrange
            btn=self.mainCalendarBtn
            if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                btn[4]=self.deepOrange
                
    def mousePressedThreeIcon(self,x,y):
        if self.mode=="threeIcon":
            if (x-160)**2+(y-679)**2<=1600:
                self.handCircle[0]=self.deepOrange
            
            if (x-268)**2+(y-639)**2<=1600:
                self.libraryInputCircle[0]=self.deepOrange
                
            if (x-376)**2+(y-679)**2<=1600:
                self.cameraCircle[0]=self.deepOrange
            
            if (x-268)**2+(y-779)**2 <=6400 and y < 819:
                self.mainCircle[0]=self.deepOrange
                
    def mousePressedLibraryInput(self,x,y):
        if self.mode=="libraryInput":
            surface=self.importButtons
            if (x-268)**2+(y-500)**2<=200**2:
                surface[1]=self.deepOrange
     
    def mousePressedCommunity(self,x,y):
        if self.mode=="community":
            surface=self.friendEventBtn
            if self.within(surface[0],surface[1],surface[2],surface[3],x,y):
                surface[4]=self.deepOrange
            
            surface=self.localEventBtn
            if self.within(surface[0],surface[1],surface[2],surface[3],x,y):
                surface[4]=self.deepOrange
            


#### Open File Browser ####
    def open_file_browser(self):
        pygame.mixer.init()  # initializing the mixer
        import tkinter
        from tkinter import filedialog

        root = tkinter.Tk()
        root.withdraw()
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        return root.filename

#### MouseReleased ####
    def mouseReleasedSign(self,x,y):
        if self.mode=="sign":
            #signInBtn
            surface= self.signInBtn
            if self.within(surface[0],surface[1],surface[2],surface[3],x,y):
                surface[4]=self.orange
                self.mode="main"
            #signUpBtn
            surface=self.signUpBtn
            if self.within(surface[0],surface[1],surface[2],surface[3],x,y):
                surface[4]=self.orange
                self.mode="interest"
                
    def mouseReleasedThreeIcon(self,x,y):
        if self.mode=="threeIcon":
            if (x-268)**2+(y-779)**2 <=6400 and y < 819:
                self.mode = "main"
                print("jgso")
                self.mainCircle[0]=self.orange
                
            elif (x-160)**2+(y-679)**2<=1600:
                self.handCircle[0]=self.orange
                self.mode="hand"
            
            elif (x-268)**2+(y-639)**2<=1600:
                self.libraryInputCircle[0]=self.orange
                self.mode="libraryInput"
                
            elif (x-376)**2+(y-679)**2<=1600:
                self.cameraCircle[0]=self.orange


    def mouseReleasedMain(self,x,y):
        if self.mode=="main":
            if (x-268)**2+(y-779)**2<=6400 and y<819:
                self.mainCircle[0]=self.orange
                self.mode="threeIcon"
            
            btn=self.mainCommunityBtn
            if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                btn[4]=self.orange
                self.mode="community"
                
            btn=self.mainCalendarBtn
            if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                btn[4]=self.orange
                self.mode="calendar"

            
    def mousePressCalendar(self,x,y):
        if self.mode=="calendar":
            for i in range(5):
                for j in range(7):
                    if self.within(260-223,40+100-20,100,100,x,y):
                        self.mode = "calendarMarch"
                    elif self.within(720-223-50,40+100-20,100,100,x,y):
                        self.mode = "calendarMay"

    def mousePressedCalendarMarch(self,x,y):
        if self.mode == "calendarMarch":
            if self.within(720-223-50,40+100-20,100,100,x,y):
                self.mode = "calendar"

    def mousePressedCalendarMay(self,x,y):
        if self.mode == "calendarMay":
            if self.within(260-223,40+100-20,100,100,x,y):
                self.mode = "calendar"

    def mousePressedOrange(self,x,y):
        if self.mode == "working":
            if self.within(30,600,30+90,600+90,x,y):
                self.num = 1
            elif self.within(130,600,90,90,x,y):
                self.num = 2
            elif self.within(230,600,90,90,x,y):
                self.num = 3
            elif self.within(330,600,90,90,x,y):
                print("here")
                self.num = 4
            elif self.within(430,600,90,90,x,y):
                self.num = 5

    def mousePressed(self,x,y):
        self.mousePressedSign(x,y)
        self.mousePressedLibraryInput(x,y)
        self.mousePressCalendar(x,y)
        self.mousePressedCalendarMarch(x,y)
        self.mousePressedCalendarMay(x,y)
        self.mousePressedCommunity(x,y)
        self.mousePressedPreference(x,y)
        self.mousePressedThreeIcon(x,y)
        self.mousePressedOrange(x,y)
        self.mousePressedMain(x,y)

    def mouseReleasedLibraryInput(self,x,y):
        if self.mode=="libraryInput":
            surface=self.importButtons
            if (x-268)**2+(y-500)**2<=200**2:
                surface[1]=self.orange
                self.path=self.open_file_browser()
                if self.path!="":
                    self.mode="working"
    
    def mouseReleasedBack(self,x,y):
        if self.within(0,0,60,45,x,y):
            if self.mode=="interest":
                self.mode="sign"
            elif self.mode=="libraryInput":
                self.mode="main"
            elif self.mode=="camera":
                self.mode="main"
            elif self.mode=="hand":
                self.mode="main"
            elif self.mode=="community":
                self.mode="main"
            elif self.mode=="calendar":
                self.mode="main"
            elif self.mode=="calendarYes":
                self.mode="calendar"
            elif self.mode=="calendarNo":
                self.mode="calendar"
            elif self.mode=="finish":
                self.mode="libraryInput"
            elif self.mode=="communityFriends":
                self.mode="community"
                
    def mouseReleasedDone(self,x,y):
        if self.within(536-60,0,60,45,x,y):
            if self.mode=="finish":
                self.mode="main"
            elif self.mode=="hand":
                self.mode="main"
            elif self.mode=="interest":
                self.mode="main"
                
    
    def mouseReleasedCommunity(self,x,y):
       if self.mode=="community":
            surface=self.friendEventBtn
            if self.within(surface[0],surface[1],surface[2],surface[3],x,y):
                surface[4]=self.orange
                self.mode="communityFriends"
                
            surface=self.localEventBtn
            if self.within(surface[0],surface[1],surface[2],surface[3],x,y):
                surface[4]=self.orange
   
    def mouseReleasedCalendar(self,x,y):
        if self.mode == "calendar":
            for i in range(5):
                for j in range(7):
                    if self.day[i][j] == 0:
                        if self.within(250 + j *70-223, 130 + i * 70+100, 60, 60,x,y):
                            self.mode = "calendarNo"
                    elif self.day[i][j] >= 1:
                        if self.within(250 + j *70-223, 130 + i * 70+100, 60, 60,x,y):
                            self.mode = "calendarYes"

    def mouseReleased(self,x,y):
        self.mouseReleasedSign(x,y)
        self.mouseReleasedCalendar(x,y)
        self.mouseReleasedLibraryInput(x,y)
        self.mouseReleasedBack(x,y)
        self.mouseReleasedDone(x,y)
        self.mouseReleasedPreference(x,y)
        self.mouseReleasedThreeIcon(x,y)
        self.mouseReleasedMain(x,y)
        self.mouseReleasedCommunity(x,y)
        print(self.mode)
        
#### MouseMotion ####
    def mouseMotionSign(self,x,y):
        if self.mode=="sign":
            btn=self.signInBtn
            if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                btn[4]=self.darkOrange
            else:
                btn[4]=self.orange 
            btn=self.signUpBtn
            if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                btn[4]=self.darkOrange
            else:
                btn[4]=self.orange
            

    def mouseMotionInterest(self,x,y):
        if self.mode=="interest":
            if len(self.interestButtonList)!=0:
                for btn in self.interestButtonList:
                    if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                        btn[4]=self.darkOrange
                    else:
                        btn[4]=self.orange 
                
    def mouseMotionMain(self,x,y):
        if self.mode=="main":
            for btn in [self.mainEvent1,self.mainEvent2,self.mainEvent3]:
                if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                    btn[4]=self.darkOrange
                else:
                    btn[4]=self.orange 
        
            if (x-268)**2+(y-779)**2<=6400 and y<819:
                self.mainCircle[0]=self.darkOrange
            else:
                self.mainCircle[0]=self.orange
            
            btn=self.mainCommunityBtn
            if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                btn[4]=self.darkOrange
            else:
                btn[4]=self.orange
            
            btn=self.mainCalendarBtn
            if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                btn[4]=self.darkOrange
            else:
                btn[4]=self.orange
            
    def mouseMotionThreeIcon(self,x,y):
        if self.mode=="threeIcon":
            if (x-160)**2+(y-679)**2<=1600:
                self.handCircle[0]=self.darkOrange
            else:
                self.handCircle[0]=self.orange
            
            if (x-268)**2+(y-639)**2<=1600:
                self.libraryInputCircle[0]=self.darkOrange
            else:
                self.libraryInputCircle[0]=self.orange
                
            if (x-376)**2+(y-679)**2<=1600:
                self.cameraCircle[0]=self.darkOrange
            else:
                self.cameraCircle[0]=self.orange
                
            if (x-268)**2+(y-779)**2<=6400 and y<819:
                self.mainCircle[0]=self.darkOrange
            else:
                self.mainCircle[0]=self.orange
                
    def mouseMotionLibraryInput(self,x,y):
        if self.mode=="libraryInput":
            surface=self.importButtons
            if (x-268)**2+(y-500)**2<=200**2:
                surface[1]=self.darkOrange
            else:
                surface[1]=self.orange
    
    # def mouseMotionFinish(self,x,y):
    #     if self.mode=="finish":
            
    def mouseMotionCommunity(self,x,y):
        if self.mode=="community":
            btn=self.friendEventBtn
            if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                btn[4]=self.darkOrange
            else:
                btn[4]=self.orange 
                
            btn=self.localEventBtn
            if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                btn[4]=self.darkOrange
            else:
                btn[4]=self.orange 
        
    def mouseMotionCalendar(self,x,y):
        if self.mode=="calendar":
            for i in range(5):
                for j in range(7):
                    if self.within(250 + j *70-223, 130 + i * 70+100, 60, 60,x,y):
                        self.calendarColor[i][j] = 1
                    else:
                        self.calendarColor[i][j] = 0
            
    def mouseMotionPreference(self,x,y):
        if self.mode=="preference":
            btn=self.preferenceBtn
            if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
                btn[4]=self.darkOrange
            else:
                btn[4]=self.orange 

    def mouseMotion(self, x, y):
        self.mouseMotionSign(x,y)
        self.mouseMotionInterest(x,y)
        self.mouseMotionMain(x,y)
        self.mouseMotionLibraryInput(x,y)
        self.mouseMotionCommunity(x,y)
        self.mouseMotionCalendar(x,y)
        self.mouseMotionPreference(x,y)
        self.mouseMotionThreeIcon(x,y)

    def keyPressed(self, keyCode, modifier,pos):
        x=pos[0]
        y=pos[1]
        if self.mode=="hand":
            if 97<=keyCode<=122:
                addText=chr(keyCode-32)
            else:
                addText=chr(keyCode)
            if 43<=x<=43+450 and 150<=y<=150+35:
                if keyCode==127:
                    self.titleText=self.titleText[:-1]
                else:
                    self.titleInputBox[4]=self.darkOrange
                    self.titleText+=addText
            else:
                 self.dateInputBox[4]=self.orange
                 
            if 43<=x<=43+200 and 245<= y <=245+35:
                if keyCode==127:
                    self.dateText=self.dateText[:-1]
                else:
                    self.dateInputBox[4]=self.darkOrange
                    self.dateText+=addText
            else:
                self.dateInputBox[4]=self.orange
        
            if 43<=x<=43+100 and 340<= y <=340+35:
                if keyCode==127:
                    self.beginTimeText=self.beginTimeText[:-1]
                else:
                    self.beginTimeInputBox[4]=self.darkOrange
                    self.beginTimeText+=addText
            else:
                self.beginTimeInputBox[4]=self.orange
                
            if  158<=x<=158+100 and 340<=y<=340+35:
                if keyCode==127:
                    self.endTimeText=self.endTimeText[:-1]
                else:
                    self.endTimeInputBox[4]=self.darkOrange
                    self.endTimeText+=addText
            else:
                self.endTimeInputBox[4]=self.orange
                
            if 43<=x<=43+200 and 435<=y<=435+35:
                if keyCode==127:
                    self.locationText=self.locationText[:-1]
                else:
                    self.locationInputBox[4]=self.darkOrange
                    self.locationText+=addText
            else:
                self.locationInputBox[4]=self.orange
        if self.mode=="interest":
            if 43<=x<=43+450 and 150<=y<=150+35:
                if 97<=keyCode<=122:
                    addText=chr(keyCode-32)
                else:
                    addText=chr(keyCode)
                if keyCode !=13:
                    if keyCode==127:
                        self.interestInput=self.interestInput[:-1]
                    else:
                        self.interestInputBox[4]=self.darkOrange
                        self.interestInput+=addText
                else:
                    self.interestList+=[self.interestInput]
                    self.interestInput=""
    def getInterestList(self):
        return self.interestList
                
    def drawInputBox(self,screen):
        list=[self.titleInputBox,self.dateInputBox,self.beginTimeInputBox,self.endTimeInputBox,self.locationInputBox]
        for surface in list:
            pygame.draw.rect(screen,surface[4],surface[:4])
           
    def drawInputBoxText(self,screen):
        self.displayTextAlignLeft(screen,self.titleText,43,150,\
                                self.black,self.regularFont)
        self.displayTextAlignLeft(screen,self.dateText,43,245,self.black,self.regularFont)
        self.displayTextAlignLeft(screen,self.beginTimeText,43,340,self.black,self.regularFont)
        self.displayTextAlignLeft(screen,self.endTimeText,158,340,self.black,self.regularFont)
        self.displayTextAlignLeft(screen,self.locationText,43,435,self.black,self.regularFont)
        
    def drawInterestInput(self,screen):
        pygame.draw.rect(screen,self.interestInputBox[4],self.interestInputBox[:4])
        self.displayTextAlignLeft(screen,self.interestInput,43,150,self.black,self.regularFont)
        
    def keyReleased(self, keyCode, modifier):
        pass
        
        


#### timerFried ####

    def timerFired(self, dt):
        if self.mode == "working":
            self.orangeTimerFired(dt)
            self.loadTimerFired(dt)
    
    def orangeTimerFired(self,dt):
        if self.num == 1:
            if self.h1 > -100:
                self.h1 -= 10
            elif 0 > self.h1:
                self.h1 += 30

        elif self.num == 2:
            if self.h2 < 100:
                self.h2 += 10
            elif 0 < self.h2:
                self.h2 -= 30

        elif self.num == 3:
            if self.h3 < 100:
                self.h3 += 10
            elif 0 < self.h3:
                self.h3 -= 30

        elif self.num == 4:
            if self.h4 > -100:
                self.h4 -= 10
            elif 0 > self.h4:
                self.h4 += 30

        elif self.num == 5:
            if self.h5 < 100:
                self.h5 += 10
            elif 0 < self.h5:
                self.h5 -= 30

        
    def loadTimerFired(self,dt):
            if self.w < 350:
                self.w += 1
            if self.w == 350:
                self.mode = "finish"
        
###########################
#draw
###########################
    def drawSignButtons(self,screen):
        pygame.draw.rect(screen, self.signInBtn[4], self.signInBtn[:4])
        pygame.draw.rect(screen, self.signUpBtn[4], self.signUpBtn[:4])
        self.displayText(screen,"Sign In",118,475,300,40,self.grey,self.regularFont)
        self.displayText(screen,"Log In", 118,535,300,40,self.grey,self.regularFont)
        
    #change
    def drawSign(self,screen):
        screen.fill(self.grey)
        screen.blit(self.userImg,(80,70))
        screen.blit(self.fbImg,(125,630))
        screen.blit(self.instaImg,(235.3,630))
        screen.blit(self.snapImg,(344,630))

    def drawBackBtn(self,screen):
        screen.blit(self.backImg,(0,0))
        
    def drawAddBtn(self,screen):
        screen.blit(self.addImg, (546,0))
        
    def drawDoneBtn(self,screen):
        screen.blit(self.doneImg, (546,0))
        
        
    # change
    def drawSearchBtn(self,screen,loc):
        screen.blit(self.searImg, loc)
        
    # change
    def drawSettingBtn(self,screen):
        screen.blit(self.setImg, (450,0))
        
    # change
    def drawCalBtn(self,screen):
        screen.blit(self.calImg, (268+50+80,10+739))
        
    # change
    def drawComBtn(self,screen):
        screen.blit(self.comImg, (50+20,739))
    # add
    def drawEventBtn(self,screen,color,loc):
        pygame.draw.rect(screen,color,loc)
        
    def drawText(self,text,screen,a,b,c,d):
        self.displayText(screen,"Title: "+text[0],a,b,c,d,self.white,self.regularFont)
        self.displayText(screen,"Date: "+text[1],a,b,c,d+50,self.white,self.regularFont)
        self.displayText(screen,"Time: "+text[2],a,b,c,d+100,self.white,self.regularFont)
        self.displayText(screen,"Loc: "+text[3],a,b,c,d+150,self.white,self.regularFont)
        
    
        
    def drawMainBtn(self,screen):
        pygame.draw.rect(screen,self.mainCommunityBtn[4],(0,739,268,80))
        pygame.draw.rect(screen,self.mainCalendarBtn[4],(268,739,268,80))
        pygame.draw.circle(screen,self.mainCircle[0],(268,779),80)

    def drawSubpage(self,screen):
        screen.fill(self.grey)
        self.drawShades(screen,self.white,0,0,self.width,45)
        screen.blit(self.backImg,(10,0))
    
        
    def drawShades(self, screen, color, a, b, c, d):
            pygame.draw.rect(screen,(160,160,160),(a-7,b-7,c+14,d+14))
            pygame.draw.rect(screen,(170,170,170),(a-6,b-6,c+12,d+12))
            pygame.draw.rect(screen,(190,190,190),(a-5,b-5,c+10,d+10))
            pygame.draw.rect(screen,(210,210,210),(a-4,b-4,c+8,d+8))
            pygame.draw.rect(screen,(230,230,230),(a-3,b-3,c+6,d+6))
            pygame.draw.rect(screen,(240,240,240),(a-2,b-2,c+4,d+4))
            pygame.draw.rect(screen,(250,250,250),(a-1,b-1,c+2,d+2))
            pygame.draw.rect(screen, color, (a,b,c,d))
            
    def drawCalendarButton(self,screen,color, fontColor, a, b, c, d, text,font, width = 0):
            pygame.draw.rect(screen, color, (a,b,c,d), width)
            myFont = font
            textSurface = myFont.render(text, True, fontColor)
            textRect1 = textSurface.get_rect()
            textRect1.center = (a + c/2, b + d/2)
            screen.blit(textSurface, textRect1)
                
    def drawLeftRightButton(self,screen, color, loc):
        pygame.draw.polygon(screen, color, loc)
    
    def calendarMarch(self,screen):
        self.drawSubpage(screen)
        x = -223
        y = 100
        self.drawCalendarButton(screen,self.grey, self.orange, 250+x, 10+y, 480, 50, "March, 2018",self.regularFont)
        self.drawLeftRightButton(screen,self.orange,((260+x,55+y-20),(290+x,40+y-20),(290+x,70+y-20)))
        self.drawLeftRightButton(screen,self.orange,((720+x,55+y-20),(690+x,40+y-20),(690+x,70+y-20)))
        for i in range(7):
            self.drawCalendarButton(screen,self.grey,self.white,250 + i * 70+x, 90+y, 60, 30, self.week[i], self.weekFont)
            day = 29
            for i in range(5):
                for j in range(7):
                    if i == 0 and j < 4: continue
                    if i ==0 and j == 4:
                        day = 1
                    self.drawCalendarButton(screen,self.grey, self.orange, 250 + j *70+x, 130 + i * 70+y, 60, 60, str(day), self.calendarFont)
                    day += 1
        screen.blit(self.oImg, (80,700))
    
    def calendarApril(self,screen):
        
        self.drawSubpage(screen)
        x = -223
        y = 100
        self.drawCalendarButton(screen,self.grey, self.orange, 250+x, 10+y, 480, 50, "April, 2018",self.regularFont)
        self.drawLeftRightButton(screen,self.orange,((260+x,55+y-20),(290+x,40+y-20),(290+x,70+y-20)))
        self.drawLeftRightButton(screen,self.orange,((720+x,55+y-20),(690+x,40+y-20),(690+x,70+y-20)))
        for i in range(7):
            self.drawCalendarButton(screen,self.grey,self.white,250 + i * 70+x, 90+y, 60, 30,self.week[i], self.weekFont)
    
            day = 29
            for i in range(5):
                for j in range(7):
                    if i == 4 and j > 2: continue
                    if i ==0 and j == 0:
                        day = 1
                    if self.calendarColor[i][j] == 0 :
                        self.drawCalendarButton(screen,self.grey, self.orange, 250 + j *70+x, 130 + i * 70+y, 60, 60, str(day), self.calendarFont)
                    elif self.calendarColor[i][j] == 1:
                        self.drawCalendarButton(screen,self.grey, self.white, 250 + j *70+x, 130 + i * 70+y, 60, 60, str(day), self.calendarFont)
                    day = day + 1
        screen.blit(self.oImg, (80,700))
    
                #if recordMode == 11:
                #  pygame.draw.rect(screen, orange, (250+x, 90+y,480 ,380))
                #  myfont = pygame.font.SysFont('Comic Sans MS', 30)
                #  textSurface = myFont.render("Date: Nov." + str(self.recordMode) + 'th', True, grey)
                #  textRect1 = textSurface.get_rect()
                #  textRect1.midleft = (300+x, 150+y)
                #  screen.blit(textSurface, textRect1)
                #  #Good
    
                #  myfont = pygame.font.SysFont('Comic Sans MS', 30)
                #  textSurface1 = myFont1.render("Condition : " + "Fair", True, grey)
                #  textRect2 = textSurface1.get_rect()
                #  textRect2.midleft = (300+x, 200+y)
                #  screen.blit(textSurface1, textRect2)
    
    def calendarMay(self,screen):
        self.drawSubpage(screen)
        x = -223
        y = 100
        self.drawCalendarButton(screen,self.grey, self.orange, 250+x, 10+y, 480, 50, "May, 2018", self.regularFont)
        self.drawLeftRightButton(screen,self.orange,((260+x,55+y-20),(290+x,40+y-20),(290+x,70+y-20)))
        self.drawLeftRightButton(screen,self.orange,((720+x,55+y-20),(690+x,40+y-20),(690+x,70+y-20)))
        for i in range(7):
            self.drawCalendarButton(screen,self.grey,self.white,250 + i * 70+x, 90+y, 60, 30, self.week[i], self.weekFont)
    
            day = 29
            for i in range(5):
                for j in range(7):
                    if i == 0 and j < 2 or i == 4 and j > 4: continue
                    if i ==0 and j == 2:
                        day = 1
                    self.drawCalendarButton(screen,self.grey, self.orange, 250 + j *70+x, 130 + i * 70+y, 60, 60, str(day), self.calendarFont)
                    day = day + 1
        screen.blit(self.oImg, (80,700))
        
        
    def drawCommunityFriends(self,screen):
        self.drawSubpage(screen)
        screen.blit(self.friendImg,(20,180))
        screen.blit(self.friendImg,(20,380))
        screen.blit(self.friendImg,(20,580))
        screen.blit(self.messageImg, (140,150))
        screen.blit(self.messageImg, (140,350))
        screen.blit(self.messageImg, (140,550))
        
    def calendarYes(self,screen):
        self.drawSubpage(screen)
        x = -223
        y = 150
        yw = 0
        for i in range(7):
            self.drawCalendarButton(screen,self.grey,self.orange,250 + i * 70+x, 90+yw, 60, 30, self.week[i], self.weekFont)
        self.drawCalendarButton(screen,self.grey, self.orange, 250+x, 10+y, 480, 50,"April 27, 2018", self.regularFont)
        self.drawLeftRightButton(screen,self.orange,((260+x,55+y-20),(290+x,40+y-20),(290+x,70+y-20)))
        self.drawLeftRightButton(screen,self.orange,((720+x,55+y-20),(690+x,40+y-20),(690+x,70+y-20)))
        
    def calendarNo(self,screen):
        self.drawSubpage(screen)
        x = -223
        y = 150
        yw = 0
        for i in range(7):
            self.drawCalendarButton(screen,self.grey,self.orange,250 + i * 70+x, 90+yw, 60, 30, self.week[i], self.weekFont)
        self.drawCalendarButton(screen,self.grey, self.orange, 250+x, 10+y, 480, 50,"April 11, 2018", self.regularFont)
        self.drawLeftRightButton(screen,self.orange,((260+x,55+y-20),(290+x,40+y-20),(290+x,70+y-20)))
        self.drawLeftRightButton(screen,self.orange,((720+x,55+y-20),(690+x,40+y-20),(690+x,70+y-20)))
        screen.blit(self.oImg,(170, 500))
        self.displayText(screen,'"An Orange A Day',20,150,500,500,self.orange,self.cuteFont)
        self.displayText(screen,'   Keeps Doctors Away"',20,220,500,500,self.black,self.cuteFont)
        
    def displayText(self,screen,text,a,b,c,d,fontColor,font):
        myFont = font
        textSurface = myFont.render(text, True, fontColor)
        textRect1 = textSurface.get_rect()
        textRect1.center = (a + c/2, b + d/2)
        screen.blit(textSurface, textRect1)
        
    def displayTextAlignLeft(self,screen,text,a,b,fontColor,font):
        print(self.interestList)
        textSurface=font.render(text,True,fontColor)
        textRect1=textSurface.get_rect()
        screen.blit(textSurface,(a,b+5))
        
    def drawThreeIcon(self,screen):
        pygame.draw.circle(screen,self.handCircle[0],(160,679),40)
        screen.blit(self.mannualImg,(160-20,679-20))
        pygame.draw.circle(screen,self.libraryInputCircle[0],(268,639),40)
        screen.blit(self.libImg,(268-20,639-20))
        pygame.draw.circle(screen,self.cameraCircle[0],(376,679),40)
        screen.blit(self.camImg,(376-20,679-20))

    def drawOrangeBtn(self,screen,loc):
        screen.blit(self.oImg,loc)
        
    def drawInterestBar(self,screen):
        if len(self.interestList)==0:
            pass
        else:
            for i in range(0,len(self.interestList)):
                box=(43,250+20*i+35*i,len(self.interestList[i])*20,35)
                pygame.draw.rect(screen,self.orange,box)
                self.displayText(screen,self.interestList[i],43,250+20*i+35*i,len(self.interestList[i])*20,35,self.black,self.regularFont)
                
                
######### get event #####
    def extractInfo(self):
        if self.mode == 'working':
            if self.numlist[0] == 1:
                self.info.append(getTextOne(self.path))
            elif self.numlist[0] == 2:
                infoDic = interestFilterTwo(self.path)
                if isinstance(infoDic,list):
                    self.info += infoDic
                elif isinstance(infoDic,dict):
                    self.info += [infoDic]
            elif self.numlist[0] == 3:
                infoDic = interestFilterThree(self.path)
                if isinstance(infoDic,list):
                    self.info += infoDic
                elif isinstance(infoDic,dict):
                    self.info += [infoDic]
            elif self.numlist[0] == 4:
                infoDic = interestFilterFour(self.path)
                if isinstance(infoDic,list):
                    self.info += infoDic
                elif isinstance(infoDic,dict):
                    self.info += [infoDic]
            elif self.numlist[0] == 5:
                infoDic = interestFilterFive(self.path)
                if isinstance(infoDic,list):
                    self.info += infoDic
                elif isinstance(infoDic,dict):
                    self.info += [infoDic]
        
    
    def getDate(self):
        if len(self.info) == 1:
            item = self.event[0]
            for key in item:
                if key == 'date':
                    for numlike in item[key].split(' '):
                        if (len(numlike) == 2 and numlike.isdigit()):date=numlike
                        elif (len(numlike) == 3 and ((numlike[:-1].isdigit() and numlike[-1].isdigit()==False)):
                            date=numlike[:-1] 
                        elif (len(numlike) == 3 and (numlike[1:].isdigit() and numlike[0].isdigit()==False)):
                            date=numlike[1:]
                        elif:(len(numlike) == 1 and numlike.isdigit()):date = numlike
            return [item['event'],numlike,item['location'],item[time]]
        elif len(self.info) == 2:
            item1 = self.event[0]
            for key in item1:
                if key == 'date':
                    for numlike in item1[key].split(' '):
                        if (len(numlike) == 2 and numlike.isdigit()) or (len(numlike) == 3 and \
                        ((numlike[:-1].isdigit() and numlike[-1].isdigit()==False) or \
                        (numlike[1:].isdigit() and numlike[0].isdigit()==False))) or \
                        (len(numlike) == 1 and numlike.isdigit()):date1 = numlike
            item2 = self.event[1]
            for key in item2:
                if key == 'date':
                    for numlike in item2[key].split(' '):
                        if (len(numlike) == 2 and numlike.isdigit()) or (len(numlike) == 3 and \
                        ((numlike[:-1].isdigit() and numlike[-1].isdigit()==False) or \
                        (numlike[1:].isdigit() and numlike[0].isdigit()==False))) or \
                        (len(numlike) == 1 and numlike.isdigit()):date2 = numlike
            return [[item1['event'],numlike1,item1['location'],item1[time]],
            [item2['event'],numlike2,item2['location'],item2[time]]]   
        
    def time(self):
        if len(self.getDate()) > 2:
            date = self.getDate()[1]
            i = date//7+1
            j = date-i*7
            self.day[i][j] += 1
        elif len(self.gateDate()) == 2:
            for c in self.gateDate():
                date = c[1]
                i = date//7+1
                j = date-i*7
                self.day[i][j] += 1
                
            
            

############### redraw ####
    def redrawSign(self, screen):
        if self.mode == "sign":
            self.drawSign(screen)
            self.drawSignButtons(screen)
    
    def redrawInterest(self, screen):
        self.drawSubpage(screen)
        self.drawInterestInput(screen)
        self.drawInterestBar(screen)
        screen.blit(self.doneImg,(518-50,0))
    
    def redrawMain(self, screen):
        if self.mode == "main":
            screen.fill(self.grey)
            self.displayText(screen,"New Events", 200,80,0,0,self.white,self.topicFont)
            self.drawMainBtn(screen)
            self.drawEventBtn(screen,self.mainEvent1[4],self.mainEvent1[:4])
            drawText(self,["","","",""],screen,self.mainEvent1[0],self.mainEvent1[1],0,0)
            self.drawEventBtn(screen,self.mainEvent2[4],self.mainEvent2[:4])
            drawText(self,["","","",""],screen,self.mainEvent2[0],self.mainEvent2[1],0,0)
            self.drawEventBtn(screen,self.mainEvent3[4],self.mainEvent3[:4])
            drawText(self,["","","",""],screen,self.mainEvent3[0],self.mainEvent3[1],0,0)
            self.drawComBtn(screen)
            self.drawCalBtn(screen)
            screen.blit(self.oImg,(235,715))
            self.drawSettingBtn(screen)
    
    def redrawThreeIcon(self,screen):
        if self.mode == "threeIcon":
            screen.fill(self.grey)
            self.displayText(screen,"New Events", 200,80,0,0,self.white,self.topicFont)
            self.drawMainBtn(screen)
            self.drawEventBtn(screen,self.mainEvent1[4],self.mainEvent1[:4])
            drawText(self,["","","",""],screen,self.mainEvent1[0],self.mainEvent1[1],0,0)
            self.drawEventBtn(screen,self.mainEvent2[4],self.mainEvent2[:4])
            drawText(self,["","","",""],screen,self.mainEvent2[0],self.mainEvent2[1],0,0)
            self.drawEventBtn(screen,self.mainEvent3[4],self.mainEvent3[:4])
            drawText(self,["","","",""],screen,self.mainEvent3[0],self.mainEvent3[1],0,0)
            self.drawComBtn(screen)
            self.drawCalBtn(screen)
            screen.blit(self.oImg,(235,715))
            self.drawSettingBtn(screen)
            self.drawThreeIcon(screen)

    def redrawHand(self,screen):
        if self.mode=="hand":
            self.drawSubpage(screen)
            self.drawInputBox(screen)
            self.drawInputBoxText(screen)
            screen.blit(self.doneImg,(518-50,0))
        
    def drawHandBoxes(self,screen):
        clock = pygame.time.Clock()
    
        input_boxes = [self.titleInputBox, self.dateInputBox,\
                    self.beginTimeInputBox,self.endTimeInputBox,\
                    self.locationInputBox,self.descriptionInputBox ]

        for box in input_boxes:
            
            box.handleEvent(screen)
    
        pygame.display.flip()
        clock.tick(30)
        

        
    def redrawLibraryInput(self,screen):
        if self.mode == "libraryInput":
            self.drawSubpage(screen)
            pygame.draw.circle(screen,self.importButtons[0],(268,500),200)
            self.displayText(screen,"Input",68,300,400,400,self.white,self.topicFont)
    

    
    def redrawCalendar(self,screen):
        if self.mode == "calendar":
            self.calendarApril(screen)
            for i in range(5):
                for j in range(7):
                    if self.day[i][j] >= 1:
                        pygame.draw.circle(screen,self.black,(250 + j *70-223+30, 130 + i * 70+100+60),10)
    
    def redrawCalendarMarch(self,screen):
        if self.mode == "calendarMarch":
            self.calendarMarch(screen)
        
    def redrawCalendarMay(self,screen):
        if self.mode == "calendarMay":
            self.calendarMay(screen)
    
    def redrawWorking(self,screen):
        if self.mode == "working":
            self.displayText(screen,"Working...",100,300,100,-70,self.black,self.cuteFont)
            pygame.draw.rect(screen,self.white,(100,300,350,50))
            pygame.draw.rect(screen,self.black,(100,300,self.w,50))
            if self.num == 0:
                self.drawOrangeBtn(screen,(30,600))
                self.drawOrangeBtn(screen,(130,600))
                self.drawOrangeBtn(screen,(230,600))
                self.drawOrangeBtn(screen,(330,600))
                self.drawOrangeBtn(screen,(430,600))
            if self.num == 1:
                self.drawOrangeBtn(screen,(30,600+self.h1))
                self.drawOrangeBtn(screen,(130,600))
                self.drawOrangeBtn(screen,(230,600))
                self.drawOrangeBtn(screen,(330,600))
                self.drawOrangeBtn(screen,(430,600))
            elif self.num == 2:
                self.drawOrangeBtn(screen,(30,600))
                self.drawOrangeBtn(screen,(130,600+self.h2))
                self.drawOrangeBtn(screen,(230,600))
                self.drawOrangeBtn(screen,(330,600))
                self.drawOrangeBtn(screen,(430,600))
            elif self.num == 3:
                self.drawOrangeBtn(screen,(30,600))
                self.drawOrangeBtn(screen,(130,600))
                self.drawOrangeBtn(screen,(230,600+self.h3))
                self.drawOrangeBtn(screen,(330,600))
                self.drawOrangeBtn(screen,(430,600))
            elif self.num == 4:
                self.drawOrangeBtn(screen,(30,600))
                self.drawOrangeBtn(screen,(130,600))
                self.drawOrangeBtn(screen,(230,600))
                self.drawOrangeBtn(screen,(330,600+self.h4))
                self.drawOrangeBtn(screen,(430,600))
            elif self.num == 5:
                self.drawOrangeBtn(screen,(30,600))
                self.drawOrangeBtn(screen,(130,600))
                self.drawOrangeBtn(screen,(230,600))
                self.drawOrangeBtn(screen,(330,600))
                self.drawOrangeBtn(screen,(430,600+self.h5))
           
    def redrawFinish(self,screen):
        if self.mode == "finish":
            self.drawSubpage(screen)
            self.displayText(screen,"Done!",50,200,430,300,self.orange,self.cuteFont)
            screen.blit(self.orImg,(180,400))
        
    def redrawCalendarYes(self,screen):
        self.extractInfo()
        if self.mode == "calendarYes":
            self.calendarYes(screen)
            drawText(self,["THE REVOLUTION","APRIL 27","","FT.LAUDERDALE,FLORIDA"],screen,self.mainEvent1[0],self.mainEvent1[1])
        if len(getDate) > 2:
            self.drawEventBtn(screen,self.mainEven2[4],self.mainEvent2[:4])
            self.drawText(self,[self.getDate()[0],self.getDate()[1],self.getDate()[3],self.getDate()[2]],screen,self.mainEvent2[0],self.mainEvent2[1])
        else:
            self.drawEventBtn(screen,self.mainEven2[4],self.mainEvent2[:4])
            self.drawText(self,[self.getDate()[0],self.getDate()[1],self.getDate()[3],self.getDate()[2]],screen,self.mainEvent2[0],self.mainEvent2[1])
            self.drawEventBtn(screen,self.mainEven3[4],self.mainEvent3[:4])
            self.drawText(self,[self.getDate()[0],self.getDate()[1],self.getDate()[3],self.getDate()[2]],screen,self.mainEvent3[0],self.mainEvent3[1])
        
    
    def redrawCalendarNo(self,screen):
        if self.mode == "calendarNo":
            self.calendarNo(screen)
        
    def redrawCommunity(self,screen):
        if self.mode == "community":
            self.drawSubpage(screen)
            pygame.draw.rect(screen,self.friendEventBtn[4],self.friendEventBtn[:4])
            self.displayText(screen,"Friends' Event",self.friendEventBtn[0],
            self.friendEventBtn[1],300,200,self.black,self.cuteFont)
            pygame.draw.rect(screen,self.localEventBtn[4],self.localEventBtn[:4])
            self.displayText(screen,"Local Event",self.localEventBtn[0],
            self.localEventBtn[1],300,200,self.black,self.cuteFont)
            self.displayText(screen,"OR",100,550,200,100,self.black,self.cuteFont)
            self.drawSearchBtn(screen,(400,700))
        
    def redrawCommunityFriends(self,screen):
        if self.mode == "communityFriends":
            self.drawCommunityFriends(screen)
        
    def redrawPreference(self,screen):
        if self.mode == "preference":
            a = 100
            b = 200
            d = 0
            self.displayText(screen,"Interest",100,100,0,0,self.black,self.cuteFont)
            for c in self.interestList:
                self.drawInterestBtn(screen,c,loc)
        
    def redrawAll(self, screen):
        self.redrawSign(screen)
        self.redrawInterest(screen)
        self.redrawMain(screen)
        #self.redrawHand(screen)
        self.redrawLibraryInput(screen)
        self.redrawCalendar(screen)
        self.redrawWorking(screen)
        self.redrawFinish(screen)
        self.redrawCalendarYes(screen)
        self.redrawCalendarNo(screen)
        self.redrawCalendarMarch(screen)
        self.redrawCalendarMay(screen)
        self.redrawCommunity(screen)
        self.redrawCommunityFriends(screen)
        self.redrawPreference(screen)
        self.redrawThreeIcon(screen)
        self.redrawHand(screen)
        

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=536, height=819, fps=50, title="BlackOrange"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (99,99,112)

        pygame.init()
        

    def run(self):
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()

        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                    print(event.pos)
                    self.currentPos=event.pos
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                # elif (event.type == pygame.MOUSEMOTION and
                #       event.buttons[0] == 1):
                #     self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()



def main():
    game = PygameGame(536,819)
    game.run()

if __name__ == '__main__':
    main()