from flask import Flask, render_template
from datetime import datetime
import random
import requests
app = Flask(__name__)

year = datetime.now().year


@app.route('/')
def home():
    return render_template('index.html', year=year)


@app.route('/guess/<name>')
def guessname(name):

    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template('hello.html', person_name=name, gender=gender, age=age)


@app.route('/hello')
def hello():
    random_number = random.randint(1, 10)
    return render_template('hello.html', year=year, num=random_number)


@app.route('/blog/<int:index>')
def get_blog(index):
    #print(index)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    blog_post = response.json()
    return render_template('blog.html', post=blog_post,numm=index)


if __name__ == "__main__":
    app.run()

""" <!--  <h1>Hey {{person_name.title()}}</h1>-->
<!--  <h2>I think you are {{gender}}</h2>-->
<!--  <h3>And may be {{age}} years old</h3>-->
   
  {% if blog_post["id"] == numm: %}
  {% endif %}
"""
