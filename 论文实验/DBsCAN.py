from sklearn import datasets
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import time
import copy
import datetime
from sklearn.metrics import accuracy_score
def find_neighbor(j, x, eps):
    N = list()
    for i in range(x.shape[0]):
        temp = np.sqrt(np.sum(np.square(x[j] - x[i])))  # 计算欧式距离
        if temp <= eps:
            N.append(i)

    return set(N)


def DBSCAN(X, eps, min_Pts):
    k = -1
    neighbor_list = []  # 用来保存每个数据的邻域
    omega_list = []  # 核心对象集合
    gama = set([x for x in range(len(X))])  # 初始时将所有点标记为未访问
    cluster = [-1 for _ in range(len(X))]  # 聚类


    for i in range(len(X)):
        neighbor_list.append(find_neighbor(i, X, eps))


        if len(neighbor_list[-1]) >= min_Pts:
            omega_list.append(i)  # 将样本加入核心对象集合
    omega_list = set(omega_list)  # 转化为集合便于操作

    while len(omega_list) > 0:
        gama_old = copy.deepcopy(gama)
        j = random.choice(list(omega_list))  # 随机选取一个核心对象
        k = k + 1
        Q = list()
        Q.append(j)
        gama.remove(j)
        while len(Q) > 0:
            q = Q[0]
            Q.remove(q)


            if len(neighbor_list[q]) >= min_Pts:
                delta = neighbor_list[q] & gama

                deltalist = list(delta)
                for i in range(len(delta)):
                    Q.append(deltalist[i])
                    gama = gama - delta
        Ck = gama_old - gama
        Cklist = list(Ck)


        for i in range(len(Ck)):
            cluster[Cklist[i]] = k
        omega_list = omega_list - Ck

    return cluster

def presion(y_true, y_pred):

    class_label=list(set(y_true))

    #将相同下标的元素发在一起。
    label_index=[]
    for i in class_label:
        c=[]
        for j in range(len(y_true)):
            if y_true[j]==i:
                c.append(j)
        label_index.append(c)

    # 查看是否正确分类
    y_ture_lable=list(range(len(y_true)))
    for i in label_index:
        pred_label=[]
        for j in i:
            if y_pred[j]==-1:
                continue
            pred_label.append(y_pred[j])


        if len(pred_label)==0:
            max_label=len(class_label)+100
        else:
            max_label = max(pred_label, key=pred_label.count)
        for s in i:
            y_ture_lable[s]=max_label


    acc=accuracy_score(y_ture_lable,y_pred)
    return acc

if __name__ == '__main__':
    # # 获取D31数据集
    # D31=pd.read_table("D31.txt", header=None)
    # data=(D31[[0,1]]).values
    # target=(D31[2]).values
    # eps = 0.8
    # min_Pts = 30

    # # 获取house数据集
    # house=pd.read_csv("houser_processed_15000.csv")
    # data=(house).values
    # print(data)
    #
    # eps =10
    # min_Pts = 20

    # # 获取3D8M数据集
    # D8M = pd.read_csv("data/3D0.4M.CSV")
    # data = (D8M).values
    #
    # eps = 0.01
    # min_Pts = 5
    # # 获取HIGGS数据集
    # HIGGS = pd.read_csv("data/HIGGS1800.csv")
    #
    # target = HIGGS['0'].values
    #
    # HIGGS = HIGGS.drop(['0'], axis=1)
    # data = (HIGGS).values
    House = pd.read_csv("data/houser_processed_18000.csv")
    data = (House).values

    # eps = 0.1
    min_Pts = 20
    eps_list = [10, 15, 20, 25, 30]
    # eps = 0.1

    for eps in eps_list:
        print(eps)
        # 原始DBSCAN
        begin = datetime.datetime.now()
        C = DBSCAN(data, eps, min_Pts)
        end = datetime.datetime.now()
        # 得到时间
        totalTime = (end - begin).total_seconds()
        print(set(C))
        print("原始Dbscan")
        print(totalTime)

        print("end")
        print('--------------------------------')


