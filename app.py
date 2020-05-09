from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

role = "admin"

@app.route('/about/')
def about():
    return render_template('about.html', role = role)

@app.route('/divide/<int:x>/<int:y>/')
def divider(x, y):
    result = 0
    for i in range (x, y + 1):
        result += 1 / (x - i + 42)
    return str(result)

@app.route('/products/')
def render_products():
	return 'Продукты'

@app.route('/videos/<video_id>/')
def render_videos_item(video_id):
    return "Здесь будет видео " + video_id

@app.route('/book/<author>/<title>/')
def render_book(author,title):
    return "Здесь будет страница книги " + title + " автора " + author

@app.route('/book/<int:book_id>/')
def render_book_by_id(book_id):
    print(type(book_id))
    return ""

@app.errorhandler(404)
def render_not_found(error):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!", 404

@app.errorhandler(500)
def render_server_error(error):
    return "Что-то не так, но мы все починим", 500

@app.route("/example/")
def render_example():
    return "<h2>Привет, я функция Example </h2>"

app.run('0.0.0.0', 8000)