from flask import Flask
from services.streak_service import StreakService
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__)

@app.route("/")
def home():
    streaks = StreakService.get_all_streaks()

    total_days = sum(int
        (streak.days)
        for streak in streaks
        )
    
    return render_template(
        "home.html",
        streaks=streaks,
        total_days=total_days
    )

@app.route("/add", methods=["GET","POST"])
def add_skill():
    if request.method == "POST":
        skill = request.form["skill"]
        StreakService.add_streak(skill)

        return redirect("/")
    return render_template("add.html")
    
@app.route("/increase/<skill>")
def increase(skill):
    StreakService.increase_streak(skill)

    return redirect("/")

if __name__  == "__main__":
    app.run(debug=True)



