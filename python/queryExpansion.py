import gensim
#model = gensim.models.KeyedVectors.load_word2vec_format("/home/trec/wiki/word2vec_gensim", binary=False)
#model = gensim.models.word2vec.Word2Vec.load("/home/trec/wiki/word2vec_gensim")


#model.most_similar("queen")
from uitls import getTitle
from gen_extend_word import actualQE
from gen_extend_word import actualQEwith2_1

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)





model=gensim.models.Word2Vec.load("/home/trec/liujinlong/word2vec_withoutstem/trec_withoutstem")

#print (actualQE(['basketball', 'player'], 5, 10, 5, model))
#print (actualQE(['basketball'], 30, 10, 5, model))
#print (actualQE(['player'], 30, 10, 5, model))


path = '/home/trec/jiaoliying/whooshDemo/topic/core_nist.txt'

listId = []
listTitle = []
(listId, listTitle) = getTitle(path)

stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn','a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'identify']


with open('queryExpansionResult.txt','w+') as fw:
      for i in range(0, len(listId)):
        title  = listTitle[i].split('$')
        t = title[0].split()
        desc = title[1].replace('\n', '').split(',')
        s = []
        for low in t:
            low1 = low.lower()
            temp = low1.split('-')
            for temp2 in temp:
                if(temp2 not in stopwords):
                    s.append(temp2)
        
        fw.write(listId[i])
  
        fw.write(':')
        titleWord = title[0].split()
        for word in titleWord:
            fw.write(word + '^1.5')
            fw.write(' ')
        #try:
            #temp = model.most_similar(['%s'%(j),] ,topn=3)
        result = actualQE(s, 30, 100, 5, model)
        #result = actualQEwith2_1(s, 5, model)
        #result = actualQEwith2_1(['queen'], 5, model)
        #except KeyError:
            #temp=[('',0)]
            #result = []
        for k in result:
            fw.write(k)
            fw.write(' ')
        for d in desc:
            if d.lower() not in stopwords:
                fw.write(d)
                fw.write(' ')
        fw.write('\n')
























