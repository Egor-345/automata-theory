from dfa.dfa import create_dfa
from nfa.nfa import create_nfa


def main():
    dfa = create_dfa()
    nfa = create_nfa()

    print("=== DFA (вариант 6а) ===")
    dfa.print_table()
    dfa_tests = ["11111", "01111", "1010101", "10000", "00000", "1000", "111111", "1010"]
    for chain in dfa_tests:
        dfa.run(chain)

    print()
    print("=== NFA (вариант 6б) ===")
    nfa.print_table()
    nfa_tests = ["", "a", "b", "ba", "ab", "bba", "aab", "bbbaaa"]
    for chain in nfa_tests:
        nfa.run(chain)


if __name__ == "__main__":
    main()