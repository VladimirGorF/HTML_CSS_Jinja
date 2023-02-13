# file = open('file.txt', 'r', encoding='utf-8')
# list_1 = list()
# resultData = list()
# for line in file.readlines():
#     resultData.append(tuple(line.split('\n')[0].split(';')))
#
# file.close()
# print(resultData)

from flask import Flask, render_template
from random import randint as rd

app = Flask(__name__)


@app.route('/')
def main():
    with open('file.txt', 'r', encoding='utf-8') as file:
        resultData = list()
        for line in file.readlines():
            resultData.append(tuple(line.split('\n')[0].split(';')))
    return render_template('base.html', data=resultData)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
