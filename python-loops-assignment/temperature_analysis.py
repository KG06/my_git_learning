# Name: Kumaravel Govindaraj
# Roll Number: iitp_aimltn_2602783 
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

high = low = 0

for index, temperature in enumerate(temperatures):
        if index == 0: 
            high = low = temperature
        if(high < temperature):
            high = temperature
        elif low > temperature:
            low = temperature

print(f"Highest Temperature: {high}°C")
print(f"Lowest Temperature: {low}°C")


print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

hot_days = 0

for temperature in temperatures:
    if(temperature <= 30):
         continue
    hot_days += 1

print(f"Hot Days (>30°C): {hot_days}")


print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]

hot_days = 0
day_counter = 0
alter_day = 0

for temperature in temperatures:
    day_counter += 1
    if(temperature >= 40): 
        alter_day = day_counter
        break
    elif(temperature >= 30):
        hot_days += 1
         
print(f"Hot Days before alert: {hot_days}")
print(f"Alert! Extreme temperature 40°C detected on Day {alter_day}")