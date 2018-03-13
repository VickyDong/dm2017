#coding:utf-8
test = open(r'data\data_final\test_lib','r')
data_test = []
lines = test.readlines()
for line in lines:
    data_test.append(line.split()[0])

def evaluate(predictPath):
    predict = open(predictPath,'r')
    data_predict = predict.read().split('\n')
    predict.close()

    # 存储每一类文档的数量
    test_account = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for item in data_test:
        test_account[int(item)] += 1

    # 存储预测结果里每一类的数量
    predict_account = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for item in data_predict:
        predict_account[int(item)] += 1

    # 存储预测正确的每一类的数量
    correct = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for i in range(len(data_predict)):
        if data_predict[i] == data_test[i]:
            correct[int(data_test[i])] += 1

    #计算每一类的正确率、召回率、F-score
    precision_list = []
    recall_list = []
    fScore_list = []
    for i in range(1,11):
        accuracy = float(correct[i]/predict_account[i])
        precision_list.append(accuracy)
        recall = float(correct[i]/(correct[i]+test_account[i]-correct[i]))
        recall_list.append(recall)

    all_correct = 0 #总体的预测正确数量
    all_wrong = 0 #总体的预测错误数量

    for key in correct.keys():
        all_correct += correct[key]
        all_wrong = all_wrong + test_account[key] - correct[key]

    # 计算总体评价标准
    all_precision = float(all_correct/len(data_test))
    all_recall = float(sum(recall_list)/len(recall_list))
    f_score = float((2*all_precision*all_recall)/(all_precision+all_recall))

    type = {
        1:'汽车',
        2:'金融',
        3:'文化',
        4:'房产',
        5:'IT',
        6:'健康',
        7:'能源',
        8:'体育',
        9:'娱乐',
        10:'军事'
    }

    for i in range(0,10):
        print(type[i+1]+'\t: Precision:'+str(precision_list[i])+' \tRecall:'+str(recall_list[i]))

    print('Precision:'+str(all_precision))
    print('Recall:'+str(all_recall))
    print('F-score:'+str(f_score))

print('Bayes:')
evaluate(r'data\bayes\bayes_result.txt')

print('\nLibsvm:')
evaluate(r'data\libsvm\libsvm_result.txt')