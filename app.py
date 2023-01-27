from flask import Flask,request,render_template
import pickle
app=Flask(__name__,template_folder='Template')
filename="model9.pkl"
fileobj=open(filename,'rb')
b= pickle.load(fileobj)
@app.route('/')
def kaise():
    return render_template('motor1.html')

@app.route('/end')
def sanket():
    return render_template('motor.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        kms_driven=float(request.form['kms_driven'])
        year=float(request.form['age'])
        age=2023-year
        power=float(request.form['power'])
        owner=request.form['owner']
        if (owner=='Second_Owner'):
            Second_Owner=1
            First_Owner=0
        else:
            Second_Owner=0
            First_Owner=1
        

        prediction=b.predict([[kms_driven,age,power,Second_Owner]])
        
        return render_template("motor.html",prediction_text="Total Motor Bike Price is Rs {} ".format(int(prediction)))

    else:
        return render_template('motor.html')

if __name__=='__main__':
    app.run(debug=True,port=8)