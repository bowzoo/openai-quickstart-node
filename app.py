import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = animal3(animal)
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


@app.route("/qa", methods=("GET", "POST"))
def qa():

    question = ""
    if request.method == "POST":
        question = request.form["question"]
        response = q_and_a(question)
        return redirect(url_for("qa",
                                result=response.choices[0].text,
                                question=question))

    result = request.args.get("result")
    question = request.args.get("question")
    return render_template("question.html", question=question, result=result)

def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )


def animal3(input):

    return openai.Completion.create(
           model="text-davinci-003",
           prompt=generate_prompt(input),
           temperature=0.6,
           )

def q_and_a(input):


    response = openai.Completion.create(
               model="text-davinci-003",
               prompt="%s" % input,
               temperature=0,
               max_tokens=160,
               #top_p=1,
               #frequency_penalty=0,
               #presence_penalty=0,
               )
    return response
