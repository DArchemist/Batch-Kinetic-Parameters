from scipy.optimize import fsolve


def equations1(vars):
    x, y = vars
    eq1 = x * 9.2709 / (y + 9.2709) - 0.7787
    eq2 = x * 9.1526 / (y + 9.1526) - 1.3475
    eq3 = x * 9.042 / (y + 9.042) - 1.6538
    eq4 = x * 8.9142 / (y + 8.9142) - 0.879
    eq5 = x * 8.7098 / (y + 8.7098) - 1.0081
    eq6 = x * 8.3247 / (y + 8.3247) - 1.112
    eq7 = x * 7.6 / (y + 7.6) - 1.1967
    eq8 = x * 6.3108 / (y + 6.3108) - 1.2669
    eq9 = x * 4.1566 / (y + 4.1566) - 0.6597
    #return [eq1, eq2, eq3, eq4, eq5, eq6, eq7]
    return [eq1, eq9]


def equations2(vars):
    x, y = vars
    eq1 = 1 / x + y / (x * 9.2709) - 1 / 0.7787
    eq2 = 1 / x + y / (x * 9.1526) - 1 / 1.3475
    eq3 = 1 / x + y / (x * 9.042) - 1 / 1.6538
    eq4 = 1 / x + y / (x * 8.9142) - 1 / 0.879
    eq5 = 1 / x + y / (x * 8.7098) - 1 / 1.0081
    eq6 = 1 / x + y / (x * 8.3247) - 1 / 1.112
    eq7 = 1 / x + y / (x * 7.6) - 1 / 1.1967
    eq8 = 1 / x + y / (x * 6.3108) - 1 / 1.2669
    eq9 = 1 / x + y / (x * 4.1566) - 1 / 0.6597
    return [eq2, eq8]


x, y = fsolve(equations1, (1, 0))
print(f'mu_max = {x} \nK_s = {y}')
