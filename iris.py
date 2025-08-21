# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 10:24:10 2025

@author: user
"""

# 1- Kütüphaneler
import matplotlib.pyplot as plt          # çizimler/grafikler için
from mpl_toolkits.mplot3d import Axes3D  # 3B çizim için
from sklearn import datasets             # iris veri setini kolayca yüklemek için
from sklearn.decomposition import PCA    # PCA ile boyut indirgeme

# 2- Iris veri setini yükle
iris = datasets.load_iris()      # iris veri seti hazır geliyor
X = iris.data                    # bagimsiz degiskenler / özellikler
y = iris.target                  # bagimli degisken / sınıf etiketleri
target_names = iris.target_names # sinif isimleri (setosa, versicolor, virginica)

# 3- 2B scatter plot
fig, ax = plt.subplots()  # yeni çizim alani olustur
scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap='Set1')  
ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])  # eksen isimleri
# legend ekle: renkler hangi sinifa ait goster
ax.legend(scatter.legend_elements()[0], target_names, loc='lower right', title='Türler')
plt.show()  # grafigi göster

# 4- PCA ile 3B scatter plot
# PCA: verinin en yuksek varyans gosterdigi dogrularla indirger
X_reduced = PCA(n_components=3).fit_transform(X)  # 4 özelliği 3 bileşene indir

fig = plt.figure(figsize=(8, 6))  # yeni 3B çizim alani
ax = fig.add_subplot(111, projection='3d', elev=-150, azim=110)  # 3B eksen ekle, aci ayarla

# 3B scatter plot
ax.scatter(
    X_reduced[:, 0],  # 1. bilesen (PC1)
    X_reduced[:, 1],  # 2. bilesen (PC2)
    X_reduced[:, 2],  # 3. bilesen (PC3)
    s=40,             # nokta boyutu
)

# eksen ve baslik ayarlari
ax.set_title("İris veri seti — İlk 3 PCA bileşeni")
ax.set_xlabel("1. bileşen (PC1)")
ax.xaxis.set_ticklabels([]) 
ax.set_ylabel("2. bileşen (PC2)")
ax.yaxis.set_ticklabels([])  
ax.set_zlabel("3. bileşen (PC3)")
ax.zaxis.set_ticklabels([]) 

plt.show()  