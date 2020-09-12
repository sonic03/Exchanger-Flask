from flask import Flask,render_template,request
import requests
app=Flask(__name__)

api_key="b6bee4c8469e09673836ab8cf32befce"
url="http://data.fixer.io/api/latest?access_key="+api_key







@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        firstCurrency=request.form.get("firstCurrency")
        secondCurrency=request.form.get("secondCurrency")
        amo=request.form.get("amount")
        r=requests.get(url)
        app.logger.info(r)
        
        infos=r.json()
        app.logger.info(infos)

        firstValue=infos["rates"][firstCurrency]
        secValues=infos["rates"][secondCurrency]

        result=(secValues/firstValue)*float(amo)

        currentinfo={}
        currentinfo["firsCurrency"]=firstCurrency
        currentinfo["secondCurrency"]=secondCurrency
        currentinfo["amount"]=amo
        currentinfo["result"]=result

        return render_template("original.html",info = currentinfo)
        


    else:

        return render_template("original.html")

if __name__=="__main__":
    app.run(debug=True)