from f_separate_str import separate_str
from f_compute_polynomial import compute_poly

print("For the input, insert different numbers separated by \'*\'")

x = 0
num_input = input("Enter numerator : ")
den_input = input("Enter denominator : ")
if len(den_input) == 0 or len(num_input) == 0:
    exit(84)
num_list = separate_str(num_input, "*")
den_list = separate_str(den_input, "*")
num_list.reverse()
den_list.reverse()

while 1:
    num_result = compute_poly(num_list, x)
    den_result = compute_poly(den_list, x)
    if den_result > -0.0001 and den_result < 0.0001:
        exit(84)
    result = num_result / den_result
    print("{0:.3f} -> {1:.5f}".format(x, result))
    x += 0.001
    if x > 1.001:
        exit(0)
