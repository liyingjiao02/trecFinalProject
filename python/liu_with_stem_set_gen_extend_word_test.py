import gensim
import numpy as np
from whoosh.lang.porter import stem

## compute similarity of two vectors
## param:
## vec1: vector 1; vec2: vector 2
## return:
## con_angle: the similarity of the two vectors

def cosine(vec1, vec2):
    Lvec1 = np.sqrt(vec1.dot(vec1))
    Lvec2 = np.sqrt(vec2.dot(vec2))
    cos_angle = vec1.dot(vec2) / (Lvec1 * Lvec2)

    return cos_angle

## 2.3 Pre-retrieval incremental kNN based approach
## param:
## queryVec: query word vector
## QEList: query extend list of the query word
## K: prune last K vector of QE according to the similarity
## atMost: the most number of query extend words selected for each query word
## return:
## qeFinal: the final query extend list of the word

def incrementle(queryVec, QEList, K, atMost):
    qeFinal = []
    for i in range(atMost):
        wordListOrder = sorted(QEList, key=lambda qe: cosine(qe, queryVec), reverse=True)
        length = len(wordListOrder)
        queryVec = wordListOrder[0]
        qeFinal.append(queryVec)
        if length <= K:
            return qeFinal
        QEList = wordListOrder[1:length - K]

    return qeFinal


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
    print ('sim ' + str(len(QEList)))  
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
    print ('simfromvec ' + str(len(QEList)))
    return QEList

    
def getWordByVector(model, vector):
    #model=gensim.models.Word2Vec.load("/home/trec/liujinlong/word2vec_withoutstem/trec_withoutstem")
    word = model.most_similar(positive=[vector],topn=1)
    return word[0][0]

## generate integrated query from query list
## param:
## queryList: the query word list
## return:
## integratedQueryList: integrated query list
def genIntegratedQuery(queryVecList):
    length = len(queryVecList)
    integratedQueryList = []
    for i in range(length - 1):
        integratedQueryList.append(queryVecList[i] + queryVecList[i+1])
    return integratedQueryList

## 2.1
## compute the mean similarity of candidate word between query list
## param:
## candidateWord: candidate word (query extend)
## queryList: the query word list
## return:
## the mean similarity
def meanSim(candidateWord, queryList):
    simSum = 0.0
    for query in queryList:
        simSum += cosine(candidateWord, query)
    return simSum / len(queryList)

    
## call meanSim to get final query extend vector list
## param:
## queryList: the query word list
## K: prune last K vector of QE according to the similarity
## L: the most number of query extend words selected for each query word
## topN: the top number selected
## return:
## the actual query extend word
def actualQE(queryList, K, L, topN, model):
    autualQueryExtend = []
    queryVectorList = []
    for query in queryList:
        tmpVec = model[query]
        queryVectorList.append(tmpVec)
        autualQueryExtend.extend(incrementle(tmpVec, getSim(model, query, 1000), K, L))
    integrateQueryList = genIntegratedQuery(queryVectorList)
    for integrateQuery in integrateQueryList:
        autualQueryExtend.extend(incrementle(integrateQuery, getSimFromVector(model, integrateQuery, 1000), K, L))
    finalQueryList = queryVectorList + integrateQueryList
    sorted(autualQueryExtend, key=lambda t: meanSim(t, finalQueryList), reverse=True)
    if len(autualQueryExtend) < topN:
        autualQueryExtendVector = autualQueryExtend
    else:
        autualQueryExtendVector = autualQueryExtend[0:topN]
    autualQueryExtendWord = []
    for vec in autualQueryExtendVector:
        autualQueryExtendWord.append(getWordByVector(model, vec) + "^" + str(meanSim(vec, finalQueryList)))
    return autualQueryExtendWord   

def actualQEwith2_1(queryList, topN, model):
    candidateWord = []
    queryVectorList = []
    for query in queryList:
        queryVectorList.append(model[query])
        candidateWord.extend(getSim(model, query, topN))
    integrateQueryList = genIntegratedQuery(queryVectorList)
    for integrateQuery in integrateQueryList:
        candidateWord.extend(getSimFromVector(model, integrateQuery, topN))
    finalQueryList = queryVectorList + integrateQueryList


    #remove the repeated candidate words
    QESet = set()
    #queryList.extend(candidateWord)
    for QE in queryList:
        if stem(QE.lower()) not in QESet:
            QESet.add(stem(QE.lower()))
    actualCandidateWord=[]
    for word in candidateWord:
        if stem(word.lower()) not in QESet:
            QESet.add(stem(word.lower()))
            actualCandidateWord.append(word)
    candidateWord=actualCandidateWord


    for q in candidateWord:
        print (getWordByVector(model, q))
        print (meanSim(q, finalQueryList))
    candidateWord = sorted(candidateWord, key=lambda t: meanSim(t, finalQueryList), reverse=True)
    print ('finish')
    for q in candidateWord:
        print (getWordByVector(model, q)) 
        print (meanSim(q, finalQueryList))
    if len(candidateWord) < topN:
        autualQueryExtendVector = candidateWord
    else:
        autualQueryExtendVector = candidateWord[0:topN]
    autualQueryExtendWord = []
    for vec in autualQueryExtendVector:
        autualQueryExtendWord.append(getWordByVector(model, vec) + "^" + str(meanSim(vec, finalQueryList)))

    return autualQueryExtendWord

    
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
#    print (getSim(model,'queen',5)[0])
#    print ('-----------------')
    
#    queen_vec=model['queen']
#    print (getSimFromVector(model,queen_vec,5)[0])
#    print ('-----------------')
    
    print (actualQE(['basketball', 'player'], 5, 10, 5, model))
    print (actualQE(['basketball'], 30, 10, 5, model))
    print (actualQE(['player'], 30, 10, 5, model))




