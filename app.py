from flask import Flask,render_template,request

app = Flask(__name__)

student = {
    "name":"Leul",
    "role":"Python Developer",
    "bio":"I am a high school student and a python developer interested in learning python ,AI/ML and other tech related things.I alos like to learn and understand how the technologies around us work.",
    "skill":["Python","flask","tkinter","git","HTML/CSS","Bootstrap"],
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
            "github":"https://github.com/Leul-Eyasu/Personal_Portfolio_flask"
        }
    ],
    "learning":[
        "Web applications",
        "Flask applications",
        "CRUD applications",
        "APIs and Live data",
        "Data bases",
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

@app.route("/contact/submit",methods=["POST"])
def submit():
    #stores the submited form in the txt file
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        with open('messages/messages.txt','a') as file:
            file.write(f"Name:{name} sent message:{message}\n")
        return render_template("submit.html",student=student)
    return "Method not allowed."


@app.route("/learning")
def learning():
    return render_template("learning.html",student=student)

if __name__ == "__main__":
    app.run()