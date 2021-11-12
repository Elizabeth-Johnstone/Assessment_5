log_file = open("um-server-01.txt")
# This is allowing us to access the data in um-server-01.txt

def sales_reports(log_file):
# This is creating a function and passing in the file name as a parameter
    for line in log_file:
# This is looping through the file data
        line = line.rstrip()
# This removes whitespace at the end of the sting
        day = line[0:3]
# This is creating a variable called "day" and assigning it to the 0th value of each line. It is also limiting it to a length of 3 characters.
        if day == "Mon":
            print(line)
# This is printing all of the lines where day = "Tue"

sales_reports(log_file)

# Extra credit:

def deliveries(log_file):
        for line in log_file:
                splitted = line.split(' ')
                melons = splitted[2]
                if int(melons) > 10:
                        print(line)

deliveries(log_file)