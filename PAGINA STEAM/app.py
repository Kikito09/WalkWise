from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/problem')
def problem():
    return render_template('problem.html')

@app.route('/solution')
def solution():
    return render_template('solution.html')

@app.route('/how-it-works')
def how_it_works():
    return render_template('how-it-works.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/comparison')
def comparison():
    return render_template('comparison.html')

@app.route('/impact')
def impact():
    return render_template('impact.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)