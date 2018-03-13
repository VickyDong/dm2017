#coding:utf-8
import pickle

def readBunchObj(path):
    file_obj=open(path,"rb")
    bunch=pickle.load(file_obj)
    file_obj.close()
    return bunch

def turn(inputPath,outputPath):
    bunch = readBunchObj(inputPath)
    out = open(outputPath,'w')
    for i in range(bunch.tdm.shape[0]):
        label = bunch.label[i]
        out.write(str(label)+' ')
        write = {}
        for j in range(7094):
            if bunch.tdm[i,j]!= 0:
                write[j] = bunch.tdm[i,j]
            else:
                pass
        outline = ''
        for key in write.keys():
            outline = outline + str(key) + ':' + str(write[key]) + ' '
        out.write(outline+'\n')
        print(i)

turn(r'data\tf-idf\tfidfspace.dat',r'data\data_final\train_lib')
turn(r'data\tf-idf\testspace.dat',r'data\data_final\test_lib')