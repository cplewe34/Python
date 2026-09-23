#road trip planner

name = input("What is your name? ")

destination = input("Where are you traveling to? ")

one_way_distance = input("What is the one-way distance of your trip in miles? ")

car_mpg = input("What is the miles per gallon of your car? ")

gas_price = input("What is the price of gas per gallon? ")

number_travelers = input("How many travelers are going on the trip? ")

#calculations for trip

total_distance = int(one_way_distance) * 2

total_gallons = total_distance / int(car_mpg)

total_cost = total_gallons * float(gas_price)

cost_per_person = total_cost / int(number_travelers)

#display of trip Summary

print(f"\nTrip Summary for {name}")

print(f"\nDestination: {destination}")

print(f"\nTotal Distance: {total_distance} miles")

print(f"Total Gallons: {total_gallons:.2f}")

print(f"\nTotal Cost: ${total_cost:.2f}")

print(f"Cost Per Person: ${cost_per_person:.2f}")

