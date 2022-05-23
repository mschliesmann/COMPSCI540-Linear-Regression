import sys
import csv
import matplotlib.pyplot as plt
import numpy as np
        
#Q2
def question2():
    file = open(sys.argv[1])
    csv_reader = csv.reader(file)
    next(csv_reader)

    x = []
    y = []
    for row in csv_reader:
        x.append(int(row[0]))
        y.append(int(row[1]))

    plt.plot(x, y)
    plt.xlabel("Year")
    plt.ylabel("Number of frozen days")
    plt.savefig("plot.jpg")
    plt.show()

#Q3, Q4, Q5, & Q6
def question3_4_5_6():
    file = open(sys.argv[1])
    csv_reader = csv.reader(file)
    next(csv_reader)

    x = []
    y = []
    for row in csv_reader:
        x.append(int(row[0]))
        y.append(int(row[1]))
    
    #Q3a
    print("Q3a:")
    xArray = []
    for point in x:
        xArray.append([1,point])
    xMatrix = np.array([xArray]).reshape((len(x),2))
    print(xMatrix)

    #Q3b
    print("Q3b:")
    yMatrix = np.array(y)
    print(yMatrix)

    #Q3c
    print("Q3c:")
    Z = np.dot(np.transpose(xMatrix), xMatrix)
    print(Z)

    #Q3d
    print("Q3d:")
    I = np.linalg.inv(Z)
    print(I)

    #Q3e
    print("Q3e:")
    PI = np.dot(I, np.transpose(xMatrix))
    print(PI)

    #Q3f
    print("Q3f:")
    hat_beta = np.dot(PI, yMatrix)
    print(hat_beta)
    
    #Q4
    x_test = 2021
    y_test = hat_beta[0] + (hat_beta[1] * x_test)
    print("Q4: " + str(y_test))

    #Q5a
    hat_beta1 = hat_beta[1]
    print("Q5a: " + "<")

    #Q5b
    print("Q5b: " + "Because this value is negative, this means there will be fewer Mendota ice days for the winter of 2021-22 than previous data trends.")
    
    #Q6a
    prediction_year = (hat_beta[0])/(-hat_beta[1])
    print("Q6a: " + str(prediction_year))

    #Q6b
    print("Q6b: Given the behavior of the linear regression, it makes sense 2455 is predicted as the first year with no frozen lake days. According to the dataset, as time progresses, the number of ice days are slowly decreasing. Therefore, it can be compelling to say that based on the trends in the linear regression, at year 2455, Mendota will not freeze over.")

question2()
question3_4_5_6()