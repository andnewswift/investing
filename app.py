import flask
import pandas as pd
from joblib import dump, load


with open(f'housepriceprediction.joblib', 'rb') as f:
    model = load(f)


app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return (flask.render_template('index.html'))

    if flask.request.method == 'POST':
        rooms = flask.request.form['rooms']
        bathroom = flask.request.form['bathroom']
        distance = flask.request.form['distance']
        car = flask.request.form['car']

        input_variables = pd.DataFrame([[rooms, bathroom, distance, car]],
                                       columns=['rooms', 'bathroom',
                                                'distance', 'car'],
                                       dtype='float',
                                       index=['input'])

        predictions = model.predict(input_variables)[0]
        print(predictions)

        return flask.render_template('index.html', original_input={'Rooms': rooms, 'Bathroom': bathroom, 'Distance': distance, 'Car': car}, result=predictions)


if __name__ == '__main__':
    app.run(debug=True)