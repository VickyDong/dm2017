from sklearn.datasets.base import Bunch
import pickle
from sklearn.feature_extraction.text import TfidfTransformer  # TF-IDF向量转换类
from sklearn.feature_extraction.text import TfidfVectorizer  # TF-IDF向量生成类

def readBunchObj(path):
    file_obj = open(path, "rb")
    bunch = pickle.load(file_obj)
    file_obj.close()
    return bunch

def writeBunchObj(path, bunchobj):
    file_obj = open(path, "wb")
    pickle.dump(bunchobj, file_obj)
    file_obj.close()

bunch = readBunchObj(r"data\tf-idf\test.dat")

testSpace = Bunch(target_name=bunch.target, label=bunch.label, tdm=[], vocabulary={})
trainBunch = readBunchObj(r"data\tf-idf\tfidfspace.dat")
vectorizer = TfidfVectorizer(vocabulary=trainBunch.vocabulary)
transformer = TfidfTransformer()
testSpace.tdm = vectorizer.fit_transform(bunch.word_list)
testSpace.vocabulary = trainBunch.vocabulary
print(testSpace.tdm.shape)

space_path = r"data\tf-idf\testspace.dat"
writeBunchObj(space_path, testSpace)

