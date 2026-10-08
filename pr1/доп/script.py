import math

ALPHABET = ['0', '1', '2']

def name(t):
    return "q" + "".join(t)

def shift(t, x):
    return t[1:] + (x,)

states = []
for b1 in ALPHABET:
    for b2 in ALPHABET:
        for b3 in ALPHABET:
            for b4 in ALPHABET:
                t = (b1, b2, b3, b4)
                is_init = (t == ('0', '0', '0', '0'))
                is_final = (b1 == '2')
                states.append((name(t), t, is_init, is_final))

name_to_id = {n: i for i, (n, _, _, _) in enumerate(states)}

transitions = []
for n, t, _, _ in states:
    for sym in ALPHABET:
        nt = shift(t, sym)
        transitions.append((n, name(nt), sym))

positions = {}
for i, (n, _, _, _) in enumerate(states):
    angle = 2 * math.pi * i / len(states)
    positions[n] = (500 + 400 * math.cos(angle), 500 + 400 * math.sin(angle))

lines = []
lines.append('<?xml version="1.0" encoding="UTF-8" standalone="no"?>')
lines.append('<structure>')
lines.append('    <type>fa</type>')
lines.append('    <automaton>')

for i, (n, _, is_init, is_final) in enumerate(states):
    x, y = positions[n]
    lines.append(f'        <state id="{i}" name="{n}">')
    lines.append(f'            <x>{int(x)}</x><y>{int(y)}</y>')
    if is_init:
        lines.append('            <initial/>')
    if is_final:
        lines.append('            <final/>')
    lines.append('        </state>')

for (frm, to, sym) in transitions:
    lines.append('        <transition>')
    lines.append(f'            <from>{name_to_id[frm]}</from>')
    lines.append(f'            <to>{name_to_id[to]}</to>')
    lines.append(f'            <read>{sym}</read>')
    lines.append('        </transition>')

lines.append('    </automaton>')
lines.append('</structure>')

with open("ka.jff", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("ka.jff создан.")
print("Состояний:", len(states))
print("Переходов:", len(transitions))