from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<red>')
def red_black_board(red):
    print("\n" + "*"*50+"\nIn the 'redblack' function")
    return render_template('index.html', color = red)

if __name__=="__main__":
    app.run(debug=True)