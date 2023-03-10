import sys

if len(sys.argv) == 4:
    print ('The file name is', sys.argv[0])
    print ('The firs argument is', sys.argv[1])
    print ('The second argument is', sys.argv[2])
    print ('The third argument is', sys.argv[3])
else:
    print ('The introduced parameters are incorrect, check them')
    print('The instructions should be like "python clase09_1_Brando.py 0 1 2"')