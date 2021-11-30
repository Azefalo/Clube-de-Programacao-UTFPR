# https://www.beecrowd.com.br/judge/en/problems/view/1017
car_efficiency = 12 # Km/L
time = int(input())
average_speed = int(input())

liters = (time * average_speed) / car_efficiency

print(f"{liters:.3f}")