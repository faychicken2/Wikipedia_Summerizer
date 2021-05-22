# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 18:01:36 2020

@author: hawk

TODO:
    ~fix summary bug that summarizes somthing else
    ~do a try except for the summary function ( https://stackoverflow.com/questions/25946692/wikipedia-disambiguation-error ) 
    
    pass content into the summerize function
    
    
    
"""
 # summarizer libraries 
import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

import keyboard


import wikipedia
import random
import pyttsx3
import sys
import json
import time


# lists of People

#line function
def line():
    line = print("_" * 100, "\n")

#this is the main function where the program starts
def main(): 
    #start of output
    #make a line
    line()
    
    #asking user for input
    opt1 = input("""what do you what to look up?
                 
Just start typing to lookup somthing.

or type "im feeling lucky"

""" )

    #print a line
    #make opt1 lowwer case
    opt1 = opt1.lower()
    
    
    #logic
    if opt1 == "im feeling lucky":
        ImFeelingLucky()
    else:
        wikiSearch = Search(opt1)
        print(wikiSearch)
        logic(wikiSearch, opt1)
        
    
            

def RNG(Low, High):
    
    RNG = random.randint(Low, High)
    return RNG

def logic(opt1, objectBeingSearched):
    #pages
    line()
    wikiPages = opt1 #Pages(opt1)
    print("*** Page ***")
    print("page ", wikiPages)
    
    #content
    content = Content(opt1)
    
    # summary 
    summySummary = summerize_the_research(content, objectBeingSearched)
    print(summySummary, "test")
    TTS(summySummary)
    
    opt2 = input("do you want references? (y/n) ")
    opt2.lower() 
    
    if opt2 == "y":
        references(opt1)
    
        
    


def DisambiguationErrorView(Input, errInput):
    line()
    # print("\nThere was an error with" , Input, "\n")
    print(Input, "is ambiguous and could mean a lot. What did you mean?")
    #making the errInput a list
    errOptions = errInput.options
    #incrmenting a number to display to user
    incrmenting = 1
    
    #this sleeps for X seconds
    #time needs to be imported to work
    time.sleep(3)
    #This for loop prints the errOptions list one at a time
    for x in errOptions:
        print(incrmenting, x)
        incrmenting += 1
        
    #ask the user what they want to look up.
    #if they dont use a number try again
    
    while True:
        try:
            UserInput = int(input(" 'Use the number to select' "))
            break
        except ValueError:
            print("Please use the number")
            continue
    #pulling what the user wants from the list
    #we - 1 because computers start at 0
    #EX: user wants displayed index 3 that would be 2 in the list
    userChoice = errOptions[UserInput-1]
    wikiPages = Pages(userChoice)
    return wikiPages



def Summaryold(Input):
    #getting a summary from the input
    try:
        i = wikipedia.summary(Input, sentences=0, chars=0, auto_suggest=False, redirect=True)
        return i
    
    except wikipedia.DisambiguationError as err:
        # line()
        # print("\nThere was an error summarizing" , Input)
        # print("\n", Input, " is ambiguous and could mean a lot. What did you mean?")
        # print("\n\nError", e)
        
        DisambiguationErrorView(Input, err)
        
        # incrmenting = 1
        # errOptions = err.options
    
        # for x in errOptions:
        #     print(incrmenting, x)
        #     incrmenting += 1
        
        




def Pages(Input):
    #getting a page from the input
    try:
        i = wikipedia.page(Input, auto_suggest=False)
        return i
    except wikipedia.DisambiguationError as e:
        #calling the line function to draw a line
        line()
        i = DisambiguationErrorView(Input, e)
    return i

def references(Input):
    #geting a referance
    i = Input.references()
    return i

def Content(Input):
    #getting content
    i = Input.content
    return i

def Search(Input):
    
    #search function
    wikiSearch = wikipedia.search(Input)      
    #increment i
    i = 1
    #print the list to the user
    for y in wikiSearch:
        print(i, y)
        i += 1
        
    #ask what the user whats to look up
    print("\nWhat to you want to search?")
    
    #while true run loop true = no errors
    while True:
        try:
            x = int(input(" 'Use the number to search' "))
            break
        except ValueError:
            print("Please use the number")
            continue

    
    #pulls what the user wants to look up
    #subtracts 1 because computers start counting at 0 not 1
    searched = wikiSearch[x-1]
    output = Pages(searched)
    
    
    #returns what the user whats to search
    return output

def ImFeelingLucky():
    #list of people
    People = ['Marilyn Monroe', 'Abraham Lincoln', 'Nelson Mandela', 'John F. Kennedy',
              'Martin Luther King', 'Queen Elizabeth', 'Winston Churchill', 'Donald Trump',
              'Bill Gates', 'Muhammad Ali', 'Mahatma Gandhi', 'Mother Teresa', 'Christopher Columbus',
              'Charles Darwin', 'Elvis Presley', 'Albert Einstein']
    
    #list of places    
    Places = ['Statue of Liberty', 'Eiffel Tower', 'Big Ben', 'Leaning Tower of Pisa',
              'Colosseum', 'Empire State Building', 'Hollywood Sign', 'Golden Gate Bridge',
              'Notre Dame', 'Tokyo Tower', 'London Eye', '''St. Peter's Basilica''',
              'Sagrada Familia', 'Sagrada Familia', 'Great Wall of China', 'Sydney Opera House']
    
    
    ListPicker =  RNG(0,2)
    
    # print(ListPicker)
    try:
        if ListPicker == 0:
            listLen = len(People)
            I = RNG(0, listLen)
            summ = People[I]
            logic(summ)
            # print(summ + "\n")
            # print(wikipedia.summary(summ))
            # TTS(wikipedia.summary(summ))
            
        elif ListPicker == 1:
            listLen = len(Places)
            I = RNG(0, listLen)
            summ = Places[I]
            logic(summ)
            # print(summ + "\n")
            # print(wikipedia.summary(summ))
            # TTS(wikipedia.summary(summ))
            
        elif ListPicker == 2:
            print(" ")
            i = wikipedia.random()
            line()
            print(i, "\n")
            logic(i)
            
            
    except KeyboardInterrupt:
        # quit
        sys.exit()



def openTextFile():
    # with open("wiki.txt", "r+") as a
    with open('data.txt', 'a') as f:
        return f
    



def TTSSettings():
    
    engine = pyttsx3.init() # object creation
    
    """ RATE"""
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    print (rate)                        #printing current voice rate
    engine.setProperty('rate', 125)     # setting up new voice rate
    
    
    """VOLUME"""
    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    print (volume)                          #printing current volume level
    engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
    
    """VOICE"""
    voices = engine.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
    
    engine.say("Hello World!")
    engine.say('My current speaking rate is ' + str(rate))
    engine.runAndWait()
    engine.stop()
    
    """Saving Voice to a file"""
    # On linux make sure that 'espeak' and 'ffmpeg' are installed
    engine.save_to_file('Hello World', 'test.mp3')
    engine.runAndWait()

#TTS Code
def TTS(Input):
    #Starting the lib
    engine = pyttsx3.init()
    try:
        #computer says Input
        engine.say(Input)
        engine.runAndWait()
    except keyboard.is_pressed:   
        print("ctrl was pressed")
        engine.stop()
        sys.exit()
        
        
        
        



def WriteToFile(InputStr):
    with open("data.txt", "a") as data:
        InputStr.write()
        data.close()
        
        f = open("demofile2.txt", "a")
        f.write("Now the file has more content!")
        f.close()

def ReadFromFile(fileName):
    
    with open(str(fileName), "r") as data:
        readData = data.read()
        return readData

def summerize_the_research(dataToSumm, objectBeingSummed):
   #dataToSumm is the data passes in to summarize
    
    # where the summerizing happens
    parser = PlaintextParser.from_string(dataToSumm, Tokenizer("english"))
    # print("\n\n\t\t *** Summerize the above info ***\n\n")
    #which summ do we want summy to use
    # use lexrank - one algorithum to summ data
    summarizer = LexRankSummarizer()
    #how many sentences do we want to summ
    number_of_Sentances = 4
    #this is there the summerizer does the work for you.
    summary = summarizer(parser.document, number_of_Sentances)
    
    # print out our resault
    print("\n\n\t\t *** Summarized ", objectBeingSummed, " ***\n\n " )
    for sentence in summary:
        print(sentence)
        
    return summary    
        
        #print summ to file
    # ExportFile = open("sumData.txt", "w")
    
    # return ExportFile.write(summary)


if __name__ == "__main__":
    '''check if we have a main function if we do run it. '''
    
    #x = Pages("lams")
    #logic(x)   
 
    main()
    

