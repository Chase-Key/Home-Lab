name = input("What's your name? ")


with open("practice.txt", "a") as file:
    file.write(f"{name}\n")
"""
Reading CSV file (either to list or dictionary)
"""
#------------------------------------------
# to read each line (.rstrip() strips spaces we created when writing file)
with open("practice.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
#-----------------------------------------
#open file and print sorted version
names = []

with open("practice.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
#----------------------------------------
# read key, value format from csv file
with open("practice.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} lives in {house}")
#----------------------------------------
#print key,value by sorted sentence
peoples = []

with open("practice.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        peoples.append(f"{name} lives in {house}")



for people in sorted(peoples):
    print(people)
#----------------------------------------
#print sorted dictionary list from csv file
people = []

with open("practice.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        person = {"name": name, "house": house}
        people.append(person)


def get_name(person):
    return person["name"]


for person in sorted(people, key=get_name):
    print(f"{person['name']} lives in {person['house']}")
#----------------------------------------
# same code as above, but lambda is used to define the function
people = []

with open("practice.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        person = {"name": name, "house": house}
        people.append(person)

        #(lambda person:) is def person(): then return person["name"]
for person in sorted(people, key=lambda person: person["name"]):
    print(f"{person['name']} lives in {person['house']}")
#--------------------------------------
#same code as above, but using import csv to read the open(file)
#Using csv to read, will automatically split and strip
#now just append dict to list to sort.
#can't sort dictionary without adding a key=
#for key=, you need to define a function that returns either the -
#-name or house so sort can know what to sort by.
#Instead of using a one-line function, you can use lambda
import csv

people = []

with open("practice.csv") as file:
    reader = csv.reader(file)
    for name, house in reader:
        people.append({"name": name, "house": house})


for person in sorted(people, key=lambda person: person["name"]):
    print(f"{person['name']} lives in {person['house']}")
#----------------------------------------
#same code as above, but using csv.DictReader() to read file as dictionary
#when reading as dictionary, add column headers so Dict can read key, value pairs
import csv

people = []

with open("practice.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        people.append({"name": row["name"], "house": row["house"]})


for person in sorted(people, key=lambda person: person["name"]):
    print(f"{person['name']} lives in {person['house']}")
#--------------------------------------
"""
How to write to csv file, either as list or dictionary
"""
#write to csv using list
import csv

name = input("What's your name? ")
house = input("Where your house? ")

with open("practice.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, house])
#--------------------------------------
#write headers for Dictionary in CSV file
import csv

name = input("What's your name? ")
house = input("Where your house? ")

with open("practice.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "house"])
    writer.writerow({"name": name, "house": house})

#------------------------------------------

first = []
last = []
house = []
students = []
names = {}


if len(sys.argv) <= 2:
    sys.exit("Too few commands")
elif len(sys.argv) > 3:
    sys.exit("Too many commands")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a .csv file")
elif not sys.argv[2].endswith(".csv"):
    sys.exit("Not a .csv file")
else:
    with open(sys.argv[1], "r", newline='') as file:
        next(file)
        for line in file:
            row = line.rstrip().strip('"').split(",")
            last, first, house = row[0].strip(" "), row[1].strip('"').strip(" "), row[-1].strip(" ")
            student = (f'"{first}, {last}", {house}\n')
            #names = {"name": f'"{first}, {last}"}
            students.append(student)
        print(students)
    with open(sys.argv[2], "w", newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([f"'{first}, {last}', {house}\n"])


#---------------------------------------------------

    with open(sys.argv[1], "r", newline='') as file:
        next(file)
        for line in file:
            row = line.rstrip().strip('"').split(",")
            last, first, house = row[0].strip(" "), row[1].strip('"').strip(" "), row[-1].strip(" ")
            # student = (f'"{first}, {last}", {house}\n')
            name = f'{first}, {last}'
            # students.append(student)
    with open(sys.argv[2], "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "house"])
        writer.writeheader()
        writer.writerow({"name": name, "house": house})


#----------------------------------------------------------

first = []
last = []
house = []
students = []
names = {}


if len(sys.argv) <= 2:
    sys.exit("Too few commands")
elif len(sys.argv) > 3:
    sys.exit("Too many commands")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a .csv file")
elif not sys.argv[2].endswith(".csv"):
    sys.exit("Not a .csv file")
else:
    with open(sys.argv[1], newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for student in reader:
            last_name, first_name = student['name'].strip(" ").split(",")
            house = student['house'].strip(" ")
    with open(sys.argv[2], "a") as file:
        writer = csv.DictWriter(file, fieldnames=["first name", "last name", "house"])
        writer.writeheader()
        writer.writerow({"first name": first_name, "last name": last_name, "house": house})
