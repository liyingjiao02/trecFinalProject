import gensim
import numpy as np
##return vector lists
def getSim(model, query, topk): 
    
    #model=gensim.models.Word2Vec.load("/home/trec/liujinlong/word2vec_withoutstem/trec_withoutstem")
    wordArray = model.most_similar(query,topn=topk )
    #print (wordArray)    
    
    #print (wordarray)#[('princess', 0.8159459829330444), ('empress', 0.7777712345123291)...]

    #print (model[wordarray[0][0]]) 

    QEList = np.zeros((topk,100))
    i = 0
    for temp in wordArray:
        QEList[i] = model[temp[0]]
        i += 1  
    return QEList
   
##return vector lists
def getSimFromVector(model, vector, topk):
    #model=gensim.models.Word2Vec.load("/home/trec/liujinlong/word2vec_withoutstem/trec_withoutstem")
    wordArray = model.most_similar(positive=[vector],topn=topk)
    #print (wordArray)    
    
    QEList = np.zeros((topk,100))
    i = 0
    for temp in wordArray:
        QEList[i] = model[temp[0]]  
        i += 1
    return QEList

    
def getWordByVector(model, vector):
    #model=gensim.models.Word2Vec.load("/home/trec/liujinlong/word2vec_withoutstem/trec_withoutstem")
    word = model.most_similar(positive=[queen_vec],topn=1)
    return word[0][0]
    
   
    
#model=gensim.models.Word2Vec.load("/home/trec/liujinlong/word2vec/trec")
#print(model.similarity(tem('beauty')))

#print(model.most_similar(positive=['woman', 'king'], negative=['man']))
#queen_vec=model['queen']
#print(model.most_similar(positive=[queen_vec],topn=2))

#print(model[stem('beautiful')])
# 可以考虑函数多一个参数，model，这样每次函数操作的时候，只用读入一次，
# 不用进行额外的文件IO

if __name__ == "__main__":
    
    model=gensim.models.Word2Vec.load("/home/trec/liujinlong/word2vec_withoutstem/trec_withoutstem")
    print (getSim(model,'queen',5)[0])
    print ('-----------------')
    
    queen_vec=model['queen']
    print (getSimFromVector(model,queen_vec,5)[0])
    print ('-----------------')
    
    print (getWordByVector(model,queen_vec))
    




