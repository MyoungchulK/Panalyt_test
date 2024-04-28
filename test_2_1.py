import numpy as np
import click
import string

@click.command()
@click.option('-tg', '--target', default = 'PANALYT', type = str)
def main(target):

    ## arrays
    al_arr = np.asarray(list(string.ascii_uppercase))
    tg_arr = np.asarray(list(target))
    print(al_arr)
    print(tg_arr)

    ## base 26 to base 10
    digi_arr = len(al_arr) ** (np.arange(len(tg_arr), 0, -1, dtype = int) - 1)
    tg_idx = np.searchsorted(al_arr, tg_arr, side = 'right')
    print(digi_arr)
    print(tg_idx)

    ## results
    results = np.nansum(digi_arr * tg_idx)
    print(f'{target} = {results}')

if __name__ == "__main__":
    main()

