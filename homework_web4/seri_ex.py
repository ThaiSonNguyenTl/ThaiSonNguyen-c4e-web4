from flask import Flask,render_template,request
from models.bike import Bike
import mlab
mlab.connect()
app = Flask(__name__)

@app.route('/new_bike', methods = ["GET","POST"])
def new_bike():
    form = request.form
    if request.method == "GET":
        return render_template("bike.html")
    elif request.method == "POST":
        model = form["model"]
        daily_fee = form["daily_fee"]
        image = form["image"]
        year = form["year"]
        add_new_bike = Bike(model = model,
                            daily_fee = daily_fee,
                            image = image,
                            year = year)
        add_new_bike.save()
        return "Save successfully"

if __name__ == '__main__':
  app.run(debug=True)