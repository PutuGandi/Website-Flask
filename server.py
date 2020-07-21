from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
print(__name__)

# @app.route('/index.html')
# def my_home():
#     return render_template('index.html')

# @app.route('/pricing.html')
# def wow_about():
#     return render_template('pricing.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

@app.route('/')
def html():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt',mode='a') as database:
        name = data['name']
        email = data['email']
        subject = data['subject']
        file = database.write(f'\n{name},{email},{subject}')

def write_to_csv(data):
    with open('database.csv',newline='',mode='a') as database2:
        name1 = data['name']
        email1 = data['email']
        subject1 = data['subject']
        messages1 = data['messages']
        csv_writer = csv.writer(database2, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name1,email1,subject1,messages1])


@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong. Try Again'
