import csv
import sys

class record :
    def __init__(self,qty,measurement,desc):
        try:
            self.qty = int(qty)
        except ValueError, TypeError:
            self.qty=getInt("Please entery a quantity",0)

        self.desc = str(desc)
        print "desc:"+desc
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
        measurement = str(line[measurementIdx])
        desc = str(line[descIdx])
        markNo = line[markNoIdx]
        try:
            if markNo.lower() == "x":
                continue;
            markNo = int(markNo)
        except ValueError, TypeError:
            print "mark number:"+str(markNo)+" wasn't valid.  I QUIT!"
            sys.exit()

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
            if myRecord.desc!=fileData[markNo].desc:
                which = getInt("Which desc would you like to use?\n1)"+myRecord.desc+"\n2)"+fileData[markNo].desc, 1, 2)
                if(which==1):
                    fileData[markNo].desc = myRecord.desc

            if(myRecord.measurement!=fileData[markNo].measurement):
                which = getInt("Which measurement would you like to use?\n1)"+myRecord.measurement+"\n2)"+fileData[markNo].measurement, 1, 2)
                if(which==1):
                    fileData[markNo].measurement = myRecord.measurement

            fileData[markNo].qty = fileData[markNo].qty + myRecord.qty
        
        print ""

    outputfile = open(outputfilename, 'w')
    writer = csv.writer(outputfile)
    for key in fileData:
        value = fileData[key]
        writer.writerow([value.qty, value.measurement, value.desc, key])
        
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
