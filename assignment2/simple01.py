# Synchronous cooking
# 1 kitchen 1 chefs 1 dish
# Multiprocessing 2 kitkens, 2 cooker, 2 dishes
# running a function in another thread
from time import sleep, ctime,time


# a custom function that blocks for a moment
def cooking(index):
    print(f'{ctime()} kitchen-{index} : Begin cooking...')
    sleep(2)
    print(f'{ctime()} kitchen-{index} : Cooking done!')

if __name__ =="__main__":
    #being of main thread
    print((f'{ctime()} main : Start cooking...'))
    start_time = time()
    #Cooking
    cooking(0)

    duration = time() -start_time
    print(f"{ctime()} main  : Finish Cooking duration in {duration:0.2f} seconds")