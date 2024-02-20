from flask import Flask,request, url_for, redirect, render_template,jsonify
import pickle
import numpy as np
import pandas as pd

val=pd.read_csv("epics_dataset.csv")

app = Flask(__name__)

model=pickle.load(open('multi_output_model.pkl','rb'))

# final=[val[val["field no"]=="D-1"].to_numpy()[0][1:4]]
# prediction=model.predict(final)
# print(prediction)
@app.route('/')
def hello_world():
    return render_template("epics.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    data = request.get_json()
    parameter = data.get('parameter')
    final=[val[val["field no"]==parameter].to_numpy()[0][1:4]]
    prediction=model.predict(final)
    result="Urea-యూరియా : {0} కి/ఎక <br> potash-పొటాష్ : {1} కి/ఎక<br> SingleSuperPhosphate-సింగిల్ సూపర్ ఫాస్ఫేట్ : {2} కి/ఎక<br>".format(round(prediction[0][0],2),round(prediction[0][1],2),prediction[0][2])
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)
