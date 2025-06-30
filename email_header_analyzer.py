"""email_header_analyzer.py

CYBER SECURITY BOOTCAMP PROJECT
CCUBED

AUTHOR: Aliyah Ibrahim
VERSION 2025-June-29

PROJECT: Email Header Analyzer
PURPOSE: Determing the credibility of an email header by its analyzing the SPF, DKIM, and DMARC components.

   
"""

#importing all necessary packages and modules
import sys
import time
import colorama

#enabling colour format reset
colorama.init(autoreset = True)


def readHeader(fileName: str):
    """
    Purpose: Reads in file requested by the user.

    Parameters
    ----------
    fileName : str
        Name of the file containing the email header.

    Returns
    -------
    headerContents : TYPE
        the email header.

    """
    #implementing try except block to handle file missing events.
    try:
        myHeader = open(fileName +".txt")
        #read entire file into memory
        headerContents = myHeader.read()
        myHeader.close()
        print(colorama.Fore.GREEN + colorama.Style.BRIGHT+"File Found Successfully")
    except FileNotFoundError:
        #missing file.
        print (colorama.Fore.RED+ colorama.Style.BRIGHT+"File Not Found.".upper() +" Try checking to ensure file path is correct")
        nextChoice = input("Would you like to retry or return to main menu.\n1. Retry\n2. Display main menu\n")
        if (nextChoice == "1"):
            #retry
            headerContents = getContByF()
        else:
            displayMainMenu()
            
        
    return headerContents

def getLinesWithResult(headerContents: str):
    """
    
    Purpose: Extracts line from the email header. 
    Lines extracted are those that contain information about the 3 comoponents(i.e SPF, DKIM and DMARC)
    
    Parameters
    ----------
    headerContents : str

    Returns
    -------
    SPFLine : str
        Line containing SPF information
    DKIMLine : str
        Line containing DKIM information
    DMARCLine : str
        Line containing DMARC information.

    """
    SPFLine = ""
    DKIMLine = ""
    DMARCLine = ""
    
    headerContents = headerContents.splitlines()
    #getting rid of all spaces in lines.
    headerContents = [line.replace(" ", "") for line in headerContents]
    for line in headerContents:
        #print(line)
        if ("spf" in line.lower()):
            SPFLine = line
        if ("dkim" in line.lower()):
            DKIMLine = line
        if ("dmarc" in line.lower()):
            DMARCLine = line
    return (SPFLine, DKIMLine, DMARCLine)


def validateComponents(extractedLine: str, passWord: str):
    """
    Purpose: Checks the extracted lines to determine if components are valid.

    Parameters
    ----------
    extractedLine : str
        Line containing information
    passWord : str
        words required for component validity

    Returns
    -------
    result : int
        

    """
    #1 represents valid
    #0 represents not enough information
    #-1 represents invalid
    
    result = 0
    if extractedLine != "":
        #file info present
        if passWord.lower() in extractedLine.lower():
            #passed
            result = 1
        else:
            result = -1
    
    return result
  
def performValidation(extractedLine: tuple(), passWord: tuple()):
    """
    Purpose: performs validation on components and returns it along with a credibility score

    Parameters
    ----------
    extractedLine : tuple()
        DESCRIPTION.
    passWord : tuple()
        DESCRIPTION.

    Returns
    -------
    SPFValid : int
        Value representing SPF validity
    DKIMValid : int
        Value representing DKIM validity
    DMARCValid : int
        Value representing DMARC validity

    """
    SPFValid = validateComponents(extractedLine[0], passWord[0])
    DKIMValid = validateComponents(extractedLine[1], passWord[1])
    DMARCValid = validateComponents(extractedLine[2], passWord[2])
    
    #credidibily system. Each pass means added 33points. 1 point added if all 3 passed.
    credScore = 0;
    if SPFValid == 1:
        credScore+=33
    if DKIMValid == 1:
        credScore+=33
    if DMARCValid == 1:
        credScore+=33
    if credScore == 99:
        credScore+=1
    
    return (SPFValid, DKIMValid, DMARCValid, credScore)


def printResult(result: tuple, resultCorrelation: list[str]):
    """
    Purpose: Prints analysis results

    Parameters
    ----------
    result : tuple
        analysis result
    resultCorrelation : list[str]
        display for each result

    Returns
    -------
    None.

    """
    resultText = ""
    colorCode = [colorama.Fore.YELLOW, colorama.Fore.GREEN, colorama.Fore.RED]
    
    #pt1 = "The analyzed result is:"
    #resultText += pt1 + "\n"
    #print(colorama.Style.BRIGHT + pt1)
    #print(result)
    pt2 = f"SPF Component: {resultCorrelation[result[0]]}"
    resultText += pt2 +"\n"
    print(colorCode[result[0]] + colorama.Style.BRIGHT + pt2)
    pt3 = f"DKIM Component: {resultCorrelation[result[1]]}"
    resultText +=pt3 +"\n"
    print(colorCode[result[1]] + colorama.Style.BRIGHT + pt3)
    pt4 = f"DMARC Component: {resultCorrelation[result[2]]}"
    resultText +=pt4 +"\n"
    print(colorCode[result[2]] + colorama.Style.BRIGHT + pt4)

    colorCode2 = [colorama.Fore.RED, colorama.Fore.YELLOW, colorama.Fore.GREEN]
    pt5 = f"Credibility Score: {result[3]}"
    resultText += pt5 +"\n"
    print(colorCode2[(result[3]//33)-1] +  colorama.Style.BRIGHT + pt5)
    
    return resultText


def getContByT():
    """
    
    Purpose: returns email header from user
    Returns
    -------
    header : str

    """
    header = input("Please paste the email header:\n")
    return header
def getContByF():
    """
    Purpose: returns email header from file
    Returns
    -------
    header : str
    """
    print("Ensure your file is saved in the same location as the code or enter it with the file path.", end="\r")
    time.sleep(2)  

    sys.stdout.write("\033[2K\r")  

    fileName = input("Please enter your file name: ")
    
    
    #check for file success
    header  = readHeader(fileName)
   
    return header

def excecuteAnalysis():
    """
    
    Purpose: Excecutes header analysis
    
    Returns
    -------
    None.

    """
    passWord = "spf=pass", "dkim=pass", "dmarc=pass"
    resultCorrelation = ["Missing: Autentitcation data not available ", "Passed: Authentication Successful", "Failed: Authentication Failed"]
    
    analysisMethod = input("How would you prefer to enter the data\n1. File by file name\n2. Pasting it into the console\n")
    validTest = analysisMethod == "1" or analysisMethod == "2"
    choiceTrials = 7;
    while ((validTest == False) and choiceTrials > 1):
        choiceTrials-=1
        print(f"Invalid Input Choice. You have {choiceTrials} attemps remaining")
        excecuteAnalysis()
    if choiceTrials == 0 and validTest == False:
        print("You have run out of options. Returning to main menu.")
        displayMainMenu()
    
    if analysisMethod == "2":
        headerC = getContByT()
    else:
        print("Please ensure that headers are separated by \"#NEXT#\"")
        headerC = getContByF()
        
    splitHeadersByHash= headerC.split("#NEXT#")
    
    #creating file for result storage. time included to prevent overwritting
    analysisFileName = f"header_analysis_result_{int(time.time())}.txt"
    resultFile = open(analysisFileName, "w")
    
    #numOfHeaders = splitHeadersByHash.length()
    #performing autentication test
    
    counter = 1
    for header in splitHeadersByHash:
        print(f"\nHeader No. {counter} result")
        result = performValidation(getLinesWithResult(header), passWord)
        resultFile.write(printResult(result, resultCorrelation))
        counter+=1
    resultFile.close()
    print(f"\nAnalysis Completed. Result written to file - {analysisFileName}\n")
    return 

def excecuteDisplayR():
    """
    

    Returns
    -------
    int
        DESCRIPTION.

    """
    readMe = """
        """
    print(readMe)
    print ("Returning to main menu")
    displayMainMenu()
    return 

def chooseMenuItem(count: int):
    """
    

    Parameters
    ----------
    count : int
        DESCRIPTION.

    Returns
    -------
    displayAns : TYPE
        DESCRIPTION.

    """
    #print()
    displayAns = input("1. Analyze Header(s)\n2. Read Usage instructions \n3. Exit Program\n").upper()
    validTest = displayAns == "1" or displayAns == "2" or displayAns == "3"
    while ((validTest == False) and count > 1):
        count -= 1
        print(f"Invalid Input Choice. You have {count} attemps remaining")
        chooseMenuItem(count)
    if count == 0 and validTest == False:
        print("You have run out of options.")
        exitProgram()
    else:
        if displayAns == "1":
            excecuteAnalysis()
        elif displayAns == "2":
            excecuteDisplayR()
        elif displayAns == "3":
            exitProgram()
            
    return displayAns


def displayMainMenu():
    """
    

    Returns
    -------
    None.

    """
    numOfTries = 20
    chooseMenuItem(numOfTries)
    
    return

def displayIntro():
    print(f"Hello and Welcome! \nThis is an email header analyzer")
    print("Select options by entering their corresponding number")

def exitProgram():
    #initiating timed exit
    for i in range(3, 0, -1):
        print(f"Exiting the program in {i}...", end='\r')
        time.sleep(1)
        sys.stdout.write("\033[2K") 

    print("Goodbye! ")
    sys.exit()
    
def main():
    displayIntro()
    displayMainMenu()
    while(True):
        print("Select one\n")
        displayMainMenu()
    #displayMainMenu()
    

if __name__ == "__main__":
    main()


print("End of processing")