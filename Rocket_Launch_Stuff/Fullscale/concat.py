
import glob
import os

dir = 'C:/git_repos/Python/Rocket_Launch_Stuff/Fullscale'
CPX1 = dir + '/CPX1/'
CPX2 = dir + '/CPX2/'
CPX3 = dir + '/CPX3/'
CPX4 = dir + '/CPX4/'

#print(dir)
#print(CPX1)
#print(CPX2)
#print(CPX3)
#print(CPX4)

with open("concatenated4.txt", 'w') as outfile:
    for files in sorted(glob.glob(CPX4 + '*.txt'), key=os.path.getmtime):
        with open(files) as infile:
            print(files)
            for line in infile:
                outfile.write(line)
                
print("done")