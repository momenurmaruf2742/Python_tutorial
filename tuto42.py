# time module

import time
#
# initial1 = time.time()
# k = 0
# while (k<45):
#     print('this is maruf')
#     k+=1
# print('while loop run in',time.time()-initial1)
#
# initial2 = time.time()
# for i in range(45):
#     print('this is maruf')
# print("for loop run in",time.time()-initial2)


localTime = time.asctime(time.localtime(time.time()))
print(localTime)