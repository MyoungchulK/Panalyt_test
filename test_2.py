import numpy as np
import click

@click.command()
@click.option('-tg', '--target', default = 19, type = int)
@click.option('-tr', '--thres', default = 1, type = int)
def main(target, thres):

    sums = 0
    his_arr = []
    while sums != 1:
        digi = np.asarray(list(str(target))).astype(int)
        sums = np.nansum(digi ** 2)
        print(target, digi, sums) 
        
        if sums in his_arr:
            return False
        his_arr.append(sums)
        
        if sums == thres: 
            return True
        else:
            target = sums

if __name__ == "__main__":
    main()

