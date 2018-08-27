in_data_file = 'A-small-practice.in'
out_data_file = 'A-small-practice.out'

fid_in = open(in_data_file, 'r')
fid_out = open(out_data_file, 'w')


num_all = int(fid_in.readline())
print('total test samples %d' % num_all)

for itest in range(num_all):
    irow = int(fid_in.readline())
    print('sample {} contains {} data'.format(itest, irow))
    fid_out.write('Case #{}: {}\n'.format(itest, irow))
    for iline in range(irow):
        sline = fid_in.readline()
        value6 = [int(s) for s in sline.split(" ")]
        print(value6)

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
# t = int(input())  # read a line with a single integer
# for i in range(1, t + 1):
#     n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
#     print("Case #{}: {} {}".format(i, n + m, n * m))
    # check out .format's specification for more formatting options

