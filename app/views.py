from flask import render_template, request
from app import app
from outputForWeb import getUserTime


pocetHodin = "8"
pocetDni = "1"
# worklogAuthors = ["62f9fcb31e82e839c24f4417", "61a73fa8c75da80072f8fb5e"]


@app.route("/", methods=['GET', 'POST'])

def answer():
    if request.method == 'POST':
        form_data = request.form
        form_data_str = str(form_data["form_1"])
        
        UserOutput = getUserTime(form_data_str)
        return render_template("table.html", pocetHodin=UserOutput[0], pocetDni=UserOutput[1], allIDs = UserOutput[2])
    else:
        return render_template("table.html")


