in_data_file = 'B-small-practice.in'
out_data_file = 'B-small-practice.out'

fid_in = open(in_data_file, 'r')
fid_out = open(out_data_file, 'w')


def cal_max_scores(scores_set):
    beauty_max = 0

    for sel in range(len(scores_set)):
        s_all = scores_set[sel]
        sel_left = sel - 1
        sel_right = sel + 1
        des_left = -1
        des_right = len(scores_set)
        selected = [0] * len(scores_set)
        selected[sel] = 1

        num_seq = [scores_set[sel]]

        while True:
            # destory
            if selected[des_left + 1] == 0 and selected[des_right - 1] == 0:
                if scores_set[des_left + 1] >= scores_set[des_right - 1]:
                    des_ind = des_left + 1
                    des_left += 1
                else:
                    des_ind = des_right - 1
                    des_right -= 1
            elif selected[des_right - 1] == 0:
                des_ind = des_right - 1
                des_right -= 1
            elif selected[des_left + 1] == 0:
                des_ind = des_left + 1
                des_left += 1
            else:
                des_ind = None

            if des_ind is not None:
                print('des index', des_ind)
            else:
                break

            # select max next data
            # we can expand two directions
            if sel_left > des_left and (sel_right < des_right):
                if scores_set[sel_left] >= scores_set[sel_right]:
                    sel_ind = sel_left
                    sel_left -= 1
                else:
                    sel_ind = sel_right
                    sel_right += 1
            # only expand right
            elif sel_right < des_right:
                sel_ind = sel_right
                sel_right += 1
            # only expand left
            elif sel_left > des_left:
                sel_ind = sel_left
                sel_left -= 1
            # stop
            else:
                sel_ind = None

            if sel_ind is not None:
                print('select index', sel_ind)
                sel_data = scores_set[sel_ind]
                num_seq.append(sel_data)
                selected[sel_ind] = 1
                s_all += sel_data
            else:
                break

            print('des_left, des_right: ', des_left, des_right)

        if s_all > beauty_max:
            beauty_max = s_all
    return beauty_max


num_all = int(fid_in.readline())
print('total test samples %d' % num_all)

for itest in range(num_all):
    num_brick = int(fid_in.readline())
    scores_str = fid_in.readline()
    scores = []
    for s in scores_str[:-1]:
        scores.append(int(s))

    max_score = cal_max_scores(scores)

    order = itest + 1
    fid_out.write('Case #{}: {}\n'.format(order, max_score))


