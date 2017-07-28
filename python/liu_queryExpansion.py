import gensim
#model = gensim.models.KeyedVectors.load_word2vec_format("/home/trec/wiki/word2vec_gensim", binary=False)
#model = gensim.models.word2vec.Word2Vec.load("/home/trec/wiki/word2vec_gensim")


#model.most_similar("queen")
from uitls import getTitle
from liu_gen_extend_word import actualQE
from liu_with_stem_set_gen_extend_word_test import actualQEwith2_1

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

with open('liuqueryExpansionResult.txt','w+') as fw:
    for i in range(0, len(listId)):
        t = listTitle[i].split()
        s = []
        for low in t:
            s.extend(low.lower().split('-'))
        
        fw.write(listId[i])
  
        fw.write(':')
        fw.write(listTitle[i])
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
        fw.write('\n')
























