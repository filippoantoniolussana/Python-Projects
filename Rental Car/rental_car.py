import sys

# Request rental code
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")

# Request rental period according to the rental code
if rentalCode == "B" or rentalCode == "D":
  rentalPeriod = input("Number of Days Rented:\n")
elif rentalCode == "W":
  rentalPeriod = input("Number of Weeks Rented:\n")

budget_charge = 40.00
daily_charge = 60.00
weekly_charge = 190.00

# Calculate base charge according to the rental code
if rentalCode == "B":
  baseCharge = float(rentalPeriod) * budget_charge
elif rentalCode == "D":
  baseCharge = float(rentalPeriod) * daily_charge
elif rentalCode == "W":
  baseCharge = float(rentalPeriod) * weekly_charge

# Request starting and ending odometer reading
odoStart = input("Starting Odometer Reading:\n")
odoEnd = input("Ending Odometer Reading:\n")

totalMiles = int(odoEnd) - int(odoStart)

averageDayMiles = float(totalMiles) / float(rentalPeriod)
averageWeekMiles = float(totalMiles) / float(rentalPeriod)

# Calculate mile charge according to the rental code
if rentalCode == "B":
  mileCharge = totalMiles * 0.25
elif rentalCode == "D":
  if averageDayMiles <= 100:
    extraMiles = 0
  elif averageDayMiles > 100:
    extraMiles = averageDayMiles - 100
    mileCharge = extraMiles * 0.25
elif rentalCode == "W":
  if averageWeekMiles > 900:
    mileCharge = 100.00 * W
  else:
    mileCharge = 0.00
    
# Calculate total amount due
amtDue = baseCharge + mileCharge

# Display client's rental summary
print("Rental Summary")
print("Rental Code: " + rentalCode)
print("Rental Period: " + rentalPeriod)
print("Starting Odometer: " + odoStart)
print("Ending Odometer: " + odoEnd)
print("Miles Driven: " + str(totalMiles))
print("Amount Due: " + "$%.2f" % amtDue)
