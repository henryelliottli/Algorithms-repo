names = (input("Enter names, separated by commas\n") or "hl,gj,as").title() # get and process input for a list of names
assignments =  (input("Enter assignment counts, separated by commas\n") or "23,10,4")# get and process input for a list of the number of assignments
grades = (input("Enter grades, separated by commas\n") or "89,19,23")  # get and process input for a list of grades

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"
names_separate = names.split(",")
assignments_separate = assignments.split(",")
grades_separate = grades.split(",")
grades_max = [ str(2*int(assignments_separate[x]) + int(grades_separate[x])) for x in range(len(assignments_separate))]

#print("{} hello {}{} {}".format(names_separate[0],assignments_separate[0],grades_separate[0],grades_max[0]))

for i in range(len(names_separate)):
    print(message.format(names_separate[i],assignments_separate[i],grades_separate[i],grades_max[i]))

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
