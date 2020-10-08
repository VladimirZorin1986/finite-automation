from typing import Set, Dict, Tuple

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
        print(f'{word[ind:]} --> {state}')
        state = RULE.get((state, char))
        if not state:
            break

    if state in FINAL_STATE:
        return 'Цепочка принадлежит языку'
    return 'Цепочка не принадлежит языку'


print(finite_automate(input('Введите слово алфавита:\n')))
