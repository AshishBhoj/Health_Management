import datetime
def getdate():
    return datetime.datetime.now()

def update(n):
    if n == 1:
        a = int(input("Enter 1 for Food and 2 for Excercise : "))
        if a == 1:
            value = input("Enter Data\n")
            with open("Trevor_Food.txt","a") as op:
                op.write(str(str(getdate())) + ": " + value + "\n")
            print("Successfully Updated!!!")
        elif a == 2:
            value = input("Enter Data\n")
            with open("Trevor_Excercise.txt","a") as op:
                op.write(str(str(getdate())) + ": " + value + "\n")
            print("Successfully Updated!!!")

    elif n == 2:
        a = int(input("Enter 1 for Food and 2 for Excercise : "))
        if a == 1:
            value = input("Enter Data\n")
            with open("Mickel_Food.txt","a") as op:
                op.write(str(str(getdate())) + ": " + value + "\n")
            print("Successfully Updated!!!")
        elif a == 2:
            value = input("Enter Data\n")
            with open("Mickel_Excercise.txt","a") as op:
                op.write(str(str(getdate())) + ": " + value + "\n")
            print("Successfully Updated!!!")

    elif n == 3:
        a = int(input("Enter 1 for Food and 2 for Excercise : "))
        if a == 1:
            value = input("Enter Data\n")
            with open("Franklin_Food.txt","a") as op:
                op.write(str(str(getdate())) + ": " + value + "\n")
            print("Successfully Updated!!!")
        elif a == 2:
            value = input("Enter Data\n")
            with open("Franklin_Excercise.txt","a") as op:
                op.write(str(str(getdate())) + ": " + value + "\n")
            print("Successfully Updated!!!")

    else:
        print("Enter a Valid Option\n")

def retrive(n):
    if n == 1:
        a = int(input("Enter 1 for Food and 2 for Excercise : "))

        if a == 1:
            with open("Trevor_Food.txt") as op:
                for i in op:
                    print(i,end="")

        elif a == 2:
            with open("Trevor_Excercise.txt") as op:
                for i in op:
                    print(i,end="")

    elif n == 2:
        a = int(input("Enter 1 for Food and 2 for Excercise : "))

        if a == 1:
            with open("Mickel_Food.txt") as op:
                for i in op:
                    print(i, end="")

        elif a == 2:
            with open("Mickel_Excercise.txt") as op:
                for i in op:
                    print(i, end="")

    elif n == 3:
        a = int(input("Enter 1 for Food and 2 for Excercise : "))

        if a == 1:
            with open("Franklin_Food.txt") as op:
                for i in op:
                    print(i, end="")

        elif a == 2:
            with open("Franklin_Excercise.txt") as op:
                for i in op:
                    print(i, end="")

    else:
        print("Enter a Valid Option\n")

if __name__ == '__main__':

    restart = ('Y')
    while restart != ['n', 'N', 'no', 'NO']:
        print("Health Management Service ")
        option = int(input("Enter 1 to update data and 2 to retrive data : "))
        if option == 1:
            client = int(input("Enter 1 for Trevor and 2 for Mickel and 3 for Franklin : "))
            update(client)
        else:
            client = int(input("Enter 1 for Trevor and 2 for Mickel and 3 for Franklin : "))
            retrive(client)
        restart = input("Press Y to restart : ")
        if restart in ['n', 'N', 'no', 'NO']:
            print("Thank You")
            break
