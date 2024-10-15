#imports
import random
from sys import exit

from guizero import App, Text, TextBox, PushButton, Window, warn, ListBox
import pandas as pd
import sqlite3 as sql


#testing - database connection
def checkConn(conn):
  try:
    conn.cursor()
    return True
  except Exception as ex:
    return False

    
#Advanced Higher Concept - connect to database
conn = sql.connect("dnd.db")
print("Database connection:", checkConn(conn))
print()
crs = conn.cursor()


# #New Knowledge - Pandas, tidying files
# #read in the class file, skipping the metadata
# dndClass = pd.read_csv("DnDClasses.csv", skiprows=2)
# #tidy the dataframe - remove duplicates and irrelevant columns
# dndClass = dndClass.drop_duplicates()
# dndClass = dndClass.drop('Role', axis=1)

# #add it to the database
# dndClass.to_sql(name='Classes', con=conn)

# #read in the race file and skip the metadata
# dndRace = pd.read_csv("DnDRaces.csv", skiprows=1)
# #tidy the dataframe - remove duplicates and irrelevant columns
# dndRace = dndRace.drop_duplicates()
# dndRace = dndRace.drop('Darkvision', axis=1)

# #add it to the database
# dndRace.to_sql(name='Races', con=conn)


#character class
class Character():
  def __init__(self):
    self.name = ""
    self.charClass = ""
    self.race = ""
    self.hitPoints = 0
    self.armourClass = 0
    self.jumpDistance = 0
    self.jumpHeight = 0
    self.speed = 0
    self.hitDice = ""

  #setter methods
  def setRace(self, race):
    self.race = race

  def setClass(self, charClass):
    self.charClass = charClass

  def setJumpDistance(self, stren):
    self.jumpDistance = stren.getScore()

  def setJumpHeight(self, stren):
    self.jumpHeight = 3 + stren.getModifier()

  def setHitPoints(self, classHitPoints, con):
    self.hitPoints = classHitPoints + con.getModifier()

  def setName(self, name):
    self.name = name

  def setArmourClass(self, armour):
    self.armourClass = armour

  def setSpeed(self, speed):
    self.speed = speed

  def setHitDice(self, hitDice):
    self.hitDice = ("1d" + str(hitDice))
    
  #getter methods
  def getName(self):
    return(self.name)

  def getRace(self):
    return(self.race)

  def getClass(self):
    return(self.charClass)

  def getArmourClass(self):
    return self.armourClass

  def getJumpDistance(self):
    return self.jumpDistance

  def getJumpHeight(self):
    return self.jumpHeight

  def getHitPoints(self):
    return self.hitPoints

  def getSpeed(self):
    return self.speed

  def getHitDice(self):
    return self.hitDice

    
#stat class
class stat():
  def __init__(self):
    self.score = 0
    self.modifier = 0

  #setter methods
  def setScore(self, score):
    self.score = score

  def setModifier(self, score):
    temp = int(score/2)
    self.modifier = temp-5

  #getter methods
  def getScore(self):
    return int(self.score)

  def getModifier(self):
    return int(self.modifier)

    
#the window to input the race
def raceWindowFunction():
  raceWindow = Window(introApp, layout="grid", title="Character Builder - Race")
  introApp.hide()

  #padding line
  padding = Text(raceWindow, grid=[0,0], width=1, height=1, size=3)

  #descriptions of each race
  humanMessage = "Human - that's you. They're generic, alright at everything, not really any special talents."
  elfMessage = "Elf - You have to have seen Lord of the Rings. You know, the guys with the pointy ears and the bows. Dress all fancy, live for hundreds of years, you get me."
  dwarfMessage = "Dwarf - Rock Miners. They're small and stout and pack a mean punch. They love rocks and stones and apparently God?"
  halfElfMessage = "Half-Elf - What you get when you mix humans and elves. They're kinda pretty, live a bit longer and that's about it."
  tieflingMessage = "Tiefling - They come from Devils, or maybe Demons. I never remember which one. It's the one from Hell. Anyway, they have horns. Some people consider them evil. That's a bit wierd."
  halfOrcMessage = "Half-Orc - If you took a really really big burly guy, and mixed them with human, that's a half-orc. They're pretty big, got tusks, often seen as rash and violent, but I think they're all sweethearts."
  halflingMessage = "Halfling - Hobbits. They're just Hobbits"
  gnomeMessage = "Gnome - No, they don't live in gardens. They are cunning, friendly and lovable. They're all small."
  dragonbornMessage = "Dragonborn - Humanoid dragon people who can breathe fire/acid/cold/lightening. Do they come from eggs? We don't know."
  randomMessage = "Or enter Random - let the program decide."
  
  raceText = Text(raceWindow, text="Enter a race:", grid=[1,1], align="left")
  raceBox = TextBox(raceWindow, grid=[1,2], align="left")
  
  humanDescription = TextBox(raceWindow, text=humanMessage, multiline=True, height=2, width=68, grid=[1,3], enabled=False)
  elfDescription = TextBox(raceWindow, text=elfMessage, multiline=True, height=3, width=68, grid=[1,4], enabled=False)
  dwarfDescription = TextBox(raceWindow, text=dwarfMessage, multiline=True, height=2, width=68, grid=[1,5], enabled=False)
  halfElfDescription = TextBox(raceWindow, text=halfElfMessage, multiline=True, height=2, width=68, grid=[1,6], enabled=False)
  tieflingDescription = TextBox(raceWindow, text=tieflingMessage, multiline=True, height=3, width=68, grid=[1,7], enabled=False)
  halfOrcDescription = TextBox(raceWindow, text=halfOrcMessage, multiline=True, height=3, width=68, grid=[1,8], enabled=False)
  halflingDescription = TextBox(raceWindow, text=halflingMessage, multiline=True, height=1, width=68, grid=[1,9], enabled=False)
  gnomeDescription = TextBox(raceWindow, text=gnomeMessage, multiline=True, height=2, width=68, grid=[1,10], enabled=False)
  dragonbornDescription = TextBox(raceWindow, text=dragonbornMessage, multiline=True, height=2, width=68, grid=[1,11], enabled=False)
  randomDescription = TextBox(raceWindow, text=randomMessage, multiline=True, height=1, width=68, grid=[1,12], enabled=False)

  #text colours - rainbow
  humanDescription.text_color = "#cc1616"
  elfDescription.text_color = "#ba4d16"
  dwarfDescription.text_color = "#9c7709"
  halfElfDescription.text_color = "#3c7d07"
  tieflingDescription.text_color = "#0e631f"
  halfOrcDescription.text_color = "#128a72"
  halflingDescription.text_color = "#095a9c"
  gnomeDescription.text_color = "#0c0f9c"
  dragonbornDescription.text_color = "#6a0794"
  randomDescription.text_color = "#a60588"
  
  submitRaceButton = PushButton(raceWindow, text="Submit", command=raceInput, grid=[1,13], args=[raceBox, raceWindow])

  
#the window to input the class
def classWindowFunction():
  classWindow = Window(introApp, layout="grid", title="Character Builder - Class")

  #padding line
  padding = Text(classWindow, grid=[0,0], width=1, height=1, size=3)
  
  #description of each class
  barbarianMessage = "Barbarian - Hit Big. Get Hit Lot. Big Axe/Sword/Maul/Club."
  bardMessage = "Bard - Music. Poems. Stories. Bards are inspiration for the party. They buff and support their allies, as well as nerfing and hindering their enemies. Unless they're in love with their enemies, then they hinder their allies."
  clericMessage = "Cleric - They can heal. They can buff. They can nerf (or nothing). They can hit. They are religious. They follow God. Maybe not the God you're thinking of just now, but some cool fantasy God with 17 arms."
  druidMessage = "Druid - You're in tune with nature. You can turn into animals, you can talk to plants, it's hippy stuff."
  fighterMessage = "Fighter - You hit real good."
  monkMessage = "Monk - You're fast and punch good."
  rangerMessage = "Ranger - You're a guardian of the forest. You use your knowledge of tracking and hunting to help the party."
  rogueMessage = "Rogue - You're sneaky. You're stealthy. You look for weak points."
  paladinMessage = "Paladin - You have the power of God and Anime on your side."
  sorcererMessage = "Sorcerer - You have had this magic in you since you were born. This innate power grows inside you."
  warlockMessage = "Warlock - You made a deal with a shady guy in a back alley and now you have magic powers."
  wizardMessage = "Wizard - You read too much, nerd."
  randomMessage = "Or enter Random - let the program decide."
  
  classText = Text(classWindow, text="Enter a class:", grid=[1,1], align="left")
  classBox = TextBox(classWindow, grid=[1,2], align="left")
  
  barbarianDescription = TextBox(classWindow, text=barbarianMessage, multiline=True, grid=[1,3], height=1, width=68, enabled=False)
  bardDescription = TextBox(classWindow, text=bardMessage, multiline=True, grid=[1,4], height=4, width=68, enabled=False)
  clericDescription = TextBox(classWindow, text=clericMessage, multiline=True, grid=[1,5], height=3, width=68, enabled=False)
  druidDescription = TextBox(classWindow, text=druidMessage, multiline=True, grid=[1,6], height=2, width=68, enabled=False)
  fighterDescription = TextBox(classWindow, text=fighterMessage, multiline=True, grid=[1,7], height=1, width=68, enabled=False)
  monkDescription = TextBox(classWindow, text=monkMessage, multiline=True, grid=[1,8], height=1, width=68, enabled=False)
  rangerDescription = TextBox(classWindow, text=rangerMessage, multiline=True, grid=[1,9], height=2, width=68, enabled=False)
  rogueDescription = TextBox(classWindow, text=rogueMessage, multiline=True, grid=[1,10], height=1, width=68, enabled=False)
  paladinDescription = TextBox(classWindow, text=paladinMessage, multiline=True, grid=[1,11], height=1, width=68, enabled=False)
  sorcererDescription = TextBox(classWindow, text=sorcererMessage, multiline=True, grid=[1,12], height=2, width=68, enabled=False)
  warlockDescription = TextBox(classWindow, text=warlockMessage, multiline=True, grid=[1,13], height=2, width=68, enabled=False)
  wizardDescription = TextBox(classWindow, text=wizardMessage, multiline=True, grid=[1,14], height=1, width=68, enabled=False)
  randomDescription = TextBox(classWindow, text=randomMessage, multiline=True, height=1, width=68, grid=[1,15], enabled=False)

  #text colours - rainbow
  barbarianDescription.text_color = "#961209"
  bardDescription.text_color = "#a63805"
  clericDescription.text_color = "#917806"
  druidDescription.text_color = "#477306"
  fighterDescription.text_color = "#0d4a09"
  monkDescription.text_color = "#0b8049"
  rangerDescription.text_color = "#067373"
  rogueDescription.text_color = "#084d70"
  paladinDescription.text_color = "#083370"
  sorcererDescription.text_color = "#200580"
  warlockDescription.text_color = "#5d0785"
  wizardDescription.text_color = "#8d0699"
  randomDescription.text_color = "#8f0764"
  
  submitClassButton = PushButton(classWindow, text="Submit", command=classInput, grid=[1,16], args=[classBox])

  
#validating race input and getting a random race if necessary
def raceInput(inputtedRace, raceWindow):
  inputtedRace = inputtedRace.value.lower()
  
  #Advanced Higher Concept - SQL Query
  rows = crs.execute("SELECT * FROM Races WHERE Name = ?", (inputtedRace,),).fetchall()
  
  if len(rows) == 0 and inputtedRace != "random":
    introApp.warn("Invalid Race", "Please re-enter the race")
    return
  
  if inputtedRace == "random":
    #Advanced Higher Concept - SQL Query
    rows = crs.execute("SELECT Name FROM Races").fetchall()  
    inputtedRace = rows[random.randint(0,len(rows)-1)][0]

  #set the race to the inputted race once it has passed validation
  char.setRace(inputtedRace)

  #testing - print race
  print(char.race)
  print()

  #call the function to enter a class
  classWindowFunction()
  #hide the enter race window
  raceWindow.hide()

  
#validating the class input and getting a random class if necessary
def classInput(inputtedClass):
  inputtedClass = inputtedClass.value.lower()

  #Advanced Higher Concept - SQL Query
  rows = crs.execute("SELECT * FROM Classes WHERE Name = ?", (inputtedClass,),).fetchall()
  
  if len(rows) == 0 and inputtedClass != "random":
    introApp.warn("Invalid Class", "Please re-enter the class")
    return
    
  if inputtedClass == "random":
    #Advanced Higher Concept - SQL Query
    rows = crs.execute("SELECT Name FROM Classes").fetchall()  
    inputtedClass = rows[random.randint(0,len(rows)-1)][0]

  #set the class to the inputted class once it has passed validation
  char.setClass(inputtedClass)
  
  #testing - print class
  print(char.charClass)
  print()
  
  #call the set stats function
  setStats(char.getClass(), char.getRace(), statistics, sixStats)
  
  #call jumping functions
  char.setJumpHeight(stren)
  char.setJumpDistance(stren)
  
  #testing - jump function
  print()
  print("Jump Distance:", char.getJumpDistance())
  print("Jump Height:", char.getJumpHeight())

  #hit points function
  #Advanced Higher Concept - SQL Query
  classHP = crs.execute("SELECT Hitpoints FROM Classes WHERE Name = ?", (char.getClass(),),).fetchall()
  char.setHitPoints(classHP[0][0], con)
  #call hit dice function
  char.setHitDice(classHP[0][0])
  
  #testing - hit points
  print()
  print("Hit Points:", char.getHitPoints())
  #testing - hit dice
  print("Hit Dice:", char.getHitDice())
  print()
  
  #call the armour class function
  findingArmourClass(char.getClass(), dex, con, wis)
  #testing - armour class
  print("Armour Class:", char.getArmourClass())

  #call the speed function
  #Advanced Higher Concept - SQL Query
  raceSpeed = crs.execute("SELECT Speed FROM Races WHERE Name = ?", (char.getRace(),),).fetchall()
  char.setSpeed(raceSpeed[0][0])
  #testing - speed
  print("Speed:" + str(char.getSpeed()) + "ft")

  #call the function where you enter the character's name
  charNameWindowFunction()

  
#Set stats function
def setStats(charClass, charRace, statistics, characterStats):
  #Advanced Higher Concept - SQL Query
  orderOfStats = crs.execute("SELECT FirstStat, SecondStat, ThirdStat, FourthStat, FifthStat, SixthStat FROM Classes WHERE Name = ?", (charClass,),).fetchall()
  
  #Advanced Higher Concept - SQL Query
  primaryStat = crs.execute("SELECT PrimaryStat FROM Races WHERE Name = ?", (charRace,),).fetchall()
  
  #Advanced Higher Concept - SQL Query
  secondaryStat = crs.execute("SELECT SecondaryStat FROM Races WHERE Name = ?", (charRace,),).fetchall()

  #assign and improve stats
  for x in range(0,6):
    match orderOfStats[0][x]:
      case "str":
        if primaryStat[0][0] == "str":
          stren.setScore(statistics[x]+2)
        elif secondaryStat[0][0] == "str":
          stren.setScore(statistics[x]+1)
        else:
          stren.setScore(statistics[x])
      case "dex":
        if primaryStat[0][0] == "dex":
          dex.setScore(statistics[x]+2)
        elif secondaryStat[0][0] == "dex":
          dex.setScore(statistics[x]+1)
        else:
          dex.setScore(statistics[x])
      case "con":
        if primaryStat[0][0] == "con":
          con.setScore(statistics[x]+2)
        elif secondaryStat[0][0] == "con":
          con.setScore(statistics[x]+1)
        else:
          con.setScore(statistics[x])
      case "int":
        if primaryStat[0][0] == "int":
          intel.setScore(statistics[x]+2)
        elif secondaryStat[0][0] == "int":
          intel.setScore(statistics[x]+1)
        else:
          intel.setScore(statistics[x])
      case "wis":
        if primaryStat[0][0] == "wis":
          wis.setScore(statistics[x]+2)
        elif secondaryStat[0][0] == "wis":
          wis.setScore(statistics[x]+1)
        else:
          wis.setScore(statistics[x])
      case "cha":
        if primaryStat[0][0] == "cha":
          cha.setScore(statistics[x]+2)
        elif secondaryStat[0][0] == "cha":
          cha.setScore(statistics[x]+1)
        else:
          cha.setScore(statistics[x])

  #call assignModifiers function
  for x in range(6):
    sixStats[x].setModifier(sixStats[x].score)

  #testing - print scores
  print("Str:", stren.getScore())
  print("Dex:", dex.getScore())
  print("Con:", con.getScore())
  print("Int:", intel.getScore())
  print("Wis:", wis.getScore())
  print("Cha:", cha.getScore())
  print()
  
  #testing - print modifiers
  print("Str:", stren.getModifier())
  print("Dex:", dex.getModifier())
  print("Con:", con.getModifier())
  print("Int:", intel.getModifier())
  print("Wis:", wis.getModifier())
  print("Cha:", cha.getModifier())


#set the armour class function
def findingArmourClass(charClass, dex, con, wis):
  
  #Advanced Higher Concept - SQL Query
  classArmour = crs.execute("SELECT Armour FROM Classes WHERE Name = ?", (charClass,),).fetchall()
  
  #Advanced Higher Concept - SQL Query  
  armourType =  crs.execute("SELECT ArmourType FROM Classes WHERE Name = ?", (charClass,),).fetchall()
  
  if armourType[0][0] == "heavy":
    char.setArmourClass(classArmour[0][0])
  elif armourType[0][0] == "light" or (armourType[0][0] == "medium" and dex.getModifier() <=2):
    char.setArmourClass(classArmour[0][0]+dex.getModifier())
  elif armourType[0][0] == "con":
    char.setArmourClass(classArmour[0][0] + dex.getModifier() + con.getModifier())
  elif armourType == "wis":
    char.setArmourClass(classArmour[0][0] + dex.getModifier(0 + wis.getModifer()))
  else:
    char.setArmourClass(classArmour[0][0] + 2)


#close the program
def closeProgram():
  introApp.destroy()
  exit()

  
#Generate the 6 stats
def generateStats():
  #initalise the arrays
  temp = [0]*4
  rolledStats = [0]*6
  
  #loop for the 6 stats
  for x in range(6):
    
    #loop for the 4 dice in the array
    for y in range(4):
      
      #get a random number between 1 and 6
      temp[y] = random.randint(1,6)
    
      #sort the 4 numbers into order using the insertion sort module
    temp = insertionSort(temp)
    
    #add the 3 highest numbers together
    rolledStats[x] = temp[0] + temp[1] + temp[2]
  
    #sort the rolled stats into highest to lowest
  rolledStats = insertionSort(rolledStats)
  return (rolledStats)


#Advanced Higher Concept - insertion sort to sort array highest to lowest
def insertionSort(array):
  for x in range(1, len(array)):
    y = x
    while y > 0 and array[y-1] < array[y]:
      array[y-1], array[y] = array[y], array[y-1]
      y = y-1
  return array

  
#the window to input the name
def charNameWindowFunction():
  charNameWindow = Window(introApp, layout="grid", title="Character Builder - Name")
  
  #padding line
  padding = Text(charNameWindow, grid=[0,0], width=1, height=1, size=3)
  
  charNameMessage = "The name is what brings the character together. Some players use nouns or verbs. Some players use fantasy sounding names found online or in the DnD books. Some people translate words into other languages and use that because they sound cool. However you choose to do it, a character's name is often what defines them as a person. So choose wisely, young adventurer, because this might be the most important choice you'll ever make (probably not but there's a chance)."
  
  charNameText = Text(charNameWindow, text="Enter A Name:", grid=[1,1], align="left")
  charNameBox = TextBox(charNameWindow, grid=[1,2], align="left")
  charNameDescription = TextBox(charNameWindow, text=charNameMessage, multiline=True, grid=[1,3], height=10, width=50, enabled=False)
  submitCharNameButton = PushButton(charNameWindow, text="Submit", command=charNameValidation, grid=[1,4], args=[charNameBox])
  
  #text colour - red
  charNameDescription.text_color = "#ad1c11"

#validate that the character name is less than or equal to 12 characters
def charNameValidation(charName):
  if len(charName.value) > 12:
    introApp.warn("Name Too Long", "Please make the name 12 or less characters")
    return
    
  charNameInput(charName)

  
#set the name of the character
def charNameInput(inputtedName):
  char.setName(inputtedName.value)
  
  charDisplayFunction()

  #testing - print name
  print()
  print(char.getName())

  
#displaying the character at the end
def charDisplayFunction():
  charDisplayWindow = Window(introApp, layout="grid", title="Character Builder - Your Character")
  
  #padding line
  paddingLine = Text(charDisplayWindow, grid=[0,0], width=1, height=1, size=3)
  
  #name of character
  charNameDisplayText = Text(charDisplayWindow, text=char.getName(), grid=[1,1], align="left")
  
  #race and class of character
  charRaceText = Text(charDisplayWindow, text=char.getRace().title(), grid=[1,2], align="left")
  charClassText = Text(charDisplayWindow, text=char.getClass().title(), grid=[1,3], align="left")
  
  #padding line2
  padding2 = Text(charDisplayWindow, grid=[1,4])
  
  #Names of stats
  statTitleText = Text(charDisplayWindow, text="Stats",grid=[1,5], align="left")
  statListText = ListBox(charDisplayWindow, items=["Strength", "Dexterity", "Constituion", "Intelligence", "Wisdom", "Charisma"], width=80, height=100, grid=[1,6], align="left")
  
  #Scores of stats
  statScores = [0]*6
  for x in range(len(statScores)):
    statScores[x] = sixStats[x].getScore()
  scoresTitleText = Text(charDisplayWindow, text="Score", grid=[2,5], align="left")
  scoreListText = ListBox(charDisplayWindow, items=statScores, width=60, height=100, grid=[2,6], align="left")
  
  #Modifiers of Stats
  statModifiers = [0]*6
  for x in range(len(statModifiers)):
    statModifiers[x] = sixStats[x].getModifier()
  modifiersTitleText = Text(charDisplayWindow, text="Modifier", grid=[3,5])
  modifiersListText = ListBox(charDisplayWindow, items=statModifiers, width=70, height=100, grid=[3,6])

  #padding line #3
  padding3 = Text(charDisplayWindow, grid=[4,5], width=2)
  
  #Armour Class
  armourClassTitleText = Text(charDisplayWindow, text="Armour Class", grid=[7,2])
  armourClassTextBox = TextBox(charDisplayWindow, text=char.getArmourClass(), grid=[7,3], width=3)
  
  #pading line #4
  padding4 = Text(charDisplayWindow, grid=[6,5], width=1)
  
  #Speed
  speedTitleText = Text(charDisplayWindow, text="Speed", grid=[5,2])
  speedTextBox = TextBox(charDisplayWindow, text=str(char.getSpeed()) + "ft", grid=[5,3], width=4)
  
  #Hit Points
  hitPointsTitleText = Text(charDisplayWindow, text="Hit Points", grid=[5,5])
  hitPointsTextBox = TextBox(charDisplayWindow, text=char.getHitPoints(), grid=[5,6], align="top", width=3)
  
  #hitDice
  hitDiceTitleText = Text(charDisplayWindow, text="Hit Dice", grid=[7,5])
  hitDiceTextBox = TextBox(charDisplayWindow, text=char.getHitDice(), grid=[7,6], align="top", width=4)
  
  #Jump Height
  jumpHeightTitleText = Text(charDisplayWindow, text="Jump Height", grid=[5,6])
  jumpHeightTextBox = TextBox(charDisplayWindow, text=char.getJumpHeight(), grid=[5,6], width=3, align="bottom")
  
  #Jump Distance
  jumpDistanceTitleText = Text(charDisplayWindow, text="Jump Distance", grid=[7,6])
  jumpDistanceTextBox = TextBox(charDisplayWindow, text=char.getJumpDistance(), width=3, align="bottom", grid=[7,6])
  
  #padding line
  padding5 = Text(charDisplayWindow, grid=[1,7])
  
  #download character
  downloadButton = PushButton(charDisplayWindow, text="Download File", command=downloadCharacter, grid=[1,8], align="left", width=10)
  

#download the character to a file
def downloadCharacter():
  with open("Character - " + char.getName() + ".csv","w") as writefile:

    writefile.write("Character Name" + "," + char.getName() + "\n")
    writefile.write("Character Race" + "," + char.getRace() + "\n")
    writefile.write("Character Class" + "," + char.getClass() + "\n")
    
    writefile.write("Character Stats \n")
    writefile.write("Strength" + "," + str(stren.getScore()) + "," + str(stren.getModifier()) + "\n")
    writefile.write("Dexterity" + "," + str(dex.getScore()) + "," + str(dex.getModifier()) + "\n")
    writefile.write("Constitution" + "," + str(con.getScore()) + "," + str(con.getModifier()) + "\n")
    writefile.write("Intelligence" + "," + str(intel.getScore()) + "," + str(intel.getModifier()) + "\n")
    writefile.write("Wisdom" + "," + str(wis.getScore()) + "," + str(wis.getModifier()) + "\n")
    writefile.write("Charisma" + "," + str(cha.getScore()) + "," + str(cha.getModifier()) + "\n")
    
    writefile.write("Armour Class" + "," + str(char.getArmourClass()) + "\n")
    writefile.write("Hit Points" + "," + str(char.getHitPoints()) + "\n")
    writefile.write("Hit Dice" + "," + str(char.getHitDice()) + "\n")
    writefile.write("Jump Distance" + "," + str(char.getJumpDistance()) + "\n")
    writefile.write("Jump Height" + "," + str(char.getJumpHeight()) + "\n")
    writefile.write("Speed" + "," + str(char.getSpeed()) + "ft")

  #testing - file being written
  print("File Written")
      
  
#Main Program
  
#instantiate the class
char = Character()

#instantiate 6 stats
stren = stat()
dex = stat()
con = stat()
intel = stat()
wis = stat()
cha = stat()


#Advanced Higher Concept - Array of Objects
sixStats = [stren, dex, con, intel, wis, cha]


statistics = generateStats()
#testing - print rolled stats
print("Rolled Stats:")
print(statistics)
print()


#First Window
introApp = App(layout="grid", title="Character Builder - Intro")

#padding line
padding = Text(introApp, grid=[0,0], width=1, height=1, size=3)

introMessage = "Creating a Dungeons and Dragons Character can sometimes be a bit boring. There's a lot of rolling and number crunching and choices that really only have one option. So, this program is going to help YOU - yes YOU - make a Dungeons and Dragons Fifth Edition Character. Follow the instructions on the screen, and in less than a minute (unless you take longer) you will have a fully made, level 1 character."

introTextBox = TextBox(introApp, text=introMessage, multiline=True, height=9, width=50, grid=[1,1], enabled=False)
introQuestion = Text(introApp, text="Are you ready to make a character?", grid=[1,2])

yesButton = PushButton(introApp, text="Yes", command=raceWindowFunction, grid=[1,3], align="left", width=15)
noButton = PushButton(introApp, text="No", command=closeProgram, grid=[1,3], align="right", width=15)

#text colours - purple
introTextBox.text_color = "#8530db"
introQuestion.text_color = "#8530db"