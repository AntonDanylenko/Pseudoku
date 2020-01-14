# Anton Danylenko, Ian Searfoss

from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

from python import sudoku_generator as sudoku



@app.route("/")
def main():
    board = sudoku.strBoard(sudoku.generatePuzzle(30))
    return render_template("index.html", puzzle=board)




if __name__ == "__main__":
    app.run(debug=True)
