import numpy as np
import copy

def find_max_comp(comp, val):
    place = []
    for i, data in enumerate(comp):
        if data == val:
            place.append(i)
    return place

def find_num_comp(comp, number):
    place = []



def min_complain(pref_mat, forb_sets):
    [N, P] = pref_mat.shape
    num_add = pref_mat.sum(axis=0)
    num_no = N - num_add
    selection = []
    comp = []
    for i in range(P):
        if num_add[i] > num_no[i]:
            selection.append('1')
            comp.append(num_no[i])
        else:
            selection.append('0')
            comp.append(num_add[i])
    selS = ''.join(selection)
    print('selS', selS)
    print('comp', comp)
    comp_np = np.asarray(comp)
    if selS not in forb_sets:
        print('ideal', selS)
        return comp_np.sum()
    else:
        # for irep in range(1, P):
        #     FoundFlag = False
        # we need to adjust the choose
        replace_p = find_max_comp(comp, comp_np.max())
        for ip in replace_p:
            sel_temp = copy.deepcopy(selection)
            if sel_temp[ip] == '0':
                sel_temp[ip] = '1'
            else:
                sel_temp[ip] = '0'
            selS = ''.join(sel_temp)
            # find an option
            if selS not in forb_sets:
                print('ideal', selS)
                comp[ip] = N - comp[ip]
                # FoundFlag = True
                break
        # if FoundFlag:
        #     break
        comp_np = np.asarray(comp)
        return comp_np.sum()

in_data_file = 'B-small-attempt0.in'
out_data_file = 'B-small-practice.out'

fid_in = open(in_data_file, 'r')
fid_out = open(out_data_file, 'w')


num_all = int(fid_in.readline())
print('total test samples %d' % num_all)

for itest in range(num_all):
    N_M_P_line = fid_in.readline()
    N, M, P = [int(s) for s in N_M_P_line.split(" ")]
    pref_mat = np.zeros((N, P))
    for i in range(N):
        sline = fid_in.readline()
        for j, data in enumerate(list(sline[:-1])):
            pref_mat[i,j] = int(data)
    forb_sets = []
    for i in range(M):
        sline = fid_in.readline()
        forb_sets.append(sline[:-1])
    result = min_complain(pref_mat, forb_sets)
    order = itest + 1
    fid_out.write('Case #{}: {}\n'.format(order, int(result)))
    print(result)


