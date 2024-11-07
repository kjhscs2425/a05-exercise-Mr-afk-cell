
"""
`check_fever` should return `True` if the temperature is `100.4` or higher. For
any lower temperature, it should return `False`.
"""
def check_fever(temperature):
  #if temperature is 100.4 or lower should be false, check_fever should remain True
  return True or False

# Get temperature from user and convert to float
temp = int(input('tell me a number'))
if check_fever(temp):
  print("You have a fever.")
else:
  print("You don't ha8ve a fever.")