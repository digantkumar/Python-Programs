# Storing the grades of students
# The student gets 1H if the percentage is greater than 70% and no less than 30% in any subject
# The student gets 2H if the percentage is greater than 60% but less than 70% and no less than 30% in any subject
# The student gets "PASS" if the percentage is greater than 40% but less than 60% and no less than 30% in any subject
# The student "FAILS" if the overall percentage is less than 40%
# Digant Kumar

def grade_points(students):
    print()
    #Pretty Printing
    print("%s %15s %15s %15s %15s %15s %13s %15s" %("ID","Last Name","First Name","ST4060","ST6030","CS6507","TOTAL","JUDGEMENT"))
    print("="*115)
    for stud in students:
        total = stud[3] + stud[4] + stud[5]  #Storing the total marks over the 3 subjects
        percentage = total/3                  #Calculating percentage
        print("%s %13s %10s %15s %15s %15s %15s" % (stud[0], stud[1], stud[2], stud[3], stud[4], stud[5], total),end=" ")
        all_pass = stud[3] >= 30 and stud[4] >= 30 and stud[5] >= 30
        if percentage > 70 and all_pass:        # If percentage > 70, 1H
            print("%12s" %("1H"))
        elif percentage > 60 and percentage < 70 and all_pass:     # Percentage>60 and <70, 2H
            print("%12s" %("2H"))
        elif percentage >= 40 and percentage <60 and all_pass:      # Percentage>40 and <60, PASS
            print("%12s" %("PASS"))
        else:
            print("%12s" %("FAIL"))                                 # Percentage<40 , FAIL
    return ""

students = [[123456,"Richarlison","Dick",75,90,80], [141451,"Thompson","Harry",40,50,40], [105126,"Harry","Larson",25,30,15],
            [204476,"Harry","Harriet",40,30,50], [541243,"Thompson","Tommy",50,50,25]]
print(grade_points(students))
