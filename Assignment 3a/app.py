from flask import Flask, render_template

app = Flask(__name__)

#creating and styling homepage using flask render_template homepage and styles2
@app.route('/')
def home_page():
    return render_template('homepage.html')

#creating and styling contact page using flask render_template contact and styles3

@app.route('/contactus')
def contact_page():
    return render_template('contact.html')
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
