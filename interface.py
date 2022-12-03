from flask import Flask,jsonify,request,render_template 
from p_data.utils import Iris
import config
import numpy as np
app=Flask(__name__)

@app.route("/")
def hello_flask():
    return render_template("index.html")


@app.route("/new",methods=["POST"])
def get_result():
    data=request.form
    print("data:",data)
    sepal_length=eval(data["sepal_length"])
    sepal_width=eval(data["sepal_width"])
    petal_length=eval(data["petal_length"])
    petal_width=eval(data["petal_width"])
    a_class =Iris(sepal_length,sepal_width,petal_length,petal_width)
    pred_class=a_class.get_predicted_class()
        

    return render_template('after.html', data=pred_class)
    #return jsonify({"result":f'predicted classes are :{pred_class}'})


if __name__=="__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8080)

    

