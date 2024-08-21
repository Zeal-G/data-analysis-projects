# 1. Declare and assign the variables here:
shuttle_name = "Determination"
print(shuttle_name)
shuttle_speed_mph = 17,500
print(shuttle_speed_mph)
distance_to_mars_km = 225,000,000
print(distance_to_mars_km)
distance_to_moon_km = 384,400
print(distance_to_moon_km)
miles_per_kilo = 0.621
print(miles_per_kilo)
# 2. Use print() to print the 'type' each variable. Print one item per line.
print(type(shuttle_name))
print(type(shuttle_speed_mph))
print(type(distance_to_mars_km))
print(type(distance_to_moon_km))
print(type(miles_per_kilo))
# Code your solution to exercises 3 and 4 here:
miles_to_mars = 225000000 * 0.621
print(miles_to_mars)

hours_to_mars = 139725000.0 * 17500
print(hours_to_mars)

days_to_mars = hours_to_mars * 25
print(days_to_mars)

miles_to_moon = 384400 * 0.621
print(miles_to_moon)

hours_to_moon = 238712.4 / 17500
print(hours_to_moon)

days_to_moon = 13.64070857142857 / 24
print(days_to_moon)

print(str(shuttle_name) + " will take " + str(days_to_moon) + " days to reach the Moon.")
# Code your solution to exercise 5 here
