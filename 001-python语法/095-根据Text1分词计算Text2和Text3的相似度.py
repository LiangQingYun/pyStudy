# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import nltk
import jieba

nltk.download('stopwords')
stop_words = set(stopwords.words('chinese')) # 加载停用词

def chinese_word_tokenize(text):
    """
       设置为ik分词器 中文分词
    """
    return jieba.lcut(text)

def get_vectorizer(text):
    # 设置分词器为ik分词器
    tokens = chinese_word_tokenize(text)
    tokens_filtered = [word for word in tokens if not word in stop_words]
    tokens_str = " ".join(tokens_filtered)
    vectorizer = TfidfVectorizer()
    vectorizer.fit_transform([tokens_str])  # 传入分词后的文本
    return vectorizer


def calculate_similarity(vectorizer, text2, text3):
    # 对text2进行分词，并计算TF-IDF权重
    tokens2 = chinese_word_tokenize(text2)
    tokens2_filtered = [word for word in tokens2 if not word in stop_words]
    tokens2_str = " ".join(tokens2_filtered)
    tfidf2 = vectorizer.transform([tokens2_str])

    # 对text3进行分词，并计算TF-IDF权重
    tokens3 = chinese_word_tokenize(text3)
    tokens3_filtered = [word for word in tokens3 if not word in stop_words]
    tokens3_str = " ".join(tokens3_filtered)
    tfidf3 = vectorizer.transform([tokens3_str])

    # 计算text2和text3的相似度
    similarity = (tfidf2 * tfidf3.T).A[0][0]

    return similarity





if __name__ == '__main__':
    text1 = "0-12个月宝宝，服用葡萄糖酸钙锌口服溶液的正确方法.mp4----------你好我是阿诺健康助手不萄糖酸钙锌口服溶液怎么服用呢零到六个月的宝宝可以一天一次一次2.5毫升一只分两次服用喝奶后半小时不用如果担心宝宝太小不习惯喝的话也可以妈妈服用营养会通过乳汁输送给孩子六到12个月的宝宝也是一天一次不同的是这个年龄段的宝宝一次要喝五毫升和奶或者吃辅食后半小时服用葡萄糖酸钙锌口服溶液不同年龄段服用方法是不一样的不要吃错了哟 1-18岁服用葡萄糖酸钙锌口服溶液的正确方法.mp4----------你好我是阿诺健康助手不萄糖酸钙锌口服溶液怎么服用那一岁到五岁的小朋友用来保健预防缺钙缺锌的话一天一次一副好身建议在早晚餐后服用效果更好如果小朋友已经出现缺钙或缺锌的症状那就要加大剂量一天两次一次五毫升也是早晚餐后服用如果是六岁到18岁的孩子用来保健预防缺钙缺锌的话一天两次一次五毫升如果已经出现缺钙或缺锌的症状也是建议加大剂量一天两次一次10毫升早晚餐后服用如果想要补钙补锌效果更好建议是按疗程服用连续服用三个月如果是已经有明显钙锌缺乏的症状可以连续服用两个疗程哦"
    text2 = "0-12个月宝宝，服用葡萄糖酸钙锌口服溶液的正确方法.mp4"
    text3 = "你好我是阿诺健康助手不萄糖酸钙锌口服溶液怎么服用呢零到六个月的宝宝可以一天一次一次2.5毫升一只分两次服用喝奶后半小时不用如果担心宝宝太小不习惯喝的话也可以妈妈服用营养会通过乳汁输送给孩子六到12个月的宝宝也是一天一次不同的是这个年龄段的宝宝一次要喝五毫升和奶或者吃辅食后半小时服用葡萄糖酸钙锌口服溶液不同年龄段服用方法是不一样的不要吃错了哟"
    vectorizer = get_vectorizer(text1)

    similarity = calculate_similarity(vectorizer, text2, text3)
    print(similarity)
