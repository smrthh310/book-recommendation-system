from flask import Flask, render_template, redirect
import warnings
from model import Book_Recommender
warnings.filterwarnings('ignore')


Recommender = Book_Recommender()

app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/demo/trends")
def demoTrends():
    a = Recommender.trending_books()
    return render_template("demotrends.html", recommended=a)

@app.route("/demo/personalized")
def demoPersonalizedDefault():
    users = Recommender.getUsers()
    read = False    
    recommended_nmf = False    
    recommended_svd = False    
    return render_template("demopersonalized.html", read = read, svd=recommended_svd, nmf=recommended_nmf, users=users, userid = False)

@app.route("/demo/personalized/<int:userid>")
def demoPersonalized(userid):
    users = Recommender.getUsers()
    read = Recommender.read_history(userid)    
    recommended_nmf = Recommender.nmf(userid, 10)    
    recommended_svd = Recommender.svd(userid, 10)    
    return render_template("demopersonalized.html", read = read, svd=recommended_svd, nmf=recommended_nmf, users = users, userid = userid)


@app.route("/demo/personalized/updateUser")
def demoPersonalizedUpdateUser():
    Recommender.setUsers()
    return redirect("/demo/personalized")


@app.route("/methods")
def methods():
    return render_template("methods.html")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('default.html', path=path)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
