#Variant #13
import matplotlib.pyplot as plt
import random

realArea = 7
totalArea = 16
x_array = []
y_array = []
appr_area_array = []
error_array = []
i_array = []

def default_figure():
    col = "#E35233"
    plt.plot([0, 0.25, 0.5, 0.75, 1], [0, 1, 2, 3, 4], color = col)
    plt.plot([1, 1, 1], [4, 3, 2], color = col)
    plt.plot([1, 2, 3], [2, 2, 2], color = col)
    plt.plot([3, 3, 3], [2, 3, 4], color = col)
    plt.plot([3, 3.25, 3.5, 3.75, 4], [4, 3, 2, 1, 0], color = col)
    plt.plot([0, 1, 2], [0, 0, 0], color = col)
    plt.plot([2, 2], [0, 1], color = col)
    plt.plot([2, 3], [1, 1], color = col)
    plt.plot([3, 3], [0, 1], color = col)
    plt.plot([3, 4], [0, 0], color = col)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Target function")
    plt.show()

def monte_carlo(iterations):
    n = iterations
    goal = 0
    
    for i in range(1, n + 1):
        x = round(random.uniform(0, 4), 3)
        y = round(random.uniform(0, 4), 3)
        if (((x >= 1) and (x <= 2)) and ((y >= 0) and (y <= 2))) or (((x >= 2) and (x <= 3)) and ((y >= 1) and (y <= 2))) or (((x >= 0) and (x <= 1)) and ((y >= 0) and (y <= 4*x))) or(((x >= 3) and (x <= 4) and ((y >= 0) and (y <= -4*x + 16)))):
            goal += 1
        appr_area = (goal * totalArea) / i
        error = abs(realArea - appr_area) / realArea * 100
        x_array.append(x)
        y_array.append(y)
        appr_area_array.append(appr_area)
        error_array.append(error)
        i_array.append(i)
        
    print(f"Goals: {goal} / {n}\nApproximate area: {round(appr_area_array[-1], 3)}\nReal area: {realArea} ({round(error_array[-1], 3)}% fault)")
default_figure()
monte_carlo(3000)
