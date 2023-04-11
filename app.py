from flask import Flask, render_template, request, session, redirect, jsonify
import json, os 
from datetime import date

app = Flask(__name__, static_folder='static')
app.secret_key = 'your-secret-key'

# Initialize empty book database
db_file = 'dblocal.json'
default_categories = ['Hospitality', 'Civil', 'Chemistry', 'Physics', 'Dictionaries', 'Mechanical', 'Fashion Design', 'Misc', 'Law', 'Ele&Electronics']
if not os.path.isfile(db_file):
    with open(db_file, 'w') as f:
        json.dump({cat: [] for cat in default_categories}, f)


def get_book_list(category):
    with open(db_file, 'r') as f:
        data = json.load(f)
    return data.get(category, [])


# Function to add a book to the database
def add_book(book_name, category):
    with open(db_file, 'r') as f:
        data = json.load(f)
    data[category].append(book_name)
    with open(db_file, 'w') as f:
        json.dump(data, f)

@app.route('/')
def index():
    # if 'username' not in session:
    #     return redirect('/signup')
    return render_template('index.html', date=date)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/signup')




@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # process form data
        return redirect('/')
    else:
        return render_template('signup.html', date=date)

@app.route('/list', methods=['GET', 'POST'])
def list_books():
    if request.method == 'POST':
        book_name = request.form['book_name']
        category = request.form['category']
        add_book(book_name, category)
    else:
        category = request.args.get('category', default_categories[1])
    book_list = get_book_list(category)
    return render_template('list.html', categories=default_categories, selected_category=category, book_list=book_list, date=date)


@app.route('/search', methods=['GET'])
def search_books():
    query = request.args.get('q', '').lower()
    with open(db_file, 'r') as f:
        data = json.load(f)
    results = []
    for category in data:
        for book in data[category]:
            if query in book.lower():
                results.append((book, category))
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)

