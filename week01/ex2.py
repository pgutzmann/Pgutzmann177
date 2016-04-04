import matplotlib.pyplot as plt

num_fail        = 0
num_outstanding = 0.
finalgrade      = []
hmwk            = [10., 10., 8., 9.5, 3., 9., 0., 6.] #these are the student's grades
midterm         = [10., 10., 10., 10., 8., 5., 10., 7.]
finalprj        = [9., 10., 10., 6., 10., 6., 8., 9.]

# calculating students grades
stu_num = 0
while (stu_num < 8):
    finalgrade.append((hmwk[stu_num] * .4 + midterm[stu_num] * .2 + finalprj[stu_num] * .4))
    print 'Student', stu_num + 1, 'final grade:', finalgrade[stu_num]
    stu_num += 1

# determining how many students failed
for stu_num in range(8):
    if (finalgrade[stu_num] < 6):
        num_fail += 1
print 'number of failed students:', num_fail

# determining how many students are outstanding
for stu_num in range(8):
    if (finalgrade[stu_num] > 9.5):
        num_outstanding += 1.
print 'fraction of outstanding students:', num_outstanding / 8.

# making histogram of grades
plt.hist(finalgrade)
plt.title("Student Grades")
plt.xlabel("Student's Grade")
plt.ylabel("Number of Students")
plt.savefig("Parker's Histogram.png")

