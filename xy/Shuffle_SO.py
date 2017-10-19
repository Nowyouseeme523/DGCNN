import cPickle as p
import numpy as np
import sys, os

# config = 'test'

# numCV = 1101
# numTrain = 161391#159274#176362
# numTrain = 1
# numTest = 2210
# d = '../../network_' + config
import gl

network = []
y = []
# num = numTest

# datadir =  '../../network/'
datadir = gl.targetdir
pronum = gl.numOut  # 104
config = 'data'
print 'begin!'
procount = 0
for pi in xrange(1, pronum + 1):
    subdir = str(pi) + '/'
    # print '111111111111111111111'
    print 'pi = ', str(pi)
    '''
    if len(os.listdir(datadir + subdir))<500:
        continue
    '''
    procount += 1
    print 'procount = ', procount
    for onefile in os.listdir(datadir + subdir):
        # print 'oneoneoneoneone!!!!!!!!!! '
        filename = onefile
        onefile = datadir + subdir + onefile
        network.append((onefile, procount - 1))

np.random.seed(2018)
np.random.shuffle(network)

print len(network)
numTrain = int(.7 * len(network))
print 'numTrain : ', numTrain
print 'numCV : ', len(network) - numTrain
print 'final procount = ', procount
'''
58000
numTrain :  34800
numCV :  11600
numTest 11600
final procount =  116
'''
f = file(config + '_train', 'wb')
f_y = file(config + '_ytrain.txt', 'w')
for i in xrange(0, numTrain):
    (tf, ti) = network[i]

    net = file(tf, 'rb')
    f.write(net.read())
    net.close()
    # print ti
    f_y.write(str(ti) + '\n')
f.close()
f_y.close()

f = file(config + '_CV', 'wb')
f_y = file(config + '_yCV.txt', 'w')
for i in xrange(numTrain, len(network)):
    (tf, ti) = network[i]
    net = file(tf, 'rb')
    f.write(net.read())
    net.close()
    f_y.write(str(ti) + '\n')
f.close()
f_y.close()

f = file(config + '_test', 'wb')
f_y = file(config + '_ytest.txt', 'w')
for i in xrange(numTrain, numTrain+2):
    (tf, ti) = network[i]
    net = file(tf, 'rb')
    f.write(net.read())
    net.close()
    f_y.write(str(ti) + '\n')
f.close()
f_y.close()

print 'Done!!'