import os.path
import re
lines1 = ''
lines2 = ''
lines3 = ''

files_path = 'C:/Users/valmi/Desktop/Phaster Test Results/'
for filename in os.listdir(files_path):
    # specify the types of files we want this program to oversee
    if filename.__contains__('BB'):
        
        if filename.__contains__('summary'):
            with open("{}/{}".format(files_path, filename)) as Summary:
                lines1 = Summary.read().splitlines()
        if filename.__contains__('phage_regions'):
            with open("{}/{}".format(files_path, filename)) as DNA:
                lines2 = DNA.read().splitlines()
        if filename.__contains__('detail'):
            with open("{}/{}".format(files_path, filename)) as details:
                lines3 = details.read().splitlines()


SpeciesName = lines3[0]
m = re.search(' (.+?),', lines3[0])
if m:
    found = m.group(1)
    SpeciesName = found
for v,i in enumerate(lines2):
    NumberMatch = "0"
    starterNum = 0
    enderNum = 0
    if i.__contains__('>'):
        NumberMatch= i[1]
        for x,y in enumerate(lines1):
            if y.__contains__(NumberMatch + " "):
                if y.__contains__('intact'):
                    starterNum = y.index('intact')
                    enderNum = starterNum + 11
                    lines2[v] = ">" + " " + SpeciesName + " " + i[1:] + " " + y[starterNum:enderNum+1]

                elif y.__contains__('incomplete'):
                    starterNum = y.index('incomplete')
                    enderNum = starterNum + 16
                    lines2[v] = ">" + " " + SpeciesName + " " + i[1:] + " " + y[starterNum:enderNum+1]

                elif y.__contains__('questionable'):
                    starterNum = y.index('questionable')
                    enderNum = starterNum + 17
                    lines2[v] = ">" + " " + SpeciesName + " " + i[1:] + " " + y[starterNum:enderNum+1]

MyFile3= open(files_path + " " + SpeciesName + ' OUTPUT' + '.txt','w')



for e in lines2:
    MyFile3.write(e)
    MyFile3.write('\n')
MyFile3.close()
