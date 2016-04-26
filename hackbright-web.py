from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    return render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)
    
@app.route("/student-search")
def get_student_form():
    """Show information form for searching for a student"""

    return render_template("student_search.html")



if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
