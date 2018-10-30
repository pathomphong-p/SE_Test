from NextdayCal import cal_next_day
task = []
with open("DataTestNextday.txt", "r") as f:
    correct = 0
    for line in f:
        task=line.strip()

        data  = task.split(" ")

        month = data[0]
        day = data[1]
        year = data[2]
        testResult = data[3]
        
        if cal_next_day(month,day,year) == testResult :
            print (month,day,year,"correct!!")
            correct = correct+1
        else :
            print (month,day,year,"fail!!")
            ans_cal = cal_next_day(month,day,year)
            print("Test:", testResult, "Cal:", ans_cal)
    print("Total Correct Test Case:", correct)