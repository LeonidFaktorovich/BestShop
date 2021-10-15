# Пишем свой веб-сервис:

from flask import Flask, request
import yaml

app = Flask(__name__)

with open('/Users/apple/PycharmProjects/BestShop/data/data.yml', 'r') as file:
    data = yaml.safe_load(file)


@app.route("/api/reserve", methods=['POST'])
def reserve():
    if not request.form.get('username'):
        return 'authorization error'
    if not request.form.get('item'):
        return 'item was not provided'
    data.append(request.form.get('username'))
    return 'new stats here'


@app.route("/api/stats", methods=['GET'])
def stats():
    # for name in data['users']:
    #     string = ('{} :\n\tДом первого уровня : {}\n\tДом второго уровня : {}\n\tДом третьего уровня : {}\n\t'
    #               'Дом четвертого уровня : {}\n\tДом пятого уровня : {}').format(name, name['1'], name['2'], name['3'],
    #                                                                              name['4'], name['5'])
    string = ''
    for name in data['users']:
        string += name
    return string


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8000', debug=True)
