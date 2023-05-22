from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

model = pickle.load(open("wine.pkl","rb"))

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/wine" , methods = ["GET","POST"])
def wine():
    volatile_acidity = float(request.form.get("volatile acidity"))
    citric_acid = float(request.form.get("citric acid"))
    residual_sugar = float(request.form.get("residual sugar"))
    chlorides = float(request.form.get("volatile acidity"))
    free_sulfur_dioxide = float(request.form.get("free sulfur dioxide"))
    total_sulfur_dioxide = float(request.form.get("total sulfur dioxide"))
    density = float(request.form.get("density"))
    pH = float(request.form.get("pH"))
    sulphates = float(request.form.get("sulphates"))
    alcohol = float(request.form.get("alcohol"))
    citric_mean = float(request.form.get("citric_mean"))
    residual_mean = float(request.form.get("residual_mean"))
    chloride_mean = float(request.form.get("chloride_mean"))
    free_mean = float(request.form.get("free_mean"))
    total_mean = float(request.form.get("total_mean"))

    result = model.predict[[volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol,citric_mean,residual_mean,chloride_mean,free_mean,total_mean]]
    
    outcome = result[0]
    if outcome == 3:
        return "three"
    elif outcome == 4:
        return "four"
    elif outcome == 5:
        return "five"
    else:
        return "Good"

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)

