from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


student_data = []

@app.route("/")
def home():
    return render_template("home.html", student_data=student_data)



@app.route("/submit", methods=['POST', 'GET'])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        family_name = request.form["family_name"]
        email = request.form["email"]
        major_subjects = request.form["major_subjects"]
        time_slot = request.form["time_slot"]
         
        if not name or not email or not family_name or not major_subjects:
            return render_template("home.html", student_data=student_data)
         
        student_data.append({"name" : name, "email" : email, "family_name" : family_name, "major_subjects" : major_subjects, "time_slot" : time_slot})
         
    return render_template("home.html", student_data=student_data)



@app.route("/already_booked")
def view_data():
    return render_template("time_slot.html", student_data=student_data)


if __name__ == "__main__":
    app.run(debug=True)