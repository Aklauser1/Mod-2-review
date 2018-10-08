daysCounted = int(input("How many days of scores? "))
total = 0

for i in range(1, daysCounted + 1):
        days = int(input("Enter score for Day " + str(i) + ":"))
        if days >= 0:
            total = total + 1
        else:
            total = total - 1
print("The total score of the " + str(daysCounted) + " days is " + str(total))

