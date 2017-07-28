import gensim
#model = gensim.models.KeyedVectors.load_word2vec_format("/home/trec/wiki/word2vec_gensim", binary=False)
#model = gensim.models.word2vec.Word2Vec.load("/home/trec/wiki/word2vec_gensim")


#model.most_similar("queen")
from uitls import getTitle
from gen_extend_word_test import actualQE
from gen_extend_word_test import actualQEwith2_1

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)





model=gensim.models.Word2Vec.load("/home/trec/liujinlong/word2vec_withoutstem/trec_withoutstem")

result = actualQEwith2_1(['cult', 'lifestyles'], 5, model)

print (result)
