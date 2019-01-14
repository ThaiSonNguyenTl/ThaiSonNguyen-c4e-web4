from flask import Flask,render_template,request,session,redirect
from models.character import Character
from models.user import User
import mlab
mlab.connect()
app = Flask(__name__)
app.config["SECRET_KEY"] ="very secret"
#LIST(MASTER)
# lay het ra thi viet Character.Objects()
@app.route('/characters') #route nay de hien thi tat ca cac nhan vat
def characters():
    if "token" in session:
        #1 lay het database
        character_list = Character.objects()
        #2 render: template + data
        return render_template("characters.html", character_list = character_list)
    else:
        return redirect("/login?next=/characters")
@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "GET":
       return render_template("login_form.html")
    elif request.method == "POST":
        form = request.form 
        username = form["username"]
        password = form["password"]

    found_user = User.objects(username=username).first() #cho nos chi tra ve 1 phan tu
    if found_user is None:
        return "User not found"
    elif found_user.password != password:
        return "Invaild password"
    else:
        session["token"] = username
        next = request.args.get("next")
        if next is None or next == "":
            return "login succesfully"
        else:
            return redirect(next)

    # if username == "admin" and password == "admin":
    #     session["token"] = "admin"   #thuong dung la username???
    #     return "login succesfully"
    # else:
    #     return "Failed to login"

@app.route("/posts")
def posts():
    if "token" not in session:
        return redirect("/login?next=/posts")
    else:
        username = session["token"]



@app.route("/logout")
def logout():
    del session["token"]
    return redirect("/login")

@app.route('/character/<given_id>')
def character_detail(given_id):
    
    #lay one
    #1 get one character dua vao id
    # character = Character.objects(id =given_id).first()  #rate__gte =3 (lon hon hoac bang)
    character = Character.object().with_id(given_id)
    #render :template+data
    if character is None:
        return "Not found"
    else:
        return render_template("character_detail.html",character=character)
    

@app.route('/add_character', methods = ['GET','POST'])
def add_character():
    
#1 GUI FORM (GET)
   if request.method == "GET":   #method ko dc co s 
       return render_template("character_form.html")
   elif request.method == "POST":
#4 NHAN FORM => LUU (POST)
       form = request.form
       name = form["name"]
       image = form["image"]
       rate = form["rate"]
       new_character = Character(name = name,image = image,rate = rate )
       new_character.save()
       return "Gotcha"




if __name__ == '__main__':
  app.run(debug=True)