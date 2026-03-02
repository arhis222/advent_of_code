
###############################################################################
#PART 1
################################################################################
with open("input.txt") as f:
    lines = f.readlines() 

times = list(map(int, lines[0].split()[1:]))
distances = list(map(int, lines[1].split()[1:]))



result = 1

for T, D in zip(times, distances):
    count = 0
    for x in range(T + 1):
        if x * (T - x) > D:
            count += 1
    result *= count

print(result)

###############################################################################
#PART 2
################################################################################
#combine the numbers
time_numbers = map(str, times)
time_string = ''.join(time_numbers)
distance_numbers = map(str, distances)
distance_string = ''.join(distance_numbers)

time = int(time_string)
distance = int(distance_string)

result = 0

for x in range(time + 1):
    if x * (time - x) > distance:
        result += 1

print(result)