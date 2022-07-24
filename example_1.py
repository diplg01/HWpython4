# Задание 1

# Вычислить число c заданной точностью d
# Пример:  - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

def Pi(x):
    mod = 1
    result = 3
    n = 2
    while True:
        temp = round(result, x)
        result += mod * 4/(n*(n+1)*(n+2))
        if round(result, x) == temp:
            print(f'Число пи с точностью до { x} знака равно {round(result, x)}')
            break
        else:
            mod *= -1
            n += 2

d = int(input('Введите нужную точность: '))
Pi(d)