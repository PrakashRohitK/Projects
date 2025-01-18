def generate_all_3_random_values(number):
    results = []
    for i in range(number + 1):
        for j in range(number + 1 - i):
            k = number - i - j
            results.append([i, j, k])
    return results
number = int(input("Enter Total Crop Area:"))
combinations = generate_all_3_random_values(number)
#print(combinations)
for i in (combinations):
    print(i)
