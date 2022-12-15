import numpy as np
import matplotlib.pyplot as plt

m1=np.array([[1,2],[4,5]])
m2=np.array([[10,20],[40,50]])

print("The Matrices Are: ",m1,"\n",m2)
print("\nMatrix Operations")
print(" --------------- \n")
add=np.add(m1,m2)
sub=np.subtract(m1,m2)
mltpy=np.multiply(m1,m2)
division=np.divide(m1,m2)
tranm1=np.transpose(m1)
tranm2=np.transpose(m2)

print("SUM= ",add,"\nDifference= ",sub,"\nMultiplication= ",mltpy,"\nDivision= ",division,"\nTranspose Of m1= "
      ,tranm1,"T\nranspose Of m2= ",tranm2)
