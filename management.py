# Inventory Management Program
"""
Implement a Tracking system program;
Prompt user for a Unique Identification Number(UIN).
Once entered, a profile of (Strain Identity, UIN, Batch#, Test Results, position).
This info will populate for user and re-prompt user for another UIN.

-Add a choice to enter a new UIN profile.

# d = {'foo': 1, 'bar': 2, 'baz': 3}
# for k, v in d.items():
#     print('k =', k, ', v =', v)
#
k = foo , v = 1
k = bar , v = 2
k = baz , v = 3
"""


class Plant:
    def __init__(self, strain, strain_class, uin, batch, location, test):
        self.strain = strain
        self.strain_class = strain_class
        self.uin = uin
        self.batch = batch
        self.location = location
        self.test = test

    def plant_id(self):
        print("Name: {}\nStrain: {}\nUIN: {}\nBatch#: {}\nLocation: {}\nTest: {}".format(self.strain,
                                                                                                 self.strain_class,
                                                                                                 self.uin,
                                                                                                 self.batch,
                                                                                                 self.location,
                                                                                                 self.test))


def main_menu():
    print("a) Add Plant")
    print("b) Review Plant")
    print("c) Delete Plant")


p4 = Plant("Acai Berry Gelato", "Sativa", "00004", "0001-0722", "Harvest Room 1", "26% & 2.32%")
p5 = Plant("Purple Kush", "Indica", "00005", "0001-0722", "Harvest Room 1", "N/A")


def main():
    while True:
        # [Beginning] - Main Menu, Enter input
        main_menu()
        u = input("Main Menu: ")
        if u == "".strip(" "):
            continue
        elif u == "a".lower():
            print("To add Plant,\n"
                  "input: Name, Strain, UIN, Batch, Location, Test")
            x = input("Add Plant: ")
            x = x.Plant()
        elif u == "b".lower():
            print("Input UIN # of plant.")
            x = input("UIN: ")
            print()



main()


# Creating file.text for Inventory Management Program
employees = {}
name = input("Enter Name: ")
salary = input("Enter Salary: ")
employees[name] = salary
#print(employees)

# Write Dictionary to .txt file
with open('scratch_3.txt', 'a') as data:
    data.write("{}\n".format(str(employees)))

# Open .txt file and Convert .txt file to Dictionary
#dictionary = {}
#with open("scratch_3.txt", 'r') as file:
    #for line in file:
        #(key, value) = line.split("\n")

        #employees[key] = value
f = open('scratch_3.txt', 'r')
print(f.read())
f.close()