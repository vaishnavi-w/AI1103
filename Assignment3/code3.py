import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

# For plotting the CDF of Z
# Setting the corresponding x and y - coordinates
# Region 1 of CDF
x_1 = np.arange(-1, 1, 0.01)
y_1 = x_1*0
# Region 2 of PDF
x_2 =   np.arange(1, 2, 0.01)
y_2=  (x_2**2-2*x_2+1)/2
# Region 3 of PDF
x_3 =   np.arange(2, 3, 0.01)
y_3=  (6*x_3-x_3**2-7)/2
# Region 4 of PDF
x_4 =   np.arange(3, 5, 0.01)
y_4=  x_4**0

# Plotting the points
plt.plot(x_1, y_1,'b')
plt.plot(x_2, y_2,'b')
plt.plot(x_3, y_3,'b')
plt.plot(x_4, y_4,'b')

plt.xlabel('Random Variable , X')
plt.ylabel('$F_{X}(x)$')

# function to show the plot
plt.grid()
plt.show()

# For plotting the PDF of Z
# Setting the corresponding x and y - coordinates
# Region 1 of PDF
x_1 = np.arange(-1, 1, 0.01)
y_1 = x_1*0
# Region 2 of PDF
x_2 =   np.arange(1, 2, 0.01)
y_2=  x_2 - 1
# Region 3 of PDF
x_3 =   np.arange(2, 3, 0.01)
y_3=  3-x_3
# Region 4 of PDF
x_4 =   np.arange(3, 5, 0.01)
y_4=  x_4*0


# Plotting the points
plt.plot(x_1, y_1,'b')
plt.plot(x_2, y_2,'b')
plt.plot(x_3, y_3,'b')
plt.plot(x_4, y_4,'b')

plt.xlabel('Random Variable , X')
plt.ylabel('$P_{X}(x)$')

# function to show the plot
plt.grid()
plt.show()