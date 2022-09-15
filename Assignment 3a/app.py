from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('homepage.html')

@app.route('/contactus')
def contact_page():
    return render_template('contact.html')
    # import to note that it is going to look for the .html files in a folder called templates

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
