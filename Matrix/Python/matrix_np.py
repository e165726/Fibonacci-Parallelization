import time
import sys
import numpy as np

def func(n):
    a = np.full((n, n), 50)
    b = np.full((n, n), 50)
    return np.dot(a,b)

stratTime = time.time()
argv = int(sys.argv[1])
print(func(argv))
endTime = time.time() #プログラムの終了時刻
runTime = endTime - stratTime #処理時間
print('time = {0}sec'.format(runTime)) #処理時間を表示