import numpy as np
import matplotlib.pyplot as plt

# [torrentSize (MiB), torrentAge, selfUploaded]
torrent_list_casual = np.array([[829.89, 0, False], [34.74, 0, False], [91.84, 0, False], [640.22, 0, True], [167.19, 0, True], [102.68, 1, False],
                                [156.44,1,False], [115.4,1,False], [4.93,1,False], [114.25,2,False], [32.24,3,False], [1190.0,3,False],
                                [157.47,4,True], [396.01,4,False], [219.14,5,False], [935.43,5,False], [457.48,5,False], [4160.0,5,True],
                                [190.97,7,True], [849.38,8,True], [462.99,8,False], [98.12,9,False], [1340.0,10,True], [874.71,10,True],
                                [1203.0,12,False], [774.09,15,False], [81.99,16,False], [106.67,18,False], [109.46,18,False],
                                [606.58,19,False], [249.33,20,False], [484.07,20,False], [845.49,20,False], [1270.0,21,True],
                                [7900.0,22,False], [354.15,23,False], [50.96,24,False], [373.25,24,False], [152.07,26,False],
                                [330.71,27,True], [208.5,27,False], [37.46,31,False], [52.77,34,False], [3110.0,41,False]])
torrent_list_poweruser = np.array([[829.89, 0, False], [34.74, 0, False], [91.84, 0, False], [640.22, 0, True], [167.19, 0, True], [102.68, 1, False],
                                [156.44,1,False], [115.4,1,False], [4.93,1,False], [114.25,2,False], [32.24,3,False], [1190.0,3,False],
                                [157.47,4,True], [396.01,4,False], [219.14,5,False], [935.43,5,False], [457.48,5,False], [4160.0,5,True],
                                [190.97,7,True], [849.38,8,True], [462.99,8,False], [98.12,9,False], [1340.0,10,True], [874.71,10,True],
                                [1203.0,12,False], [774.09,15,False], [81.99,16,False], [106.67,18,False], [109.46,18,False],
                                [606.58,19,False], [249.33,20,False], [484.07,20,False], [845.49,20,False], [1270.0,21,True],
                                [7900.0,22,False], [354.15,23,False], [50.96,24,False], [373.25,24,False], [152.07,26,False],
                                [330.71,27,True], [208.5,27,False], [37.46,31,False], [52.77,34,False], [3110.0,41,False], [829.89, 0, False], [34.74, 0, False], [91.84, 0, False], [640.22, 0, True], [167.19, 0, True], [102.68, 1, False],
                                [156.44,1,False], [115.4,1,False], [4.93,1,False], [114.25,2,False], [32.24,3,False], [1190.0,3,False],
                                [157.47,4,True], [396.01,4,False], [219.14,5,False], [935.43,5,False], [457.48,5,False], [4160.0,5,True],
                                [190.97,7,True], [849.38,8,True], [462.99,8,False], [98.12,9,False], [1340.0,10,True], [874.71,10,True],
                                [1203.0,12,False], [774.09,15,False], [81.99,16,False], [106.67,18,False], [109.46,18,False],
                                [606.58,19,False], [249.33,20,False], [484.07,20,False], [845.49,20,False], [1270.0,21,True],
                                [7900.0,22,False], [354.15,23,False], [50.96,24,False], [373.25,24,False], [152.07,26,False],
                                [330.71,27,True], [208.5,27,False], [37.46,31,False], [52.77,34,False], [3110.0,41,False], [829.89, 0, False], [34.74, 0, False], [91.84, 0, False], [640.22, 0, True], [167.19, 0, True], [102.68, 1, False],
                                [156.44,1,False], [115.4,1,False], [4.93,1,False], [114.25,2,False], [32.24,3,False], [1190.0,3,False],
                                [157.47,4,True], [396.01,4,False], [219.14,5,False], [935.43,5,False], [457.48,5,False], [4160.0,5,True],
                                [190.97,7,True], [849.38,8,True], [462.99,8,False], [98.12,9,False], [1340.0,10,True], [874.71,10,True],
                                [1203.0,12,False], [774.09,15,False], [81.99,16,False], [106.67,18,False], [109.46,18,False],
                                [606.58,19,False], [249.33,20,False], [484.07,20,False], [845.49,20,False], [1270.0,21,True],
                                [7900.0,22,False], [354.15,23,False], [50.96,24,False], [373.25,24,False], [152.07,26,False],
                                [330.71,27,True], [208.5,27,False], [37.46,31,False], [52.77,34,False], [3110.0,41,False], [829.89, 0, False], [34.74, 0, False], [91.84, 0, False], [640.22, 0, True], [167.19, 0, True], [102.68, 1, False],
                                [156.44,1,False], [115.4,1,False], [4.93,1,False], [114.25,2,False], [32.24,3,False], [1190.0,3,False],
                                [157.47,4,True], [396.01,4,False], [219.14,5,False], [935.43,5,False], [457.48,5,False], [4160.0,5,True],
                                [190.97,7,True], [849.38,8,True], [462.99,8,False], [98.12,9,False], [1340.0,10,True], [874.71,10,True],
                                [1203.0,12,False], [774.09,15,False], [81.99,16,False], [106.67,18,False], [109.46,18,False],
                                [606.58,19,False], [249.33,20,False], [484.07,20,False], [845.49,20,False], [1270.0,21,True],
                                [7900.0,22,False], [354.15,23,False], [50.96,24,False], [373.25,24,False], [152.07,26,False],
                                [330.71,27,True], [208.5,27,False], [37.46,31,False], [52.77,34,False], [3110.0,41,False], [829.89, 0, False], [34.74, 0, False], [91.84, 0, False], [640.22, 0, True], [167.19, 0, True], [102.68, 1, False],
                                [156.44,1,False], [115.4,1,False], [4.93,1,False], [114.25,2,False], [32.24,3,False], [1190.0,3,False],
                                [157.47,4,True], [396.01,4,False], [219.14,5,False], [935.43,5,False], [457.48,5,False], [4160.0,5,True],
                                [190.97,7,True], [849.38,8,True], [462.99,8,False], [98.12,9,False], [1340.0,10,True], [874.71,10,True],
                                [1203.0,12,False], [774.09,15,False], [81.99,16,False], [106.67,18,False], [109.46,18,False],
                                [606.58,19,False], [249.33,20,False], [484.07,20,False], [845.49,20,False], [1270.0,21,True],
                                [7900.0,22,False], [354.15,23,False], [50.96,24,False], [373.25,24,False], [152.07,26,False],
                                [330.71,27,True], [208.5,27,False], [37.46,31,False], [52.77,34,False], [3110.0,41,False], [829.89, 0, False], [34.74, 0, False], [91.84, 0, False], [640.22, 0, True], [167.19, 0, True], [102.68, 1, False],
                                [156.44,1,False], [115.4,1,False], [4.93,1,False], [114.25,2,False], [32.24,3,False], [1190.0,3,False],
                                [157.47,4,True], [396.01,4,False], [219.14,5,False], [935.43,5,False], [457.48,5,False], [4160.0,5,True],
                                [190.97,7,True], [849.38,8,True], [462.99,8,False], [98.12,9,False], [1340.0,10,True], [874.71,10,True],
                                [1203.0,12,False], [774.09,15,False], [81.99,16,False], [106.67,18,False], [109.46,18,False],
                                [606.58,19,False], [249.33,20,False], [484.07,20,False], [845.49,20,False], [1270.0,21,True],
                                [7900.0,22,False], [354.15,23,False], [50.96,24,False], [373.25,24,False], [152.07,26,False],
                                [330.71,27,True], [208.5,27,False], [37.46,31,False], [52.77,34,False], [3110.0,41,False], [829.89, 0, False], [34.74, 0, False], [91.84, 0, False], [640.22, 0, True], [167.19, 0, True], [102.68, 1, False],
                                [156.44,1,False], [115.4,1,False], [4.93,1,False], [114.25,2,False], [32.24,3,False], [1190.0,3,False],
                                [157.47,4,True], [396.01,4,False], [219.14,5,False], [935.43,5,False], [457.48,5,False], [4160.0,5,True],
                                [190.97,7,True], [849.38,8,True], [462.99,8,False], [98.12,9,False], [1340.0,10,True], [874.71,10,True],
                                [1203.0,12,False], [774.09,15,False], [81.99,16,False], [106.67,18,False], [109.46,18,False],
                                [606.58,19,False], [249.33,20,False], [484.07,20,False], [845.49,20,False], [1270.0,21,True],
                                [7900.0,22,False], [354.15,23,False], [50.96,24,False], [373.25,24,False], [152.07,26,False],
                                [330.71,27,True], [208.5,27,False], [37.46,31,False], [52.77,34,False], [3110.0,41,False], [829.89, 0, False], [34.74, 0, False], [91.84, 0, False], [640.22, 0, True], [167.19, 0, True], [102.68, 1, False],
                                [156.44,1,False], [115.4,1,False], [4.93,1,False], [114.25,2,False], [32.24,3,False], [1190.0,3,False],
                                [157.47,4,True], [396.01,4,False], [219.14,5,False], [935.43,5,False], [457.48,5,False], [4160.0,5,True],
                                [190.97,7,True], [849.38,8,True], [462.99,8,False], [98.12,9,False], [1340.0,10,True], [874.71,10,True],
                                [1203.0,12,False], [774.09,15,False], [81.99,16,False], [106.67,18,False], [109.46,18,False],
                                [606.58,19,False], [249.33,20,False], [484.07,20,False], [845.49,20,False], [1270.0,21,True],
                                [7900.0,22,False], [354.15,23,False], [50.96,24,False], [373.25,24,False], [152.07,26,False],
                                [330.71,27,True], [208.5,27,False], [37.46,31,False], [52.77,34,False], [3110.0,41,False], [829.89, 0, False], [34.74, 0, False], [91.84, 0, False], [640.22, 0, True], [167.19, 0, True], [102.68, 1, False],
                                [156.44,1,False], [115.4,1,False], [4.93,1,False], [114.25,2,False], [32.24,3,False], [1190.0,3,False],
                                [157.47,4,True], [396.01,4,False], [219.14,5,False], [935.43,5,False], [457.48,5,False], [4160.0,5,True],
                                [190.97,7,True], [849.38,8,True], [462.99,8,False], [98.12,9,False], [1340.0,10,True], [874.71,10,True],
                                [1203.0,12,False], [774.09,15,False], [81.99,16,False], [106.67,18,False], [109.46,18,False],
                                [606.58,19,False], [249.33,20,False], [484.07,20,False], [845.49,20,False], [1270.0,21,True],
                                [7900.0,22,False], [354.15,23,False], [50.96,24,False], [373.25,24,False], [152.07,26,False],
                                [330.71,27,True], [208.5,27,False], [37.46,31,False], [52.77,34,False], [3110.0,41,False], [829.89, 0, False], [34.74, 0, False], [91.84, 0, False], [640.22, 0, True], [167.19, 0, True], [102.68, 1, False],
                                [156.44,1,False], [115.4,1,False], [4.93,1,False], [114.25,2,False], [32.24,3,False], [1190.0,3,False],
                                [157.47,4,True], [396.01,4,False], [219.14,5,False], [935.43,5,False], [457.48,5,False], [4160.0,5,True],
                                [190.97,7,True], [849.38,8,True], [462.99,8,False], [98.12,9,False], [1340.0,10,True], [874.71,10,True],
                                [1203.0,12,False], [774.09,15,False], [81.99,16,False], [106.67,18,False], [109.46,18,False],
                                [606.58,19,False], [249.33,20,False], [484.07,20,False], [845.49,20,False], [1270.0,21,True],
                                [7900.0,22,False], [354.15,23,False], [50.96,24,False], [373.25,24,False], [152.07,26,False],
                                [330.71,27,True], [208.5,27,False], [37.46,31,False], [52.77,34,False], [3110.0,41,False], [829.89, 0, False], [34.74, 0, False], [91.84, 0, False], [640.22, 0, True], [167.19, 0, True], [102.68, 1, False],
                                [156.44,1,False], [115.4,1,False], [4.93,1,False], [114.25,2,False], [32.24,3,False], [1190.0,3,False],
                                [157.47,4,True], [396.01,4,False], [219.14,5,False], [935.43,5,False], [457.48,5,False], [4160.0,5,True],
                                [190.97,7,True], [849.38,8,True], [462.99,8,False], [98.12,9,False], [1340.0,10,True], [874.71,10,True],
                                [1203.0,12,False], [774.09,15,False], [81.99,16,False], [106.67,18,False], [109.46,18,False],
                                [606.58,19,False], [249.33,20,False], [484.07,20,False], [845.49,20,False], [1270.0,21,True],
                                [7900.0,22,False], [354.15,23,False], [50.96,24,False], [373.25,24,False], [152.07,26,False],
                                [330.71,27,True], [208.5,27,False], [37.46,31,False], [52.77,34,False], [3110.0,41,False], [829.89, 0, False], [34.74, 0, False], [91.84, 0, False], [640.22, 0, True], [167.19, 0, True], [102.68, 1, False],
                                [156.44,1,False], [115.4,1,False], [4.93,1,False], [114.25,2,False], [32.24,3,False], [1190.0,3,False],
                                [157.47,4,True], [396.01,4,False], [219.14,5,False], [935.43,5,False], [457.48,5,False], [4160.0,5,True],
                                [190.97,7,True], [849.38,8,True], [462.99,8,False], [98.12,9,False], [1340.0,10,True], [874.71,10,True],
                                [1203.0,12,False], [774.09,15,False], [81.99,16,False], [106.67,18,False], [109.46,18,False],
                                [606.58,19,False], [249.33,20,False], [484.07,20,False], [845.49,20,False], [1270.0,21,True],
                                [7900.0,22,False], [354.15,23,False], [50.96,24,False], [373.25,24,False], [152.07,26,False],
                                [330.71,27,True], [208.5,27,False], [37.46,31,False], [52.77,34,False], [3110.0,41,False], [829.89, 0, False], [34.74, 0, False], [91.84, 0, False], [640.22, 0, True], [167.19, 0, True], [102.68, 1, False],
                                [156.44,1,False], [115.4,1,False], [4.93,1,False], [114.25,2,False], [32.24,3,False], [1190.0,3,False],
                                [157.47,4,True], [396.01,4,False], [219.14,5,False], [935.43,5,False], [457.48,5,False], [4160.0,5,True],
                                [190.97,7,True], [849.38,8,True], [462.99,8,False], [98.12,9,False], [1340.0,10,True], [874.71,10,True],
                                [1203.0,12,False], [774.09,15,False], [81.99,16,False], [106.67,18,False], [109.46,18,False],
                                [606.58,19,False], [249.33,20,False], [484.07,20,False], [845.49,20,False], [1270.0,21,True],
                                [7900.0,22,False], [354.15,23,False], [50.96,24,False], [373.25,24,False], [152.07,26,False],
                                [330.71,27,True], [208.5,27,False], [37.46,31,False], [52.77,34,False], [3110.0,41,False], [829.89, 0, False], [34.74, 0, False], [91.84, 0, False], [640.22, 0, True], [167.19, 0, True], [102.68, 1, False],
                                [156.44,1,False], [115.4,1,False], [4.93,1,False], [114.25,2,False], [32.24,3,False], [1190.0,3,False],
                                [157.47,4,True], [396.01,4,False], [219.14,5,False], [935.43,5,False], [457.48,5,False], [4160.0,5,True],
                                [190.97,7,True], [849.38,8,True], [462.99,8,False], [98.12,9,False], [1340.0,10,True], [874.71,10,True],
                                [1203.0,12,False], [774.09,15,False], [81.99,16,False], [106.67,18,False], [109.46,18,False],
                                [606.58,19,False], [249.33,20,False], [484.07,20,False], [845.49,20,False], [1270.0,21,True],
                                [7900.0,22,False], [354.15,23,False], [50.96,24,False], [373.25,24,False], [152.07,26,False],
                                [330.71,27,True], [208.5,27,False], [37.46,31,False], [52.77,34,False], [3110.0,41,False], [829.89, 0, False], [34.74, 0, False], [91.84, 0, False], [640.22, 0, True], [167.19, 0, True], [102.68, 1, False],
                                [156.44,1,False], [115.4,1,False], [4.93,1,False], [114.25,2,False], [32.24,3,False], [1190.0,3,False],
                                [157.47,4,True], [396.01,4,False], [219.14,5,False], [935.43,5,False], [457.48,5,False], [4160.0,5,True],
                                [190.97,7,True], [849.38,8,True], [462.99,8,False], [98.12,9,False], [1340.0,10,True], [874.71,10,True],
                                [1203.0,12,False], [774.09,15,False], [81.99,16,False], [106.67,18,False], [109.46,18,False],
                                [606.58,19,False], [249.33,20,False], [484.07,20,False], [845.49,20,False], [1270.0,21,True],
                                [7900.0,22,False], [354.15,23,False], [50.96,24,False], [373.25,24,False], [152.07,26,False],
                                [330.71,27,True], [208.5,27,False], [37.46,31,False], [52.77,34,False], [3110.0,41,False], [829.89, 0, False], [34.74, 0, False], [91.84, 0, False], [640.22, 0, True], [167.19, 0, True], [102.68, 1, False],
                                [156.44,1,False], [115.4,1,False], [4.93,1,False], [114.25,2,False], [32.24,3,False], [1190.0,3,False],
                                [157.47,4,True], [396.01,4,False], [219.14,5,False], [935.43,5,False], [457.48,5,False], [4160.0,5,True],
                                [190.97,7,True], [849.38,8,True], [462.99,8,False], [98.12,9,False], [1340.0,10,True], [874.71,10,True],
                                [1203.0,12,False], [774.09,15,False], [81.99,16,False], [106.67,18,False], [109.46,18,False],
                                [606.58,19,False], [249.33,20,False], [484.07,20,False], [845.49,20,False], [1270.0,21,True],
                                [7900.0,22,False], [354.15,23,False], [50.96,24,False], [373.25,24,False], [152.07,26,False],
                                [330.71,27,True], [208.5,27,False], [37.46,31,False], [52.77,34,False], [3110.0,41,False], [829.89, 0, False], [34.74, 0, False], [91.84, 0, False], [640.22, 0, True], [167.19, 0, True], [102.68, 1, False],
                                [156.44,1,False], [115.4,1,False], [4.93,1,False], [114.25,2,False], [32.24,3,False], [1190.0,3,False],
                                [157.47,4,True], [396.01,4,False], [219.14,5,False], [935.43,5,False], [457.48,5,False], [4160.0,5,True],
                                [190.97,7,True], [849.38,8,True], [462.99,8,False], [98.12,9,False], [1340.0,10,True], [874.71,10,True],
                                [1203.0,12,False], [774.09,15,False], [81.99,16,False], [106.67,18,False], [109.46,18,False],
                                [606.58,19,False], [249.33,20,False], [484.07,20,False], [845.49,20,False], [1270.0,21,True],
                                [7900.0,22,False], [354.15,23,False], [50.96,24,False], [373.25,24,False], [152.07,26,False],
                                [330.71,27,True], [208.5,27,False], [37.46,31,False], [52.77,34,False], [3110.0,41,False], [829.89, 0, False], [34.74, 0, False], [91.84, 0, False], [640.22, 0, True], [167.19, 0, True], [102.68, 1, False],
                                [156.44,1,False], [115.4,1,False], [4.93,1,False], [114.25,2,False], [32.24,3,False], [1190.0,3,False],
                                [157.47,4,True], [396.01,4,False], [219.14,5,False], [935.43,5,False], [457.48,5,False], [4160.0,5,True],
                                [190.97,7,True], [849.38,8,True], [462.99,8,False], [98.12,9,False], [1340.0,10,True], [874.71,10,True],
                                [1203.0,12,False], [774.09,15,False], [81.99,16,False], [106.67,18,False], [109.46,18,False],
                                [606.58,19,False], [249.33,20,False], [484.07,20,False], [845.49,20,False], [1270.0,21,True],
                                [7900.0,22,False], [354.15,23,False], [50.96,24,False], [373.25,24,False], [152.07,26,False],
                                [330.71,27,True], [208.5,27,False], [37.46,31,False], [52.77,34,False], [3110.0,41,False], [829.89, 0, False], [34.74, 0, False], [91.84, 0, False], [640.22, 0, True], [167.19, 0, True], [102.68, 1, False],
                                [156.44,1,False], [115.4,1,False], [4.93,1,False], [114.25,2,False], [32.24,3,False], [1190.0,3,False],
                                [157.47,4,True], [396.01,4,False], [219.14,5,False], [935.43,5,False], [457.48,5,False], [4160.0,5,True],
                                [190.97,7,True], [849.38,8,True], [462.99,8,False], [98.12,9,False], [1340.0,10,True], [874.71,10,True],
                                [1203.0,12,False], [774.09,15,False], [81.99,16,False], [106.67,18,False], [109.46,18,False],
                                [606.58,19,False], [249.33,20,False], [484.07,20,False], [845.49,20,False], [1270.0,21,True],
                                [7900.0,22,False], [354.15,23,False], [50.96,24,False], [373.25,24,False], [152.07,26,False],
                                [330.71,27,True], [208.5,27,False], [37.46,31,False], [52.77,34,False], [3110.0,41,False], [829.89, 0, False], [34.74, 0, False], [91.84, 0, False], [640.22, 0, True], [167.19, 0, True], [102.68, 1, False],
                                [156.44,1,False], [115.4,1,False], [4.93,1,False], [114.25,2,False], [32.24,3,False], [1190.0,3,False],
                                [157.47,4,True], [396.01,4,False], [219.14,5,False], [935.43,5,False], [457.48,5,False], [4160.0,5,True],
                                [190.97,7,True], [849.38,8,True], [462.99,8,False], [98.12,9,False], [1340.0,10,True], [874.71,10,True],
                                [1203.0,12,False], [774.09,15,False], [81.99,16,False], [106.67,18,False], [109.46,18,False],
                                [606.58,19,False], [249.33,20,False], [484.07,20,False], [845.49,20,False], [1270.0,21,True],
                                [7900.0,22,False], [354.15,23,False], [50.96,24,False], [373.25,24,False], [152.07,26,False],
                                [330.71,27,True], [208.5,27,False], [37.46,31,False], [52.77,34,False], [3110.0,41,False]])

# constants for the sake of readibility etc.
months = 30  # days
day = 24  # hours

def prop_model(seedtime,torrents):
    totalBon = 0
    for torrent in torrents:
        ageBon = 0
        seedBon = 0
        uploadBon = 0
        size = torrent[0]
        age = torrent[1]
        uploaded = torrent[2]
        if size < 20000:
            sizeBon = (size * 0.001) * day
        else:
            sizeBon = 20 * day
        if uploaded:
            uploadBon = 1 * day  # base bonus
        ageBon = np.minimum((0.2 * (age+seedtime//months) * day), 2.4 * day)  # Age Bonus
        seedBon = np.minimum((0.2 * (seedtime//months) * day), 0.6 * day)  # Seed Time Bonus
        torrentBon = sizeBon + ageBon + uploadBon + seedBon
        totalBon += torrentBon
    return totalBon

def curr_model(seedtime,torrents):
    totalBon = 0

    for torrent in torrents:
        ageBon = 0
        seedBon = 0
        uploadBon = 0
        size = torrent[0]
        age = torrent[1]
        uploaded = torrent[2]

        if size >= 1 and size < 50: #
            sizeBon = 0.05 * day
        elif size >= 50 and size < 1000:
            sizeBon = 0.25 * day
        elif size >= 1000 and size < 50000:
            sizeBon = 0.50 * day
        elif size >= 50000:
            sizeBon = 0.75 * day
        else: # <1MiB
            sizeBon = 0 * day

        if age+seedtime >= 6*months: # torrent age
            if age+seedtime >= 12*months:
                ageBon = 1.5 * day
            else:
                ageBon = 1 * day

        if seedtime >= 1 * months and seedtime < 2 * months: #seedtime
            seedBon = 0.25 * day
        elif seedtime >= 2 * months and seedtime < 3 * months:
            seedBon = 0.50 * day
        elif seedtime >= 3 * months and seedtime < 6 * months:
            seedBon = 0.75 * day
        elif seedtime >= 6 * months and seedtime < 12 * months:
            seedBon = 1 * day
        elif seedtime >= 12 * months:
            seedBon = 2 * day

        torrentBon = sizeBon + ageBon + uploadBon + seedBon

        totalBon += torrentBon
    return totalBon

def Good_model(seedtime,torrents):
    totalBon = 0

    for torrent in torrents:
        ageBon = 0
        seedBon = 0
        uploadBon = 0
        size = torrent[0]
        age = torrent[1]
        uploaded = torrent[2]

        if size >= 1024 and size < 25600: # everyday torrents
            sizeBon = 0.25 * day
        elif size >= 25600 and size < 102400: # large torrents
            sizeBon = 0.50 * day
        elif size >= 102400: # huge torrents
            sizeBon = 0.75 * day
        else: # <1MiB
            sizeBon = 0 * day

        if age+seedtime >= 6*months:
            if age+seedtime >= 12*months:
                ageBon = 1.5 * day
            else:
                ageBon = 1 * day

        if seedtime >= 1 * months and seedtime < 2 * months:
            seedBon = 0.25 * day
        elif seedtime >= 2 * months and seedtime < 3 * months:
            seedBon = 0.50 * day
        elif seedtime >= 3 * months and seedtime < 6 * months:
            seedBon = 0.75 * day
        elif seedtime >= 6 * months and seedtime < 12 * months:
            seedBon = 1 * day
        elif seedtime >= 12 * months:
            seedBon = 2 * day

        torrentBon = sizeBon + ageBon + uploadBon + seedBon

        totalBon += torrentBon
    return totalBon

curr_y_casual = []
curr_total_casual = 0
curr_y_totals_casual = []
curr_upload_from_BON_casual = []
curr_y_poweruser = []
curr_total_poweruser = 0
curr_y_totals_poweruser = []
curr_upload_from_BON_poweruser = []
for seed_day in range(0,600):
    curr_y_casual.append(curr_model(seed_day, torrent_list_casual))
    curr_total_casual += curr_model(seed_day, torrent_list_casual)
    curr_y_totals_casual.append(curr_total_casual)
    curr_upload_from_BON_casual.append(curr_model(seed_day, torrent_list_casual) / 50)
    curr_y_poweruser.append(curr_model(seed_day, torrent_list_poweruser))
    curr_total_poweruser += curr_model(seed_day, torrent_list_poweruser)
    curr_y_totals_poweruser.append(curr_total_poweruser)
    curr_upload_from_BON_poweruser.append(curr_model(seed_day, torrent_list_poweruser) / 50)


prop_y_casual = []
prop_total_casual = 0
prop_y_totals_casual = []
prop_upload_from_BON_casual = []
prop_y_poweruser = []
prop_total_poweruser = 0
prop_y_totals_poweruser = []
prop_upload_from_BON_poweruser = []
for seed_day in range(0,600):
    prop_y_casual.append(prop_model(seed_day, torrent_list_casual))
    prop_total_casual += prop_model(seed_day, torrent_list_casual)
    prop_y_totals_casual.append(prop_total_casual)
    prop_upload_from_BON_casual.append(prop_model(seed_day, torrent_list_casual) / 1200)
    prop_y_poweruser.append(prop_model(seed_day, torrent_list_poweruser))
    prop_total_poweruser += prop_model(seed_day, torrent_list_poweruser)
    prop_y_totals_poweruser.append(prop_total_poweruser)
    prop_upload_from_BON_poweruser.append(prop_model(seed_day, torrent_list_poweruser) / 1200)

good_y_casual = []
good_total_casual = 0
good_y_totals_casual = []
good_upload_from_BON_casual = []
good_y_poweruser = []
good_total_poweruser = 0
good_y_totals_poweruser = []
good_upload_from_BON_poweruser = []
for seed_day in range(0,600):
    good_y_casual.append(Good_model(seed_day, torrent_list_casual))
    good_total_casual += Good_model(seed_day, torrent_list_casual)
    good_y_totals_casual.append(good_total_casual)
    good_upload_from_BON_casual.append(Good_model(seed_day, torrent_list_casual) / 500)
    good_y_poweruser.append(Good_model(seed_day, torrent_list_poweruser))
    good_total_poweruser += Good_model(seed_day, torrent_list_poweruser)
    good_y_totals_poweruser.append(good_total_poweruser)
    good_upload_from_BON_poweruser.append(Good_model(seed_day, torrent_list_poweruser) / 500)

# BON accruance plot
fig1=plt.figure()
ax1=fig1.add_subplot(111)
ax1.set_xlim(0,600)
ax1.set_ylim(0,50000000)
ax1.grid(True)
ax1.set(title="Current BON System vs Good BON System vs Proposed BON System", xlabel="Seedtime (Days)", ylabel="Total BON Generated")
x_days = np.arange(0.,600.)
ax1.plot(x_days, curr_y_totals_casual, color='red', linestyle='solid', linewidth=2, label='CurCas')
ax1.plot(x_days, prop_y_totals_casual, color='blue', linestyle='solid', linewidth=2, label='ProCas')
ax1.plot(x_days, good_y_totals_casual, color='purple', linestyle='solid', linewidth=2, label='GoodCas')
ax1.plot(x_days, curr_y_totals_poweruser, color='red', linestyle='dashed', linewidth=2, label='CurPro')
ax1.plot(x_days, prop_y_totals_poweruser, color='blue', linestyle='dashed', linewidth=2, label='ProPro')
ax1.plot(x_days, good_y_totals_poweruser, color='purple', linestyle='dashed', linewidth=2, label='GoodPro')
for months in range(0,21,3):
    ax1.axvline(30*months, 0, 5000, linestyle='dashed',color ='green')
    ax1.text(30*months + 10, 1200, (str(months)+' months'), rotation=90, ha='left', va='bottom', color='green')
ax1.legend(loc='lower right')
plt.show()

# BON generation rate plot
fig2=plt.figure()
ax2=fig2.add_subplot(111)
ax2.set_xlim(0,600)
ax2.set_ylim(0,100000)
ax2.grid(True)
ax2.set(title="Current BON System vs Good BON System vs Proposed BON System", xlabel="Seedtime (Days)", ylabel="BON Generated per Day")
x_days = np.arange(0.,600.)
ax2.plot(x_days, curr_y_casual, color='red', linestyle='solid', linewidth=2, label='CurCas')
ax2.plot(x_days, prop_y_casual, color='blue', linestyle='solid', linewidth=2, label='ProCas')
ax2.plot(x_days, good_y_casual, color='purple', linestyle='solid', linewidth=2, label='GoodCas')
ax2.plot(x_days, curr_y_poweruser, color='red', linestyle='dashed', linewidth=2, label='CurPro')
ax2.plot(x_days, prop_y_poweruser, color='blue', linestyle='dashed', linewidth=2, label='ProPro')
ax2.plot(x_days, good_y_poweruser, color='purple', linestyle='dashed', linewidth=2, label='GoodPro')
for months in range(0,21,3):
    ax2.axvline(30*months, 0, 5000, linestyle='dashed',color ='green')
    ax2.text(30*months + 10, 1200, (str(months)+' months'), rotation=90, ha='left', va='bottom', color='green')
ax2.legend(loc='lower right')
plt.show()

# Upload Credit generation rate plot
fig3=plt.figure()
ax3=fig3.add_subplot(111)
ax3.set_xlim(0,600)
ax3.set_ylim(0,2000)
ax3.grid(True)
ax3.set(title="Current BON System vs Good BON System vs Proposed BON System", xlabel="Seedtime (Days)", ylabel="Upload Credit Generated per Day (GiB)")
x_days = np.arange(0.,600.)
ax3.plot(x_days, curr_upload_from_BON_casual, color='red', linestyle='solid', linewidth=2, label='CurCas')
ax3.plot(x_days, prop_upload_from_BON_casual, color='blue', linestyle='solid', linewidth=2, label='ProCas')
ax3.plot(x_days, good_upload_from_BON_casual, color='purple', linestyle='solid', linewidth=2, label='GoodCas')
ax3.plot(x_days, curr_upload_from_BON_poweruser, color='red', linestyle='dashed', linewidth=2, label='CurPro')
ax3.plot(x_days, prop_upload_from_BON_poweruser, color='blue', linestyle='dashed', linewidth=2, label='ProPro')
ax3.plot(x_days, good_upload_from_BON_poweruser, color='purple', linestyle='dashed', linewidth=2, label='GoodPro')
for months in range(0,21,3):
    ax3.axvline(30*months, 0, 5000, linestyle='dashed',color ='green')
    ax3.text(30*months + 10, 1200, (str(months)+' months'), rotation=90, ha='left', va='bottom', color='green')
ax3.legend(loc='lower right')
plt.show()

print('# torrents:' + str(len(torrent_list_casual)))
print('Total size (GiB):' + str((np.sum(torrent_list_casual[:, 0])) / 1000))
print('Total Self Uploaded: ' + str((np.sum(torrent_list_casual[:, 2]))))
print('Average size (MiB):' + str((np.average(torrent_list_casual[:, 0]))))
print('Sum BON for Current Model: ' + str(curr_total_casual))
print('Sum BON for Proposed Model: ' + str(prop_total_casual))
print('Sum BON for Good Model: ' + str(good_total_casual))

print('# torrents:' + str(len(torrent_list_poweruser)))
print('Total size (GiB):' + str((np.sum(torrent_list_poweruser[:, 0])) / 1000))
print('Total Self Uploaded: ' + str((np.sum(torrent_list_poweruser[:, 2]))))
print('Average size (MiB):' + str((np.average(torrent_list_poweruser[:, 0]))))
print('Sum BON for Current Model: ' + str(curr_total_poweruser))
print('Sum BON for Proposed Model: ' + str(prop_total_poweruser))
print('Sum BON for Good Model: ' + str(good_total_poweruser))