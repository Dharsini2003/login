from flask import Flask,render_template,request,redirect
from jsonutiles import *
app=Flask(__name__)


        

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        data=read()
        stud_data={
            "no":len(data["Students"])+1,
            "name":request.form["sname"],
            "age":request.form["sage"],
            "course":request.form["scourse"],
            "email":request.form["semail"]
        }
        data["Students"].append(stud_data)
        write(data)
        
    return redirect("/")

@app.route("/")

def index():
    data=read()
    return render_template("page.html",stud_data=data["Students"])

@app.route("/delete/<id>")
def delete(id):
    data=read()
    for stud in data["Students"]:
        if stud["no"]==int(id):
            data["Students"].remove(stud)
    
    sno=1
    for stud in data["Students"]:
        stud["no"]=sno
        sno+=1
    write(data)
    return redirect("/")

@app.route("/update/<id>", methods=["GET","POST"])
def update(id):
    data=read()
    for stud in data["Students"]:
        if stud["no"]==int(id):
            stud["name"]=request.form["sname"]
            stud["age"]=request.form["sage"]
            stud["course"]=request.form["scourse"]
            stud["email"]=request.form["semail"]
    write(data)
    return redirect("/")
            
if __name__=="__main__":
    app.run(debug=True)