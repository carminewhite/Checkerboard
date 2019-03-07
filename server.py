from flask import Flask, render_template
app = Flask(__name__)


@app.route('/<red_or_green>')
def chess_board(red_or_green):
    primary_color = red_or_green
    other_color = "#ffffe0"
    if primary_color == "red":
        other_color = "black"
    elif primary_color == "green":
        other_color = "#ffffe0"

    print("\n" + "*"*50+"\nIn the 'chess_board' function.  Color is:", red_or_green)
    return render_template('index.html', primary_color = primary_color, other_color = other_color)


if __name__=="__main__":
    app.run(debug=True)