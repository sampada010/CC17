from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Greet Me App</title>
</head>
<body>
    <h2>Welcome to the Greet Me App!</h2>
    <form method="POST">
        <label for="name">Enter your name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        <input type="submit" value="Greet Me">
    </form>
    {% if name %}
        <h3>Hello, {{ name }}! 😊</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def greet():
    name = None
    if request.method == "POST":
        name = request.form.get("name")
    return render_template_string(html, name=name)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
