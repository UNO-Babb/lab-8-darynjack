#ProcessData.py
#Name:
#Date:
#Assignment:

import random
def makeID(first, last, ID):
  userID = first[0] + last +ID[8:]

  return userID

def makeMajorYear(major, year):

  if year == "Freshman":
    year = "Fr"
  if year == "Sophomore":
    year = "So"
  if year == "Junior":
    year = "Jr"
  if year == "Senior":
    year = "Sr"
 
  majorYear = major[0:3] + year
 
  return majorYear

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  output = ""
  for student in inFile:
    data = student.split()
  # print(data)
    userID = makeID(data[0], data[1], data[3])
    print(userID)
    majorYear =makeMajorYear(data[6], data[5])
    print(majorYear)

    output += data[1] + "," + data[0] + "\n"
  outFile.write(output)
 
  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
