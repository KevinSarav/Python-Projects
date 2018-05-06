""" Kevin Saravia, PeopleSoft ID: 1478627
    Program #2: Calculating Life Signs
    COSC 1306, Fall 2017
    This program computes breaths and heartbeats from age."""

age = float(input("Enter age: "))                        #input age as a float

if age < 0.083 :                                         #if age < 0.083, which is 1 month of a year, set bpm to 30-60
    bpmLo = 30
    bpmHi = 60
elif 0.083 <= age < 0.5 :                                #if 0.083 <= age < 0.5, which is 1 - 6 months,
    bpmLo = 30                                           #set bpm to 30 - 50
    bpmHi = 50
elif 0.5 <= age < 1 :                                    #if 0.5 <= age < 1, which is 6 months - 1 year,
    bpmLo = 24                                           #set bpm to 24 - 46
    bpmHi = 46
elif 1 <= age < 4 :                                      #if 1 <= age < 4, set bpm to 20 - 30
    bpmLo = 20
    bpmHi = 30
elif 4 <= age < 6 :                                      #if 4 <= age < 6, set bpm ti 20 - 25
    bpmLo = 20
    bpmHi = 25
elif 6 <= age < 12 :                                     #if 6 <= age < 12, set bpm to 16 - 20
    bpmLo = 16
    bpmHi = 20
else :                                                   #else, which is if 12 <= age, set bpm to 12 - 16
    bpmLo = 12
    bpmHi = 16

totalMinutes = age * 365 * 24 * 60                       #age * 365 gets days lived, * 24 gets hours, * 60 gets minutes
totalBreathsLo = int(bpmLo * totalMinutes)               #gets minimum bpm by multiplying bpmLo by totalMinutes
totalBreathsHi = int(bpmHi * totalMinutes)               #gets maximum bpm by multiplying bpmHi by totalMinutes

totalHeartBeats = int(67.5 * totalMinutes)               #gets heartbeats by multiplying totalMinutes by 67.5 bps

print("Number of breaths to date is : ",                 #prints minimum to maximum breaths in inputted age's lifetime
      totalBreathsLo, "-", totalBreathsHi, "breaths")
print("Number of heart beats to date is : ",             #prints heartbeats in inputted age's lifetime
      totalHeartBeats, "heartbeats")