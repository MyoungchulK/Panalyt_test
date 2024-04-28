import numpy as np
import click

@click.command()
@click.option('-tg', '--target', default = '1,51')
@click.option('-t1', '--thres1', default = 3, type = int)
@click.option('-r1', '--replace1', default = 'Pana', type = str)
@click.option('-t2', '--thres2', default = 5, type = int)
@click.option('-r2', '--replace2', default = 'Lyt', type = str)
def main(target, thres1, replace1, thres2, replace2):

    ## array creation
    tg_param = np.asarray(target.split(',')).astype(int)
    tg_arr = np.arange(tg_param[0], tg_param[1], dtype = int)
    tg_obj = tg_arr.astype(object)

    ## replace
    t1_bool = tg_arr % thres1 == 0
    t2_bool = tg_arr % thres2 == 0
    tg_obj[t2_bool] = replace2
    tg_obj[t1_bool] = replace1
    tg_obj[np.logical_and(t1_bool, t2_bool)] += replace2
    
    print(tg_obj.tolist())

def main_2(target, thres1, replace1, thres2, replace2):

    tg_param = list(map(int, target.split(',')))
    tg_obj = []
    thres3 = thres1 * thres2
    for tg in range(tg_param[0], tg_param[1] + 1):
        if tg % thres3 == 0: ele = replace1 + replace2
        elif tg % thres1 == 0: ele = replace1
        elif tg % thres2 == 0: ele = replace2  
        else: ele = tg
        #if tg % (thres1 * thres2) == 0: ele += replace2 # could use this
        tg_obj.append(ele)

    print(tg_obj)

if __name__ == "__main__":
    main()
    #main_2('1,50', 3, 'Pana', 5, 'Lyt')
