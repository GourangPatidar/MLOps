from flask import Flask  , render_template , request


app=Flask(__name__)

@app.route('/home' )
def index():
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return name
    return render_template('form.html')



@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        return f"Name: {name}, Age: {age}"
    
@app.route('/success/<score>')
def success(score):
    return render_template('results.html'  , results=int(score))
    


if __name__=="__main__":
    app.run(debug=True)