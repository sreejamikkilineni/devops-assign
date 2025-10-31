from flask import Flask, render_template, request, redirect, session, url_for
import copy

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for session

# Initialize empty board
def init_board():
    return [['' for _ in range(3)] for _ in range(3)]

# Check for winner
def check_winner(board):
    # Rows, columns, diagonals
    lines = board + list(map(list, zip(*board)))  # rows and columns
    lines.append([board[i][i] for i in range(3)])  # main diagonal
    lines.append([board[i][2 - i] for i in range(3)])  # anti-diagonal

    for line in lines:
        if line[0] != '' and all(cell == line[0] for cell in line):
            return line[0]
    return None

# Check for draw
def check_draw(board):
    return all(cell != '' for row in board for cell in row)

@app.route('/')
def index():
    if 'board' not in session:
        session['board'] = init_board()
        session['turn'] = 'X'
        session['winner'] = None
        session['draw'] = False
    return render_template('index.html',
                           board=session['board'],
                           turn=session['turn'],
                           winner=session['winner'],
                           draw=session['draw'])

@app.route('/move/<int:row>/<int:col>')
def move(row, col):
    if 'board' not in session:
        return redirect(url_for('index'))

    board = session['board']
    turn = session['turn']
    winner = session.get('winner')
    draw = session.get('draw', False)

    if board[row][col] == '' and not winner:
        board[row][col] = turn
        winner = check_winner(board)
        draw = check_draw(board) if not winner else False
        session['winner'] = winner
        session['draw'] = draw
        session['turn'] = 'O' if turn == 'X' else 'X'
        session['board'] = board

    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
