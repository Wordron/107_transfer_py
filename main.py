from f_separate_str import separate_str
from f_compute_polynomial import compute_poly
import sys

x = 0
result = 1
len_argv = len(sys.argv)

if len_argv == 0:
    exit(84)
while 1:
    for i in range(1, len_argv, 2):
        num_list = separate_str(sys.argv[i], "*")
        den_list = separate_str(sys.argv[i + 1], "*")
        num_list.reverse()
        den_list.reverse()
        num_result = compute_poly(num_list, x)
        den_result = compute_poly(den_list, x)
        if den_result > -0.0001 and den_result < 0.0001:
            exit(84)
        result = result * (num_result / den_result)
    print("{0:.3f} -> {1:.5f}".format(x, result))
    result = 1
    x += 0.001
    if x > 1.001:
        exit(0)
