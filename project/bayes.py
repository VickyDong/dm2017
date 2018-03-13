#coding:utf-8

testPath = r'data\data_final\test_lib'
trainPath = r'data\data_final\train_lib'

train_amount = 0 #训练集总数
test_amount = 0 #测试集总数
len_dict = 7094  #词典维度

# 计算先验概率
train_account = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
trainFile = open(trainPath,'r')
line = trainFile.readline()
while line:
    train_account[int(line.split()[0])] += 1
    train_amount += 1
    line = trainFile.readline()
trainFile.close()

test_account = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
testFile = open(testPath,'r')
line = testFile.readline()
while line:
    test_account[int(line.split()[0])] += 1
    test_amount += 1
    line = testFile.readline()
testFile.close()

test_p_yi = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
for key in range(1, 11):
    test_p_yi[key] = float(test_account[key] / test_amount)

# 训练模型
p = {}
model = open(r'data\bayes\model_output.txt','w')
train = open(trainPath,'r')

for lineNo in range(train_amount):
    line = train.readline()
    list = line.split(' ')
    type_id = int(list[0])
    if type_id not in p:
        p[type_id] = {}
    for item in list[1:-1]:
        word_id = item.split(':')[0]
        if word_id not in p[type_id]:
            p[type_id][word_id] = 1
        else:
            p[type_id][word_id] += 1

for key1 in p.keys():
    for key2 in p[key1].keys():
        p[key1][key2] = float((p[key1][key2]+1)/(train_account[key1]+10))

    out = str(p[key1]).replace('{','').replace('}','') + '\n'
    model.write(out)

model.close()
train.close()

laplace = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0} #拉普拉斯平滑
for key in range(1,11):
    laplace[key] = float(1/ (train_account[key]+10))




# 开始预测
output = open(r'data\bayes\bayes_result.txt','w')
testF = open(testPath,'r')
line = testF.readline()
i = 0
while line:
    i += 1
    test_list = line.split(' ')
    test = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    No_list = []
    for item in test_list[1:-1]:
        No_list.append(item.split(':')[0])
    for type in range(1,11):
        this = 1.0
        for item in No_list:
            if item in p[type]:
                this *= p[type][item]
            else:
                this *= laplace[type]
        test[type] = this * test_p_yi[type]
    predict = max(test, key=lambda x: test[x])
    outputLine = str(predict)
    if i!= test_amount:
        output.write(outputLine+'\n')
    else:
        output.write(outputLine)
    line = testF.readline()
