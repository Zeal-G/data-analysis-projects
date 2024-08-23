# Assign the variables for exercise 1 here:
engine_indicator_light = "red blinking"
print(engine_indicator_light);
space_suits_on = True
print(space_suits_on);
shuttle_cabin_ready = True
print(space_suits_on);
crew_status = space_suits_on and shuttle_cabin_ready
print(crew_status);
computer_status_code = 200
print(computer_status_code);
shuttle_speed = 15000
print(shuttle_speed)
# BEFORE running the code, predict what will be printed to the console by the following statements:
# I predict the outcome will give us "engines are off"
if engine_indicator_light == "green": 
  print("engines have started")
elif engine_indicator_light == "green blinking": 
  print("engines are preparing to start")
else:
  print("engines are off")