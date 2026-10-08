class DFA:
    def __init__(self, alphabet, states, accept, start, transitions):
        self.alphabet = alphabet
        self.states = states
        self.accept_states = accept
        self.start = start
        self.transitions = transitions

    def print_table(self):
        col_w = 10
        header = "state".ljust(col_w)
        for symbol in self.alphabet:
            header += ("delta(" + symbol + ")").ljust(col_w)
        print(header)
        print("-" * (col_w * (len(self.alphabet) + 1)))
        for state in self.states:
            mark = ""
            if state == self.start:
                mark = "->"
            if state in self.accept_states:
                mark += "*"
            row = (mark + state).ljust(col_w)
            for symbol in self.alphabet:
                next_state = self.transitions[(state, symbol)]
                row += next_state.ljust(col_w)
            print(row)
        print()

    def run(self, chain) -> None:
        current_state = self.start
        path = [current_state]
        position = 0

        while position < len(chain):
            symbol = chain[position]
            if (current_state, symbol) not in self.transitions:
                print(f"Цепочка {chain}: символ {symbol} вне алфавита -> REJECT")
                return
            current_state = self.transitions[(current_state, symbol)]
            path.append(current_state)
            position += 1

        accept = current_state in self.accept_states
        trace = " -> ".join(path)
        verdict = "ACCEPT" if accept else "REJECT"
        print(f"Цепочка {chain}")
        print(f"  Путь: {trace}")
        print(f"  Результат: {verdict}")


def _name(bits):
    s = ""
    for i in range(4, -1, -1):
        s += str((bits >> i) & 1)
    return "q" + s


def create_dfa():
    alphabet = ['0', '1']
    states = [_name(b) for b in range(32)]
    accept_states = [_name(b) for b in range(32) if (b & 0x10) != 0]
    start = _name(0)  # q00000
    transitions = {}
    for bits in range(32):
        cur = _name(bits)
        for sym in ('0', '1'):
            x = 0 if sym == '0' else 1
            new_bits = ((bits << 1) | x) & 0x1F
            transitions[(cur, sym)] = _name(new_bits)
    return DFA(alphabet, states, accept_states, start, transitions)