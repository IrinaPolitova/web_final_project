# Это программа, где будет натренирована модель, генерирующая строчки

import pandas as pd
import markovify
from random import choice

all_lines = []

f = pd.read_csv('french_poems.csv', encoding='utf-8')

for poem in f['poem']:
    new = poem.split('\n')
    for s in new:
        all_lines.append(s)


shuffled = f.sample(frac=1)
train = ' '.join(shuffled.poem)


m = markovify.Text(train)


def sent(value):
    if value == 'real':
        line = choice(all_lines)
        if line.endswith(',') or line.endswith('.'):
            line = line[:-1]
        
        return line

    if value == 'create':
        i = m.make_short_sentence(max_chars=50)
        if i is None:
            while i is None:
                i = m.make_short_sentence(max_chars=50)

        if i.endswith('.'):
            i = i[:-1]

        return i
