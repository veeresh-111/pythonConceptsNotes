
import sys
sys.path.append("C:/Users/hp/PycharmProjects/pythonProject/Day9/PackA")
sys.path.append("C:/Users/hp/PycharmProjects/pythonProject/Day9/PackB")

# Approach 1
# import emp
# empobj=emp.Employee(101,'john',50000)
# empobj.displayemp()
#
# import stu
# empobj=stu.Student(10,'scott','B')
# empobj.displaystu()

#Approach 2
from emp import *
empobj=Employee(101,'john',50000)
empobj.displayemp()

from stu import *
empobj=Student(10,'scott','B')
empobj.displaystu()
