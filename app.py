from typing import Set, Dict, Tuple
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top_secret'

# Определение константных величин
RULE: Dict[Tuple[str, str], str] = {('H', 'a'): 'S',
                                    ('H', 'b'): 'SE',
                                    ('S', 'b'): 'SE',
                                    ('SE', 'a'): 'SE',
                                    ('SE', 'b'): 'SE'}
INITIAL_STATE: str = 'H'
FINAL_STATE: Set[str] = {'S', 'SE'}


def finite_automate(word: str) -> str:
    """Реализация конечного автомата для проверки символьных строк"""
    state: str = INITIAL_STATE
    for ind, char in enumerate(word):
        yield f'{word[ind:]} --> {state}'
        state = RULE.get((state, char))
        if not state:
            break

    if state in FINAL_STATE:
        yield 'Цепочка принадлежит языку'
    else:
        yield 'Цепочка не принадлежит языку'


@app.route('/', methods=['GET', 'POST'])
def index():
    res = None
    if request.method == 'POST':
        res = finite_automate(request.form['word'])
    return render_template('index.html', res=res)

