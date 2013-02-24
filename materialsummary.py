import csv
import sys

def main (inputfilename,outputfilename):
    print inputfilename
    print outputfilename

    csvfile = open(inputfilename)
    reader = csv.reader(csvfile)

    qtyIdx = 0
    measurementIdx = 1
    descIdx = 2
    markNoIdx = 3

    for line in reader:
        print "        qty:"+str(line[qtyIdx])
        print "measurement:"+str(line[measurementIdx])
        print "       desc:"+str(line[descIdx])
        print "     markNo:"+str(line[markNoIdx])
        print ""

inputFileNameArg = 1
outputFileNameArg = 2
minargs = 3

if(len(sys.argv)<minargs):
  print "NOT ENOUGH ARGS PROVIDED, MIN ARGS IS "+str(minargs)
  print "proper format is 'python proc_materials_summary.py <filename>'"
  exit()

main(sys.argv[inputFileNameArg], sys.argv[outputFileNameArg])


