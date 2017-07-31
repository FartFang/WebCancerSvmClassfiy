# from LIBSVM.svm.svmutil import *
from Bio import SeqIO
import re

from LIBSVM.svm.svmutil import svm_read_problem, svm_load_model, svm_predict


def turnToSvmData():
    testData=[]
    file=open('/Users/fangziming/Predict/App/testData.txt','a')
    for seq_record in SeqIO.parse('/Users/fangziming/Predict/App/data.txt','fasta'):
        testData.append(seq_record.seq)
    gap1=['L.R', 'P.A', 'N.D', 'N.V', 'Q.P', 'Q.L', 'N.W', 'D.T', 'N.G', 'R.R', 'A.P', 'T.H', 'H.M', 'L.E', 'K.M', 'P.H', 'L.P', 'T.D', 'Q.A', 'P.Q', 'R.Q']
    file.write('1 ')
    for m in range(0,len(gap1)):
        s=str(testData)
        pattern=re.compile(gap1[m])
        obj=pattern.findall(s)
        a=float(len(obj))/len(s)*3
        file.write(str(m+1)+':'+str(round(a,3)))
        file.write(' ')
    file.write('\n')
    file.close()
    return 1
def scale():
    count = 0
    count = len(open('/Users/fangziming/Predict/App/testData.txt','rU').readlines())
    import os
    os.system('/Users/fangziming/Desktop/libsvm-3.22/svm-scale  /Users/fangziming/Predict/App/testData.txt > /Users/fangziming/Predict/App/predictData.txt ')
    return count
def predict(count):
    y, x = svm_read_problem('/Users/fangziming/Predict/App/predictData.txt')
    m=svm_load_model('/Users/fangziming/Predict/App/trianMode.model')
    p1_label, p1_acc, p1_val = svm_predict(y[405:406], x[405:406], m, '-b 1')
    p_label, p_acc, p_val = svm_predict(y[count-1:],x[count-1:],m,'-b 1')
    print p_val[0][1]
    a='probability of cancer:'+str(p_val[0][0])
    b='\nprobability of non-cancer:'+ str(p_val[0][1])
    type=''
    if p_val[0][1]>0.5:
        type='Cancerlectin'
    else:
        type='NonCancerlectin'

    m = {'probabilityOfCancer':str(p_val[0
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   






































































                                   ][1]),'probabilityOfNonCancer':str(p_val[0][0]),'type':type}
    if p_val[0][1]==p1_val[0][1]:
        return -1
    return m

# turnToSvmData()
# count = scale()
# print predict(count)
