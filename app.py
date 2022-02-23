from flask import Flask, render_template
app = Flask (__name__)

@app.route("/")
def home():
    return render_template("Index.html")

@app.route("/login")
def login():
    return "Return login"

# @app.route("/register")
# def register():
#     return render_template("Index.html")
@app.route('/register', methods = ["get", "post"])
def register():
    if request.method == "post":
        print(request.form)
        fullName = request.form.get("fullName")
        emailAdd = request.form.get("emailAdd")
        password = request.form.get("password")

        print(fullName + "" + emailAdd + "" + password)

        return render_template( "Index.html", fullName=fullName, emailAdd=emailAdd, password=password)
if __name__ == "__main__":
    app.run(debug=True)


