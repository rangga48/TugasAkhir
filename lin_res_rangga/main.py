from flask import jsonify, request, Flask
import json
import logging
from jwcrypto import jwt,jwk, jws
key = jwk.JWK(generate='oct', size=256)
key.export()
app = Flask(__name__)
import pandas as pd
from sklearn import linear_model 
import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split

from numpy import genfromtxt
import pandas as pd
my_data = pd.read_csv('Nilai_Convert_4.csv', delimiter=';')
print("Table Data")
print(my_data)
x1 = my_data['x1'].replace({',': '.'}, regex=True)
x2 = my_data['x2'].replace({',': '.'}, regex=True)
a = 0
x1 = [int(float(x)) for x in x1]
x2 = [int(float(x)) for x in x2]
#print(pd.DataFrame(x1).values.tolist())
#x1 = x1[~np.isnan(x1)]
#x2 = x2[~np.isnan(x2)]
y = my_data['y'].replace({',': '.'}, regex=True)

dataset = np.vstack((x1,x2)).T
training_X,x_test,training_y,y_test=train_test_split(dataset,y,test_size=0.2,random_state=1)
clf = svm.SVC(kernel='linear', C=1.0)
clf.fit(training_X, training_y)
print(clf.predict([[89,89]]))

df = pd.read_csv('Nilai_Convert_4.csv', delimiter=";")
features = ['x1','x2']
for x in features:
    df[x] = pd.to_numeric(df[x].replace({',':'.'},regex=True), downcast="float")
x = df[features]
y = df['y']
regr = linear_model.LinearRegression()
regr.fit(x,y)

@app.route('/get-nilai', methods=["POST"])
def validate():
    # print("AVA")
    data = json.loads(request.data)

    result = {
        "hasil":list(regr.predict([[(int(data['harian'])+int(data['uts'])+int(data['uas']))/3,int(data['keterampilan'])]]))[0]
    }
    
    return jsonify(result), 200

@app.route('/get-nilai-svm', methods=["POST"])
def validate_svm():
    
    data = json.loads(request.data)
    print([[int(float(data['pengetahuan'])),int(float(data['keterampilan']))]])
    print(list(clf.predict([[int(float(data['pengetahuan'])),int(float(data['keterampilan']))]]))[0])
    result = {
        "hasil":str(list(clf.predict([[int(float(data['pengetahuan'])),int(float(data['keterampilan']))]]))[0]),
        "coef":clf.coef_[0].tolist(),
        "intercept":clf.intercept_[0],
        "support_vector":clf.support_vectors_.tolist()
    }
    
    return jsonify(result), 200