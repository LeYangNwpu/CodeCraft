file_accept = './Google_2018_0826_RoundE/A-small-practice.out'
file_current = './Google_2018_0826_RoundE/A-small-attempt0-test.out'

fid_acc = open(file_accept, 'r')
fid_cur = open(file_current, 'r')

while True:
    ans_acc = fid_acc.readline()
    ans_cur = fid_cur.readline()
    print(ans_acc, ans_cur)
    if ans_acc != ans_cur:
        print('inconsistent', ans_acc, ans_cur)
        break
    if not ans_acc and not ans_cur:
        print('consistent result')
        break
