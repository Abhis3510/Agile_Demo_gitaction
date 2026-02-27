from flask import Flask, render_template, request
from sklearn import model_selection, linear_model
import numpy as np

app = Flask(__name__)

# --- Your ML Program Logic ---
X = [[4.0], [5.0], [6.0], [7.0], [8.0], [9.0], [10.0]]
y = [8, 10, 12, 14, 16, 18, 20]

# Train the model
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3, random_state=7)
reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)
accuracy = reg.score(X_test, y_test) * 100

@app.route('/')
def index():
    return render_template('index.html', accuracy=round(accuracy, 2))

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input from the form
        user_input = float(request.form['val'])
        # Predict using the model
        prediction = reg.predict([[user_input]])
        return render_template('index.html', 
                               accuracy=round(accuracy, 2), 
                               prediction=round(prediction[0], 2),
                               last_val=user_input)

if __name__ == '__main__':
    app.run(debug=True)