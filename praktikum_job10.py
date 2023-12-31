# -*- coding: utf-8 -*-
"""Praktikum_Job10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kyJtbiOppTgAyd6Om39xbMkUOhBrc9oe
"""

import pandas as pd
from sklearn import svm

df = pd.read_csv('svm_mushrooms.csv')
df = df.drop(['class'],axis=1)
target = df['population']
s = set()
for val in target:
 s.add(val)
s = list(s)
rows = list(range(100,150))
df = df.drop(df.index[rows])

import matplotlib.pyplot as plt

x = df['gill-size']
y = df['gill-color']
gill_x = x[:50]
gill_y = y[:50]
versicolor_x = x[50:]
versicolor_y = y[50:]
plt.figure(figsize=(8,6))
plt.scatter(gill_x,gill_y,marker='+',color='green')
plt.scatter(versicolor_x,versicolor_y,marker='_',color='red')
plt.show()


import pandas as pd
raw_file = 'svm_mushrooms.csv'
raw_data = pd.read_csv(raw_file)
raw_data.head()
# kita encode raw data supaya berubah menjadi angka semua
encoded_data = pd.get_dummies(raw_data)
# kita lihat isi data kita yang sudah di-encode
encoded_data.head()
# atribut/feature adalah dari kolom ketiga sampai kolom terakhir
X = encoded_data.iloc[:, 3:]
# target/class adalah kolom pertama; kolom kedua kita abaikan saja, karena merupakan negasi dari kolom pertama
Y = encoded_data.iloc[:, 1]

from sklearn.model_selection import train_test_split
# kita akan gunakan 10% dari seluruh dataset sebagai data testing
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.10, random_state=1234)

from sklearn.svm import SVC
# kita inisiasi SVM classifier kita menggunakan kernel radial (RBF)
clf = SVC(kernel='linear', gamma=0.1)
# latih SVM!
clf.fit(X_train, y_train)
y_train_predicted = clf.predict(X_train)

from sklearn.metrics import accuracy_score
accuracy_score(y_train, y_train_predicted)
y_test_predicted = clf.predict(X_test)
accuracy_score(y_test, y_test_predicted)

from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test, y_test_predicted))
print(confusion_matrix(y_test, y_test_predicted))