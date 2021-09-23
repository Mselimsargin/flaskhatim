from flask import Flask,render_template,url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/afaru/OneDrive/Masaüstü/hatim2/hatim.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add",methods=["POST","GET"])
def add():
    if request.method=='POST':
        service1=request.form['service1']
        service=request.form['service']
        service3=request.form['service3']
        service4=request.form['service4']
        new = users(mintika=service1,kurum=service,hatim=service3,adet=service4)
        db.session.add(new)
        db.session.commit()
        
    return redirect(url_for("index"))   



class users(db.Model):
    _id= db.Column("id",db.Integer,primary_key=True)
    mintika = db.Column(db.String(80), unique=True, nullable=False)
    kurum = db.Column(db.String(120), unique=True, nullable=False)
    hatim = db.Column(db.String(120), unique=True, nullable=False)
    adet = db.Column(db.Integer, nullable=False)

    def __init__(self,mintika,kurum,hatim,adet):
        self.mintika=mintika
        self.kurum=kurum
        self.hatim=hatim
        self.adet=adet



if __name__=="__main__":
    db.create_all()
    app.run(debug=True)  

    
  


  