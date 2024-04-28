import numpy as np
import click

@click.command()
@click.option('-tg', '--target', default = 19, type = int)
@click.option('-tr', '--thres', default = 1, type = int)
def main(target, thres):

    his_arr = []
    while True:
        digi = np.asarray(list(str(target))).astype(int)
        sums = np.nansum(digi ** 2)
        print(target, digi, sums) 
        
        if sums in his_arr:
            return False
        his_arr.append(sums)
        
        if sums == thres: 
            return True
        target = sums

def main_2(target, thres):

    his_arr = []
    while True:
        digi = list(map(int, str(target)))
        sums = sum([i ** 2 for i in digi])
        print(target, digi, sums)

        if sums in his_arr: return False
        his_arr.append(sums)
        
        if sums == thres: return True
        target = sums

if __name__ == "__main__":
    main()
    #main_2(19, 1)
