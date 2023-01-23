# bounce.py
#
# Exercise 1.5
height = 100
bounce = 1
while bounce < 11:
    print(bounce, round((height * 3 / 5), 4))
    height *= 3 / 5
    bounce += 1
