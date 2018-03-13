from sklearn.datasets.base import Bunch
import pickle
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

def writeBunchObj(path,bunchObj):
    file_obj=open(path,"wb")
    pickle.dump(bunchObj,file_obj)
    file_obj.close()

def readBunchObj(path):
    file_obj=open(path,"rb")
    bunch=pickle.load(file_obj)
    file_obj.close()
    return bunch

bunch = readBunchObj(r'data\tf-idf\train.dat')
tfidfspace=Bunch(target_name=bunch.target,label=bunch.label,tdm=[],vocabulary={})
vectorizer=TfidfVectorizer(sublinear_tf=True,max_df=0.5,min_df=0.0012)
transformer=TfidfTransformer()#该类会统计每个词语的TF-IDF权值
tfidfspace.tdm=vectorizer.fit_transform(bunch.word_list)
tfidfspace.vocabulary=vectorizer.vocabulary_
print(len(tfidfspace.vocabulary))
space_path=r"data\tf-idf\tfidfspace.dat"
writeBunchObj(space_path,tfidfspace)