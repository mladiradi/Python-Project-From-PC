
n = int(input())
library = {}

for _ in range(n):
    data = input().split("|")
    car, mileage, fuel = data[0], int(data[1]), int(data[2])
    library[car] = {'mileage': mileage, 'fuel': fuel}

while True:
    data = input()
    if data == "Stop":
        break

    command = data.split(" : ")
    action = command[0]

    if action == "Drive":
        car, distance, fuel = command[1], int(command[2]), int(command[3])
        if library[car]['fuel'] < fuel:
            print("Not enough fuel to make that ride")
        else:
            library[car]['mileage'] += distance
            library[car]['fuel'] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if library[car]['mileage'] > 100000:
                del library[car]
                print(f"Time to sell the {car}!")

    elif action == "Refuel":
        car, fuel = command[1], int(command[2])
        library[car]['fuel'] += fuel
        if library[car]['fuel'] > 75:
            fuel = 75 - (library[car]['fuel'] - fuel)
            library[car]['fuel'] = 75
        print(f"{car} refueled with {fuel} liters")

    elif action == "Revert":
        car, kilometers = command[1], int(command[2])
        library[car]['mileage'] -= kilometers
        if library[car]['mileage'] < 10000:
            library[car]['mileage'] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

for car, info in library.items():
    print(f"{car} -> Mileage: {library[car]['mileage'] } kms, Fuel in the tank: {info['fuel']} lt.")

# # input:
#
# 3
# Audi A6|38000|62
# Mercedes CLS|11000|35
# Volkswagen Passat CC|45678|5
# Drive : Audi A6 : 543 : 47
# Drive : Mercedes CLS : 94 : 11
# Drive : Volkswagen Passat CC : 69 : 8
# Refuel : Audi A6 : 50
# Revert : Mercedes CLS : 500
# Revert : Audi A6 : 30000
# Stop
#
#
# # 2:
#
# 4
# Lamborghini Veneno|11111|74
# Bugatti Veyron|12345|67
# Koenigsegg CCXR|67890|12
# Aston Martin Valkryie|99900|50
# Drive : Koenigsegg CCXR : 382 : 82
# Drive : Aston Martin Valkryie : 99 : 23
# Drive : Aston Martin Valkryie : 2 : 1
# Refuel : Lamborghini Veneno : 40
# Revert : Bugatti Veyron : 2000
# Stop
#
# # output:
#
# Audi A6 driven for 543 kilometers. 47 liters of fuel consumed.
# Mercedes CLS driven for 94 kilometers. 11 liters of fuel consumed.
# Not enough fuel to make that ride
# Audi A6 refueled with 50 liters
# Mercedes CLS mileage decreased by 500 kilometers
# Audi A6 -> Mileage: 10000 kms, Fuel in the tank: 65 lt.
# Mercedes CLS -> Mileage: 10594 kms, Fuel in the tank: 24 lt.
# Volkswagen Passat CC -> Mileage: 45678 kms, Fuel in the tank: 5 lt.
#
#
# # 2:
#
# Not enough fuel to make that ride
# Aston Martin Valkryie driven for 99 kilometers. 23 liters of fuel consumed.
# Aston Martin Valkryie driven for 2 kilometers. 1 liters of fuel consumed.
# Time to sell the Aston Martin Valkryie!
# Lamborghini Veneno refueled with 1 liters
# Bugatti Veyron mileage decreased by 2000 kilometers
# Lamborghini Veneno -> Mileage: 11111 kms, Fuel in the tank: 75 lt.
# Bugatti Veyron -> Mileage: 10345 kms, Fuel in the tank: 67 lt.
# Koenigsegg CCXR -> Mileage: 67890 kms, Fuel in the tank: 12 lt.
