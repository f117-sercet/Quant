import numpy as np
import pandas as pd
import math


#词频
def computedTf(wordDict, bow):
    tfDict = {}
    nbowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count / nbowCount
    return tfDict


def computeIDF(wordDictList, bow):
    idfDict = dict.fromkeys(wordDictList[0], 0)
    N = len(wordDictList)
    for wordDict in wordDictList:
        # 遍历字典中的每个词汇
        for word, count in wordDict:
            if count > 1:
                idfDict[word] = +1
    for word, ni in idfDict.items():
        idfDict[word] = math.log((N + 1 / ni + 1))
    return idfDict


def computeTFIDF(tf, idfs):
    tfidf = {}
    for word, tfval in tf.items():
        tfidf[word] = tfval * idfs[word]
    return tfidf


if __name__ == '__main__':
    docA = "The cat sat on my bad"
    docB = "The dog sat on my knees"

    bowA = docA.split(" ")
    bowB = docB.split(" ")

    # 构件词库
    wordSet = set(bowA).union(set(bowB))
    wordDictA = dict.fromkeys(wordSet, 0)
    wordDictB = dict.fromkeys(wordSet, 0)
    for word in bowA:
        wordDictA[word] += 1

    for word in bowB:
        wordDictB[word] += 1

    data_df = pd.DataFrame([wordDictA, wordDictB])

    # 计算TF
    tfA = computedTf(wordDictA, bowA)
    tfB = computedTf(wordDictA, bowB)
    idfs = computeIDF(wordDictA, wordDictB)
    tfidfA=computeTFIDF(tfA,idfs)
    tfidfB = computeTFIDF(tfB, idfs)
