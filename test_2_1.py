import numpy as np
import click
import string

@click.command()
@click.option('-tg', '--target', default = 'PANALYT')
def main(target):

    ## arrays
    al_arr = np.asarray(list(string.ascii_uppercase))
    al_len = len(al_arr)
    print(al_arr)

    ## target
    tg_arr = np.asarray(list(target))
    print(tg_arr)

    ## decimals and corresponding numbers
    digi_arr = (np.arange(len(tg_arr), 0, -1, dtype = int) -1) * al_len
    tg_idx = np.searchsorted(al_arr, tg_arr, side = 'right')
    print(digi_arr)
    print(tg_idx)

    ## results
    results = np.nansum(digi_arr + tg_idx)
    print(f'{target} = {results}')

if __name__ == "__main__":
    main()
