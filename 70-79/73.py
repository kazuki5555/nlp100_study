# 73. 学習
# 72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．

import csv
import sys
from collections import Counter

import numpy as np

from stemming.porter2 import stem

stop_words = []

with open("tmp/stopword.tsv") as target:
    tsv = csv.reader(target, delimiter="\t")
    for t in tsv:
        for word in t:
            stop_words.append(word.lower())


def is_stopword(word: str) -> bool:
    return word.lower() in stop_words

def load_feature() -> dict:
    with open("tmp/features.txt", mode="r", encoding="utf8", errors="ignore") as feature:
        return {f.strip(): i for i, f in enumerate(feature, start=1)}

def create_train_data(sentiments: list, feature_dict: dict) -> list:
    train_x = np.zeros([len(sentiments), len(feature_dict) + 1], dtype=np.float64)
    train_y = np.zeros(len(sentiments), dtype=np.float64)

    for i, sentiment in enumerate(sentiments):
        train_x[i] = extract_feature(sentiment[3:], feature_dict)
        
        if sentiment[0:2] == "+1":
            train_y[i] = 1

    return train_x, train_y

def extract_feature(data: str, feature_dict: dict) -> list:
    train_x = np.zeros(len(feature_dict) + 1, dtype=np.float64)
    train_x[0] = 1

    for word in data.split(' '):
        word = word.strip()
        
        if is_stopword(word):
            continue

        word = stem(word)

        try:
            train_x[feature_dict[word]] = 1
        except:
            pass

    return train_x


feature_dict = load_feature()

with open("tmp/sentiment.txt", mode="r", encoding="utf8", errors="ignore") as sentiment:
    x_train, y_train = create_train_data(list(sentiment), feature_dict)
    print(len(x_train), len(y_train))