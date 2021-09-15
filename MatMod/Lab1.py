import math
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

water = list(np.float_([0.024,0.038,0.04,0.045,0.047,0.0578,0.0629,0.0629,0.063,0.064,0.0678,0.0691,0.071,0.0742,0.0752,0.077,0.0779,0.0781,0.0787,0.0789,0.0791,0.0862,0.0867,0.0877,0.089,0.0897,0.096,0.098,0.099]))
hair = list(np.float_([11.7,12.7,15.5,16.8,16.7,17.5,18.5,18.7,18.8,19.5,20.8,20.3,23.3,23.2,23.7,24.4,28.9,25.8,29.5,23.3,22.5,26.2,29.7,33.8,35,32,40,41,43.8]))

length = len(hair)


sum_powers = 0
for i in water:
    sum_powers += pow(i,2)


sum_water = np.sum(water)
sum_hair = np.sum(hair)
average_water = sum_water / len(water)
average_hair = sum_hair / len(hair)


print("average value for xi & yi ", average_water, average_hair)

sum_mult = 0

for i in range(length):
    sum_mult += hair[i] * water[i]
print("Sum of Xi*Yi = ", sum_mult)


corellation_coef = 0
l = 0
v = 0

for i in range(length):
    corellation_coef += ( water[i] - average_water ) * ( hair[i] - average_hair )
    l += pow(water[i] - average_water, 2)
    v += pow(hair[i] - average_hair, 2)


corellation_coef = corellation_coef / ( math.sqrt(l) * math.sqrt(v) )
print("Corellation coef = ", corellation_coef)
  

##linear system

M1 = np.array( [[29, sum_water], [ sum_water, sum_powers ]] )
V1 = np.array( [sum_hair, sum_mult ] )
koef = np.linalg.solve( M1,V1 )

print("Linearity coef = ", np.linalg.solve(M1,V1))

water_reshaped = np.array(water).reshape(-1,1)

#linear model
def linear_model(water, water_reshaped, hair):
    linear_model = LinearRegression()
    linear_model.fit(water_reshaped, hair)
    hair_linear_pred = linear_model.predict(water_reshaped)

    plt.plot(water, hair, 'co')
    plt.plot(water, hair_linear_pred)
    plt.title('Linear Model')
    plt.show()

    print('Coefficient of determination:', linear_model.score(water_reshaped, hair))

#polynomial model
def polynomial(water, water_reshaped, hair):
    transformer = PolynomialFeatures(degree = 2, include_bias = False)
    transformer.fit(water_reshaped)
    water_polynomial = transformer.transform(water_reshaped)
    polynomial_model = LinearRegression().fit(water_polynomial, hair)
    hair_polynomial_pred = polynomial_model.predict(water_polynomial)


    plt.plot(water, hair, 'co')
    plt.plot(water, hair_polynomial_pred)
    plt.title('Polynomial Model')
    plt.show()

    print('Coefficient of determination:', polynomial_model.score(water_polynomial, hair))

#logariphmical model
def logar(water ,water_reshaped, hair):
    xlog_logarithmic = np.log(water_reshaped)
    logarithmic_model = LinearRegression()
    logarithmic_model.fit(xlog_logarithmic, hair)

    y_logarithmic_pred = logarithmic_model.predict(xlog_logarithmic)

    plt.plot(water, hair, 'co')
    plt.plot(water, y_logarithmic_pred)
    plt.title('Logarithmic Model')
    plt.show()

    print('Coefficient of determination:', logarithmic_model.score(xlog_logarithmic, hair))

def exponential(water ,water_reshaped, hair):
    
    ylog_exponential = np.log(hair)

    # y = Aexp(-BX) ==> ln(Y) = ln(A) - BX
    exponential_model = LinearRegression()
    exponential_model.fit(water_reshaped, ylog_exponential)

    y_exponential_pred = np.exp(exponential_model.predict(water_reshaped))

    plt.plot(water, hair, 'co')
    plt.plot(water, y_exponential_pred)
    plt.title('Exponential Model')
    plt.show()


    print('Coefficient of determination:', exponential_model.score(water_reshaped, ylog_exponential))

##Uncomment needed model to see it's shape

#linear_model(water, water_reshaped, hair)
#polynomial(water, water_reshaped, hair)
#logar(water, water_reshaped, hair)
#exponential(water, water_reshaped, hair)