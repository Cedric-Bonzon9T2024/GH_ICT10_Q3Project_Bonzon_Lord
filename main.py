from python import display
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    status = ""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            message = "All fields are required."
            status = "error"
        elif len(password) < 6:
            message = "Password must be at least 6 characters."
            status = "error"
        else:
            message = "Account created successfully!"
            status = "success"

    return render_template("index.html", message=message, status=status)