#coding:utf-8
import demjson,jieba,jieba.posseg as pseg

def saveFile(data,i):
    if i>10:
        path = "data\\train_fenci\\result_" + str(i-10) +".txt"
    else:
        path = "data\\test_fenci\\result_"+str(i)+".txt"
    file = open(path,'a+b')
    file.read()
    for d in data:
        d = str(d)+" "
        file.write(d.encode('utf-8'))
    n = "\r\n"
    file.write(n.encode('utf-8'))
    file.close()

path1 = "data\\test_first\\auto_test.json"
path2 = "data\\test_first\\jr_test.json"
path3 = "data\\test_first\\cul_test.json"
path4 = "data\\test_first\\house_test.json"
path5 = "data\\test_first\\it_test.json"
path6 = "data\\test_first\\jk_test.json"
path7 = "data\\test_first\\ny_test.json"
path8 = "data\\test_first\\ty_test.json"
path9 = "data\\test_first\\yl_test.json"
path10 = "data\\test_first\\mil_test.json"
path11 = "data\\train_first\\auto_train.json"
path12 = "data\\train_first\\jr_train.json"
path13 = "data\\train_first\\cul_train.json"
path14 = "data\\train_first\\house_train.json"
path15 = "data\\train_first\\it_train.json"
path16 = "data\\train_first\\jk_train.json"
path17 = "data\\train_first\\y_train.json"
path18 = "data\\train_first\\ty_train.json"
path19 = "data\\train_first\\yl_train.json"
path20 = "data\\train_first\\mil_train.json"


texttype = {
    1:path1,
    2:path2,
    3:path3,
    4:path4,
    5:path5,
    6:path6,
    7:path7,
    8:path8,
    9:path9,
    10:path10,
    11:path11,
    12:path12,
    13:path13,
    14:path14,
    15:path15,
    16:path16,
    17:path17,
    18:path18,
    19:path19,
    20:path20,
    }
    

#获取json文件中的内容
counttype = 0

#停用词文件
stop_path = "data\stop_word.txt"
stop_file = open(stop_path,'r',encoding='utf-8')
lines1 = stop_file.readlines()
stopword = []
for line1 in lines1:
    stopword.append(line1.strip())

for i in range(1,21):
    #获取文件路径
    path = texttype[i]
    count = 0
    counttype += 1
    print("****************************" + str(i) + "**************************")

    #读取文件
    file = open(path ,'r+',encoding = "utf-8")

    while 1:
        line = file.readline()
        if not line:
            break
        else:
            count = count + 1
            print(count)

            
            data = demjson.decode(line)
            content = data['content']
            words = jieba.cut(content,cut_all=False)
            words = pseg.cut(content)
            s = []
            cixing = {"n","nt","nz","nl","ng"}
        
            for w in words:
                if w.flag in cixing :
                    if((len(w.word)) > 1) and (w.word not in stopword):
                        s.append(w.word)
                    
            if len(s) >= 10:
                saveFile(s,i)
       

               



            
      

        
        

