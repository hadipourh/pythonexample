def num_of_distinct_prime_divisors(n):
    d = 2
    distinct_divisors = []
    while (n != 1):
        if (n % d == 0):
            n //= d
            if d not in distinct_divisors:
                distinct_divisors.append(d)
        else:
            d += 1
    return len(distinct_divisors)

input_data = int(input())
output, output_ndivs = input_data, num_of_distinct_prime_divisors(input_data)
for i in range(9):
    input_data = int(input())
    temp = num_of_distinct_prime_divisors(input_data)
    if (temp > output_ndivs):
        output, output_ndivs = input_data, temp
    elif (temp == output_ndivs):
        if (input_data > output):
            output = input_data
print(output, output_ndivs)
