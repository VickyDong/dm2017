#coding；utf-8
from sklearn.datasets.base import Bunch
import pickle

trainBunch = Bunch(target=[],label=[],word_list=[])
testBunch = Bunch(target=[],label=[],word_list=[])

def loadFile(path,type,bunchType):
    bunchType.target.append(type)
    file = open(path,'r',encoding='utf-8')
    lines = file.readlines()
    for line in lines:
        bunchType.word_list.append(line)
        bunchType.label.append(type)

def writeBunchObj(path,bunchObj):
    file_obj=open(path,"wb")
    pickle.dump(bunchObj,file_obj)
    file_obj.close()

def readBunchObj(path):
    file_obj=open(path,"rb")
    bunch=pickle.load(file_obj)
    file_obj.close()
    return bunch

if __name__ == '__main__':
    for i in range(1,11):
        num = str(i)
        loadFile(r'data\test_fenci\result_' + num + '.txt',num,testBunch)
        loadFile(r'data\train_fenci\result_' + num + '.txt',num,trainBunch)
        print('load type '+num +' complete!')

    writeBunchObj(r'data\tf-idf\test.dat',testBunch)
    writeBunchObj(r'data\tf-idf\train.dat',trainBunch)