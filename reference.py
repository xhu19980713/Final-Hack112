class PygameGame(object):
   
    # Helpers
    # Init functions
    def initColor(self):
        self.white = (255,255,255)

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
        self.deepOrange = self.hex_to_rgb("#c16112")  #pressed
    

    def within(self,left,down,width,height,x,y):
        return left < x < left+width and down < y < down +height

    def hex_to_rgb(self,value):
        """Return (red, green, blue) for the color given as #rrggbb."""
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
        
    def loadFont(self):
        self.regularFont = pygame.font.SysFont("Arvo-Bold.ttf",35)
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
        first_button_y = 475
        first_button_x = 118
        self.signInBtn = [first_button_x,first_button_y,width,height, self.orange]
        self.signUpBtn = [first_button_x,first_button_y+gap+height,width,height,self.orange]

    def interestButtons(self):
        gap=10
        btnHeight=35
        self.interestButtonList=[]
        for i in range(0,len(self.interestList)):
            lenText=len(self.interestList[i])
            self.interestButtonList+=InterestBox(43,30+btnWidth*i+gap*i,\
                                                lenText*10+20,btnWidth,\
                                                self.interestList[i])
                                                
    def mainButtons(self):
        width=200
        gap=10
        self.mainEvent1=[43,80,450,width,self.white]
        self.mainEvent2=[43,80+width+gap,450,width,self.white]
        self.mainEvent3=[43,80+width*2+gap*2,450,width,self.white]
        # main function button ps?
        
        
    def handButtons(self):
        self.titleInput()
        self.dateInput()
        self.beginTimeInput()
        self.endTimeInput()
        self.locationInput()
        self.descriptionInput()
        
   # def finishButtons(self):
   #     self.
        
    
    #def calendarButtons(self):
        #xh

    
    def buttons(self):
        self.interestInput()
        self.signButtons()
        self.interestButtons()
        self.mainButtons()
        self.handButtons
        self.importButtons=[self.orange,(218,500,),200]
        #self.finishButtons()
        #self.calendarButtons()
        self.friendEventBtn=[118,100,300,200,self.orange]
        self.localEventBtn=[118,350,300,200,self.orange]
        self.preferenceBtn=[118,475,300,40,self.orange]
    
      
##############################
#text input boxes
##############################
    def interestInput(self):
        #text input box at interest input page
        self.interestList=[]
        boxWidth=450
        boxHeight=35
        self.interestInputBox=InputBox(43,70,boxWidth,boxHeight,self.interestList,self.regularFont)
        
    def titleInput(self):
        self.titleText=""
        boxWidth=450
        boxHeight=35
        self.titleInputBox=InputBox(43,70,boxWidth,boxHeight,self.titleText,self.regularFont)
        
    def dateInput(self):
        self.dateText=""
        boxWidth=200
        boxHeight=35
        self.dateInputBox=InputBox(43,125,boxWidth,boxHeight,self.dateText,self.regularFont)
        
    def beginTimeInput(self):
        self.beginTimeText=""
        boxWidth=100
        boxHeight=35
        self.beginTimeInputBox=InputBox(43,180,boxWidth,boxHeight,self.beginTimeText,self.regularFont)
    
    def endTimeInput(self):
        self.endTimeText=""
        boxWidth=100
        boxHeight=35
        self.endTimeInputBox=InputBox(158,180,boxWidth,boxHeight,self.endTimeText,self.regularFont)
    
    def locationInput(self):
        self.locationText=""
        boxWidth=200
        boxHeight=35
        self.locationInputBox=InputBox(43,235,boxWidth,boxHeight,self.locationText,self.regularFont)
        
    def descriptionInput(self):
        self.descriptionText=""
        boxWidth=450
        boxHeight=100
        self.descriptionInputBox=InputBox(43,290,boxWidth,boxHeight,self.descriptionText,self.regularFont)

#########################
### Main Framework ######
#########################

    def init(self):
        self.mode = "sign"
        self.initColor()
        self.signButtons()
        self.loadFont()
        self.initBtnList=[self.signInBtn,self.signUpBtn]
        #14 modes 
        self.modeLst=["sign","interest","main","hand","libraryInput","camera"\
                      "calendar","working","finish","calendarYes","calendarNo",\
                      "calendarMarch","calendarMay","community"\
                      "communityFriends","preference","friendEvent"]
        self.path = None
        self.buttons()
        self.week = ['Sun','Mon','Tus','Wed','Thr','Fri','Sat']
        self.userImg = pygame.image.load('orange.png')
        self.instaImg = pygame.image.load('instagram.png')
        self.snapImg = pygame.image.load('snapchat1.png')
        self.fbImg = pygame.image.load('fb1.png')
        self.oImg = pygame.image.load('o.png')
        self.friendImg = pygame.image.load('login1.png')
        self.messageImg = pygame.image.load('bubble.png')
        
        #self.loadLogo()  xh
        #self.loadShareLogo() xh

#### MousePressed ####
    def mousePressedSign(self,x,y):
        if self.mode=="sign":
            #signInBtn
            surface= self.initBtnList[0]
            if self.within(surface[0],surface[2],surface[1],surface[3],x,y):
                surface[4]=self.deepOrange
            #signUpBtn
            surface=self.initBtnList[1]
            if self.within(surface[0],surface[2],surface[1],surface[3],x,y):
                surface[4]=self.deepOrange
                
    def mousePressedLibraryInput(self,x,y):
        if self.mode=="libraryInput":
            surface=self.importButtons
            if (x-218)**2+(y-500)**2<=200**2:
                surface[1]=self.deepOrange
                
    # def mousePressCalendar(self,x,y):
    #     if self.mode=="calendar":
    #         #xh
    #             
    def mousePressedCommunity(self,x,y):
        if self.mode=="community":
            surface=self.friendEventBtn
            if self.within(surface[0],surface[2],surface[1],surface[3],x,y):
                surface[4]=self.deepOrange
            
            surface=self.self.localEventBtn
            if self.within(surface[0],surface[2],surface[1],surface[3],x,y):
                surface[4]=self.deepOrange
            
    def mousePressedPreference(self,x,y):
        if self.mode=="preference":
            surface=self.preferenceBtn
            if self.within(surface[0],surface[2],surface[1],surface[3],x,y):
                surface[4]=self.deepOrange
                
    def mousePressed(self,x,y):
        self.mousePressedSign(x,y)
        self.mousePressedLibraryInput(x,y)
        #self.mousePressCalendar(x,y)
        self.mousePressedCommunity(x,y)
        self.mousePressedPreference(x,y)
        
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
            surface= self.initBtnList[0]
            if self.within(surface[0],surface[2],surface[1],surface[3],x,y):
                surface[4]=self.orange
            #signUpBtn
            surface=self.initBtnList[1]
            if self.within(surface[0],surface[2],surface[1],surface[3],x,y):
                surface[4]=self.orange
                self.mode="interest"
            
    # def mouseReleasedCalendar(self,x,y):
    #     
    
    def mouseReleasedLibraryInput(self,x,y):
        if self.mode=="libraryInput":
            surface=self.importButtons
            if (x-218)**2+(y-500)**2<=200**2:
                surface[1]=self.orange
                self.path=self.open_file_browser()
                if self.path!="":
                    self.mode="working"
    
    def mouseReleasedBack(self,x,y):
        if self.within(0,0,60,60,x,y):
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
            elif self.mode=="friendEvent":
                self.mode="community"
                
    def mouseReleasedDone(self,x,y):
        if self.within(536-60,0,60,60,x,y):
            if self.mode=="finish":
                self.mode="main"
            elif self.mode=="hand":
                self.mode="main"
            elif self.mode=="interest":
                self.mode="main"
                
    def mouseReleasedPreference(self,x,y):
        if self.mode=="preference":
            surface=self.preferenceBtn
            if self.within(surface[0],surface[2],surface[1],surface[3],x,y):
                surface[4]=self.orange
                data.mode="friendEvent"
    
   # def mouseReleasedMonthChange(self,x,y):
   
            
    def mouseReleased(self,x,y):
        self.mouseReleasedSign(x,y)
        #self.mouseReleasedCalendar(x,y)
        self.mouseReleasedLibraryInput(x,y)
        self.mouseReleasedBack(x,y)
        self.mouseReleasedDone(x,y)
        self.mouseReleasedPreference(x,y)
        print(self.mode)
        
#### MouseMotion ####
    def mouseMotionSign(self,x,y):
        if self.mode=="sign":
            for btn in self.initBtnList:
                if self.within(btn[0],btn[2],btn[1],btn[3],x,y):
                    btn[4]=self.darkOrange
                else:
                    btn[4]=self.orange 

    def mouseMotionInterest(self,x,y):
        if self.mode=="interest":
            if len(self.interestButtonList)!=0:
                for btn in self.interestButtonList:
                    if self.within(btn[0],btn[2],btn[1],btn[3],x,y):
                        btn[4]=self.darkOrange
                    else:
                        btn[4]=self.orange 
                
    def mouseMotionMain(self,x,y):
        if self.mode=="main":
            for btn in [self.mainEvent1,self.mainEvent2,self.mainEvent3]:
                if self.within(btn[0],btn[2],btn[1],btn[3],x,y):
                    btn[4]=self.darkOrange
                else:
                    btn[4]=self.orange 
            
    def mouseMotionLibraryInput(self,x,y):
        if self.mode=="libraryInput":
            surface=self.importButtons
            if (x_218)**2+(y-500)**2<=200**2:
                surface[1]=self.darkOrange
            else:
                surface[1]=self.orange
    
    # def mouseMotionFinish(self,x,y):
    #     if self.mode=="finish":
            
    def mouseMotionCommunity(self,x,y):
        if self.mode=="community":
            btn=self.friendEventBtn
            if self.within(btn[0],btn[2],btn[1],btn[3],x,y):
                btn[4]=self.darkOrange
            else:
                btn[4]=self.orange 
                
            btn=self.localEventBtn
            if self.within(btn[0],btn[2],btn[1],btn[3],x,y):
                btn[4]=self.darkOrange
            else:
                btn[4]=self.orange 
        
    # def mouseMotionCalendar(self,x,y):
    #     if self.mode=="calendar":
    #         #xh
            
    def mouseMotionPreference(self,x,y):
        if self.mode=="preference":
            btn=self.preferenceBtn
            if self.within(btn[0],btn[2],btn[1],btn[3],x,y):
                btn[4]=self.darkOrange
            else:
                btn[4]=self.orange 

    def mouseMotion(self, x, y):
        self.mouseMotionSign(x,y)
        self.mouseMotionInterest(x,y)
        self.mouseMotionMain(x,y)
        self.mouseMotionLibraryInput(x,y)
        self.mouseMotionCommunity(x,y)
        #self.mouseMotionCalendar(x,y)
        self.mouseMotionPreference(x,y)

    def keyPressed(self, keyCode, modifier):
        pass

    def keyReleased(self, keyCode, modifier):
        pass
        
        


#### timerFried ####

    def timerFired(self, dt):
        pass
        
###########################
#draw
###########################
    # change
    def drawSign(self):
        screen.fill(self.grey)
        screen.blit(self.userImg,(80,70))
        screen.blit(self.fbImg,(118,700))
        screen.blit(self.instaImg,(235.3,700))
        screen.blit(self.snapImg,(353,700))
        
    def drawMainBtn(self,screen):
        pygame.draw.circle(screen,self.orange,(218,779),70)
        pygame.draw.rect(screen,self.orange,(0,819-80,536,80))
        textSurface = self.buttonFont.render("community", True, self.white)
        textRect1 = textSurface.get_rect()
        textRect1.center = (a + c / 2, b + d / 2)
        screen.blit(textSurface, textRect1)
        
    def drawSubpage(self):
        screen.fill(self.grey)
        self.drawShades(self.white,0,0,self.width,60)
        
    def drawShades(self,color, a, b, c, d):
            pygame.draw.rect(screen,(160,160,160),(a-7,b-7,c+14,d+14))
            pygame.draw.rect(screen,(170,170,170),(a-6,b-6,c+12,d+12))
            pygame.draw.rect(screen,(190,190,190),(a-5,b-5,c+10,d+10))
            pygame.draw.rect(screen,(210,210,210),(a-4,b-4,c+8,d+8))
            pygame.draw.rect(screen,(230,230,230),(a-3,b-3,c+6,d+6))
            pygame.draw.rect(screen,(240,240,240),(a-2,b-2,c+4,d+4))
            pygame.draw.rect(screen,(250,250,250),(a-1,b-1,c+2,d+2))
            pygame.draw.rect(screen, color, (a,b,c,d))
            
    def drawCalendarButton(self,color, fontColor, a, b, c, d, text,font, width = 0):
            pygame.draw.rect(screen, color, (a,b,c,d), width)
            myFont = font
            textSurface = myFont.render(text, True, fontColor)
            textRect1 = textSurface.get_rect()
            textRect1.center = (a + c/2, b + d/2)
            screen.blit(textSurface, textRect1)
                
    def drawLeftRightButton(self, color, loc):
        pygame.draw.polygon(screen, color, loc)
    
    def calendarMarch(self):
        self.subpage()
        x = -223
        y = 100
        self.drawCalendarButton(self.grey, self.orange, 250+x, 10+y, 480, 50, "March, 2018",self.regularFont)
        self.drawLeftRightButton(self.orange,((260+x,55+y-20),(290+x,40+y-20),(290+x,70+y-20)))
        self.drawLeftRightButton(self.orange,((720+x,55+y-20),(690+x,40+y-20),(690+x,70+y-20)))
        for i in range(7):
            self.drawCalendarButton(self.grey,self.white,250 + i * 70+x, 90+y, 60, 30, self.week[i], self.weekFont)
            day = 29
            for i in range(5):
                for j in range(7):
                    if i == 0 and j < 4: continue
                    if i ==0 and j == 4:
                        day = 1
                # if calendarColor[i][j] == 0 :
                            # self.drawCalendarButton(screen, self.blueGray, self.white, 250 + j *70, 130 + i * 70, 60, 60, str(day), 25)
                    self.drawCalendarButton(self.grey, self.orange, 250 + j *70+x, 130 + i * 70+y, 60, 60, str(day), self.calendarFont)
                # if calendarColor[i][j] == 1:
                        #self.drawCalendarButton(screen, self.blueGray, self.blueGray, 250 + j *70, 130 + i * 70, 60, 60, str(day), 25, 3)
                        #drawCalendarButton(grey, white, 250 + j *70+x, 130 + i * 70+y, 60, 60, str(day), 25)
                    day = day + 1
        screen.blit(self.oImg, (80,700))
    
    def calendarApril(self):
        self.drawSubpage()
        x = -223
        y = 100
        self.drawCalendarButton(self.grey, self.orange, 250+x, 10+y, 480, 50, "April, 2018",self.regularFont)
        self.drawLeftRightButton(self.orange,((260+x,55+y-20),(290+x,40+y-20),(290+x,70+y-20)))
        self.drawLeftRightButton(self.orange,((720+x,55+y-20),(690+x,40+y-20),(690+x,70+y-20)))
        for i in range(7):
            self.drawCalendarButton(self.grey,self.white,250 + i * 70+x, 90+y, 60, 30,self.week[i], self.weekFont)
    
            day = 29
            for i in range(5):
                for j in range(7):
                    if i == 4 and j > 2: continue
                    if i ==0 and j == 0:
                        day = 1
                # if calendarColor[i][j] == 0 :
                            # self.drawCalendarButton(screen, self.blueGray, self.white, 250 + j *70, 130 + i * 70, 60, 60, str(day), 25)
                    self.drawCalendarButton(self.grey, self.orange, 250 + j *70+x, 130 + i * 70+y, 60, 60, str(day), self.calendarFont)
                # if calendarColor[i][j] == 1:
                        #self.drawCalendarButton(screen, self.blueGray, self.blueGray, 250 + j *70, 130 + i * 70, 60, 60, str(day), 25, 3)
                        #drawCalendarButton(grey, white, 250 + j *70+x, 130 + i * 70+y, 60, 60, str(day), 25)
                    day = day + 1
    
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
        screen.blit(self.oImg, (80,700))
    
    def calendarMay(self):
        self.drawSubpage()
        x = -223
        y = 100
        self.drawCalendarButton(self.grey, self.orange, 250+x, 10+y, 480, 50, "May, 2018", self.regularFont)
        self.drawLeftRightButton(self.orange,((260+x,55+y-20),(290+x,40+y-20),(290+x,70+y-20)))
        self.drawLeftRightButton(self.orange,((720+x,55+y-20),(690+x,40+y-20),(690+x,70+y-20)))
        for i in range(7):
            self.drawCalendarButton(self.grey,self.white,250 + i * 70+x, 90+y, 60, 30, self.week[i], self.weekFont)
    
            day = 29
            for i in range(5):
                for j in range(7):
                    if i == 0 and j < 2 or i == 4 and j > 4: continue
                    if i ==0 and j == 2:
                        day = 1
                # if calendarColor[i][j] == 0 :
                            # self.drawCalendarButton(screen, self.blueGray, self.white, 250 + j *70, 130 + i * 70, 60, 60, str(day), 25)
                    self.drawCalendarButton(self.grey, self.orange, 250 + j *70+x, 130 + i * 70+y, 60, 60, str(day), self.calendarFont)
                # if calendarColor[i][j] == 1:
                        #self.drawCalendarButton(screen, self.blueGray, self.blueGray, 250 + j *70, 130 + i * 70, 60, 60, str(day), 25, 3)
                        #drawCalendarButton(grey, white, 250 + j *70+x, 130 + i * 70+y, 60, 60, str(day), 25)
                    day = day + 1
        screen.blit(self.oImg, (80,700))
        
    def drawCommunityFriends(self):
        self.drawSubpage()
        screen.blit(self.friendImg,(20,180))
        screen.blit(self.friendImg,(20,380))
        screen.blit(self.friendImg,(20,580))
        screen.blit(self.messageImg, (140,150))
        screen.blit(self.messageImg, (140,350))
        screen.blit(self.messageImg, (140,550))
        
    def calendarYes(self):
        self.drawSubpage()
        x = -223
        y = 150
        yw = 0
        for i in range(7):
            self.drawCalendarButton(self.grey,self.orange,250 + i * 70+x, 90+yw, 60, 30, self.week[i], self.weekFont)
        self.drawCalendarButton(self.grey, self.orange, 250+x, 10+y, 480, 50,"April 6, 2018", self.regularFont)
        self.drawLeftRightButton(self.orange,((260+x,55+y-20),(290+x,40+y-20),(290+x,70+y-20)))
        self.drawLeftRightButton(self.orange,((720+x,55+y-20),(690+x,40+y-20),(690+x,70+y-20)))
        
    def calendarNo(self):
        self.drawSubpage()
        x = -223
        y = 150
        yw = 0
        for i in range(7):
            self.drawCalendarButton(self.grey,self.orange,250 + i * 70+x, 90+yw, 60, 30, self.week[i], self.weekFont)
        self.drawCalendarButton(self.grey, self.orange, 250+x, 10+y, 480, 50,"April 6, 2018", self.regularFont)
        self.drawLeftRightButton(self.orange,((260+x,55+y-20),(290+x,40+y-20),(290+x,70+y-20)))
        self.drawLeftRightButton(self.orange,((720+x,55+y-20),(690+x,40+y-20),(690+x,70+y-20)))
        screen.blit(self.oImag,(170, 500))
        self.displayText('"An Orange A Day',20,150,500,500,self.orange)
        self.displayText('   Keeps Doctors Away"',20,220,500,500,self.black)
        
    
    def displayText(self,text,a,b,c,d,fontColor):
        myFont = self.cuteFont
        textSurface = myFont.render(text, True, fontColor)
        textRect1 = textSurface.get_rect()
        textRect1.center = (a + c/2, b + d/2)
        screen.blit(textSurface, textRect1)
        
                
############### redraw ####
    def redrawSign(self, screen):
        self.sign(self)
        self.
    
    def redrawAll(self, screen):
        pass
        

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