from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

student = {
    "name":"Leul",
    "age":18,
    "role":"Python Developer",
    "bio":"I am a high school student interested in learning python and other tech related thinhgs.",
    "skill":["python","flask","tkinter","git","github"],
    "email":"leulleul334@gamil.com",
    "github":"https://github.com/Leul-Eyasu",
    "projects":[
        {
            "title":"Smart library Managment system",
            "description":"A console and GUI app that organize, accses and store books saving it in json file. ",
            "tech":["Python","OOP","json","tkinter"],
            "github":"https://github.com/Leul-Eyasu/Smart_Library_System"
        },
        {
            "title":"Personal Portfolio",
            "description":"A Simple personal Portfolio made using the Python Library flask and some HTML and bootstarp for styling it.",
            "tech":["Python","Flask","HTML","Bootstrap"],
            "github":"https://github.com/Leul-Eyasu/Smart_Library_System"
        }
    ],
    "learning":[
        "Web applications",
        "Flask applications",
        "CRUD applications",
        "APIs and Live data",
        "Data bases"
        "Prompt Engineering"
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

@app.route("/learning")
def learning():
    return render_template("learning.html",student=student)

if __name__ == "__main__":
    app.run(debug=True)