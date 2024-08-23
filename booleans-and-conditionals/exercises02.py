engine_indicator_light = "red blinking"
space_suits_on = True
shuttle_cabin_ready = True
crew_status = space_suits_on and shuttle_cabin_ready
computer_status_code = 200
shuttleSpeed = 15000

# 3) Write conditional expressions to satisfy the following safety rules:
if shuttle_cabin_ready:
   print("Cabin Ready")
else:
   print("Cabin Not Ready")
# a) If crew_status is true, print "Crew Ready" else print "Crew Not Ready".
if crew_status:
   print("Ready for take off")
else:
   print("Not ready for take off")

# b) If computer_status_code is 200, print "Please stand by. Computer is rebooting." Else if computer_status_code is 400, print "Success! Computer online." Else print "ALERT: Computer offline!"
if computer_status_code:
   print("Computer on")
else:
   print("Compuer off")

# c) If shuttle_speed is > 17,500, print "ALERT: Escape velocity reached!" Else if shuttle_speed is < 8000, print "ALERT: Cannot maintain orbit!" Else print "Stable speed".


# 4) PREDICT: Do the code blocks shown in the Section D produce the same result?

# print("Yes" or "No")