# libraries
import matplotlib.pyplot as plt
import numpy as np
import random

# data initialization
capital = 1000.0
riskPerc = 1.0
successRate = 0.4
failureRate = 0.6
riskRewardRatio = 1.8

# temporary variables
expectancy = successRate * riskRewardRatio - failureRate
maxCapital = 0.0
maxDrawdown = 0.0

values = []
values.append(capital)

# prob is in decimal form, 30% is 0.30 
def probability(prob):
    tmp = prob * 1000
    if (random.randint(1, 1000) <= tmp):
        return True
    return False

# create data
for i in range(1000):
    if probability(successRate) == True:
        capital = capital * (1 + riskPerc * riskRewardRatio / 100)
    else:
        capital = capital * (1 - riskPerc / 100)
    if capital > maxCapital:
        maxCapital = capital
    dd = 1 - capital / maxCapital
    if dd > maxDrawdown:
        maxDrawdown = dd
    values.append(capital)

print("Trading expectancy: " + str(f'{expectancy:.2f}'))
print("Maximum drawdown: " + str(f'{maxDrawdown * 100:.2f}') + "%")
plt.plot(values, color="blue", lw=1)
plt.show()