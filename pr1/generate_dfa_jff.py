import math

def name(bits):
    s = ""
    for i in range(4, -1, -1):
        s += str((bits >> i) & 1)
    return "q" + s

# 32 состояния: биты 0..31
states = []
for bits in range(32):
    is_final = (bits & 0x10) != 0   # первый бит = 1
    is_init = (bits == 0)           # q00000
    states.append((name(bits), is_init, is_final))

name_to_id = {n: i for i, (n, _, _) in enumerate(states)}

# Переходы: сдвиг влево + новый бит
transitions = []
for bits in range(32):
    for sym in ('0', '1'):
        x = 0 if sym == '0' else 1
        new_bits = ((bits << 1) | x) & 0x1F
        transitions.append((name(bits), name(new_bits), sym))

# Раскладка по кругу, чтобы граф не был кашей
positions = {}
for bits in range(32):
    angle = 2 * math.pi * bits / 32
    positions[name(bits)] = (400 + 300 * math.cos(angle),
                              400 + 300 * math.sin(angle))

# Генерация XML в формате .jff
lines = []
lines.append('<?xml version="1.0" encoding="UTF-8" standalone="no"?>')
lines.append('<structure>')
lines.append('    <type>fa</type>')
lines.append('    <automaton>')

for i, (n, is_init, is_final) in enumerate(states):
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

with open("dfa.jff", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("dfa.jff создан.")
print("Состояний:", len(states))
print("Переходов:", len(transitions))