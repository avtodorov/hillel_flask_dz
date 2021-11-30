from flask import Flask
import random
from faker import Faker
import csv
import requests

app = Flask(__name__)
fake = Faker()


@app.route('/')
def index():
    return '<b> index page </b>'


@app.route('/requirements')
def show_requirements():
    with open('requirements.txt') as file:
        contens = file.read()
        return contens


# random user and users
@app.route('/generate-users/')
def fake_user_generator():
    emails = ['gmail.com', 'mail.ru', 'meta.ua', 'i.ua', 'outlook.com', 'yahoo.com']
    result = fake.name().replace(" ", "") + '@' + emails[random.randint(0, 5)] + '</br>'
    return f'<h2> This is fake user generator </h2></br>' \
           f'Example of random user: {result} </br>' \
           f'To generate a list of random users pass a quantity(<b>qtt</b>) after /generate-users/<b>qtt</b>'


@app.route('/generate-users/<int:qtt>')
def fake_users_generator(qtt):
    emails = ['gmail.com', 'mail.ru', 'meta.ua', 'i.ua', 'outlook.com', 'yahoo.com']
    result = ''
    n = 1

    for names in range(qtt):
        name = fake.name().replace(" ", "")
        result += str(n) + ') ' + name + '@' + emails[random.randint(0, 5)] + '</br>'
        n += 1

    return f'<h3> List of "{qtt}" random users :</h3> </br>{result}'


# mean height and weight
@app.route('/mean')
def mean():
    with open('hw.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        height = 0
        weight = 0
        qtt = 0
        for row in reader:
            height += float(row[' Height(Inches)'])
            weight += float(row[' Weight(Pounds)'])
            qtt += 1

        mean_height = round(height / qtt, 2)
        mean_weight = round(weight / qtt, 2)

    return f'<h3> Mean height and weight from hw.csv file is: </h3></br>' \
           f'Mean height : <b>{mean_height}</b> (Inches) </br>' \
           f'Mean weight : <b>{mean_weight}</b> (Pounds)</br>' \
           f'Total selection is: {qtt}'


# astronauts in space
@app.route('/space')
def astronauts_in_space():
    r = requests.get('http://api.open-notify.org/astros.json')
    api_space = r.json()
    astronauts_in_space_names = api_space['people']
    astronauts_in_space_qtt = api_space['number']
    result = ''
    for astronaut in astronauts_in_space_names:
        result += astronaut['name'] + '</br>'
    return f'<h3> There is "{astronauts_in_space_qtt}" in space right now </h3></br>' \
           f'<b>Their names</b> : </br> {result}' \



if __name__ == '__main__':
    app.run()
