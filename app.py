from flask import Flask,render_template

app = Flask(__name__)

student = {
    "name":"Leul",
    "age":18,
    "role":"Python Developer",
    "bio":"I am a high school student interested in learning python and other tech related thinhgs.",
    "skill":["python","html","css"],
    "email":"leulleul334@gamil.com",
    "github":"https://github.com/Leul-Eyasu",
    "projects":[
        {
            "title":"Smart library Managment system",
            "description":"A console and GUI app that organize and accses book and store it in json file. ",
            "tech":["pytyon","OOP","json","tkinter"],
            "github":"https://github.com/Leul-Eyasu/Smart_Library_System"
        }
    ]
}

@app.route("/")
def home():
    return render_template("index.html",student=student)

@app.route("/projects")
def projects():
    return render_template("projects.html",student=student)

@app.route("/contact")
def contact():
    return render_template("contact.html",student=student)



if __name__ == "__main__":
    app.run(debug=True)