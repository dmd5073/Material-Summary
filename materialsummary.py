import csv
import sys
import math

class record :
    def __init__(self,qty,measurement,desc):
        try:
            self.qty = int(qty)
        except ValueError, TypeError:
            self.qty=getInt("Please entery a quantity",0)

        self.desc = str(desc)
        self.measurement = str(measurement)

def main (inputfilename,outputfilename):
    print inputfilename
    print outputfilename

    inputfile = open(inputfilename)
    reader = csv.reader(inputfile)

    qtyIdx = 0
    measurementIdx = 1
    descIdx = 2
    markNoIdx = 3

    fileData = dict()

    for line in reader:
        qty = line[qtyIdx]
        measurement = text(line[measurementIdx]).upper()
        desc = text(line[descIdx]).upper()

        if(line[markNoIdx].lower()=="x"):
            continue
        markNo = text(line[markNoIdx]).upper()

        print "        qty:"+str(qty)
        print "measurement:"+str(measurement)
        print "       desc:"+str(desc)
        print "     markNo:"+str(markNo)
        
        myRecord = record(qty, measurement, desc)
        if(markNo not in fileData):
            print "new mark number"
            fileData[markNo] = myRecord 
        else:
            print "not new mark number"
            decideOption("Which desc would you like to use?", myRecord.desc, fileData[markNo].desc)
            decideOption("Which measurement would you like to use?", myRecord.measurement, fileData[markNo].measurement)

            fileData[markNo].qty = fileData[markNo].qty + myRecord.qty
        
        print ""

    outputfile = open(outputfilename, 'w')
    writer = csv.writer(outputfile)
    for key in fileData:
        value = fileData[key]
        writer.writerow([value.qty, value.measurement, value.desc, key])
def text(string):
    string = str(string)
    if len(string)==0 or (string[0]!="'" and not (string[0]=='"' and string[len(string)-1]=='"')):
        string = "'"+string
    return string

def decideOption(prompt, opt1, opt2):
    if(opt1==opt2):
        return opt1
    else: 
        if len(opt1)>len(opt2):
            opt2 = opt2.ljust(len(opt1))
        if len(opt1)<len(opt2):
            opt1 = opt1.ljust(len(opt2))

        differences = ""
        for i in range(len(opt1)):
            if opt1[i] != opt2[i]:
                differences = differences + "^"
            else:
                differences = differences + " "

        print prompt
        
        width = 40
        numLines = int(math.ceil((float(len(opt1)))/width))
        for i in range(numLines):
            print "  1):"+opt1[i*width:(i+1)*width]
            print "  2):"+opt2[i*width:(i+1)*width]
            print "diff:"+differences[i*width:(i+1)*width]

        decision = getInt(prompt, 1, 2)
        if decision == 1:
            return opt1
        else:
            return opt2

def getInt(prompt, minVal=0, maxVal=sys.maxint):
    found = False
    while(not found):
        print prompt
        try:
            response = sys.stdin.readline()
            response = int(response)
            if response<minVal or response>maxVal:
                print "response out of bounds, try again"
            else:
                return response
        except:
            print "sorry, didn't catch that"
        
inputFileNameArg = 1
outputFileNameArg = 2
minargs = 3

if(len(sys.argv)<minargs):
  print "NOT ENOUGH ARGS PROVIDED, MIN ARGS IS "+str(minargs)
  print "proper format is 'python proc_materials_summary.py <filename>'"
  sys.exit()

main(sys.argv[inputFileNameArg], sys.argv[outputFileNameArg])
