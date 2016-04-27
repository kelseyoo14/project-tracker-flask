from flask import Flask, Markup, flash, request, render_template

import hackbright

app = Flask(__name__)
app.secret_key = "fngnoirsgjgjpg"


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

@app.route("/student-add")
def student_add():
    '''Adds a student'''
    return render_template("student_add.html")


@app.route("/student-add", methods=['POST'])
def student_create():
    '''Creates a student'''
    # reminder to use request.form to get POST args
    first = request.form.get('first')
    last = request.form.get('last')
    github = request.form.get('github')

    # call the existing backend function to talk to the db
    hackbright.make_new_student(first, last, github)

    # flash confirmation

    text = "Student <a href='student?github={}'>{} {}</a> added!".format(github,first,last)
    flash(Markup(text))

    return render_template("student_add.html")



if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
