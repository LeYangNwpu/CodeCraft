scores_set_ori = [1, 0, 2, 9, 3, 8, 4, 7, 5, 6]
scores_set = scores_set_ori.copy()

beauty_max = 0
doc_seq = None

for sel in range(1, len(scores_set)):
    s_all = scores_set[sel]
    sel_left = sel-1
    sel_right = sel+1
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
        doc_seq = num_seq

print('result')
print(beauty_max)
print(doc_seq)






