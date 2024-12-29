from evol_nums import *
import colorama
from colorama import Fore, Style
colorama.init()

# Colors for different test cases
TEST_COLORS = [Fore.CYAN, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA]

def print_header(text):
    print(f"\n{Fore.WHITE}{'='*70}")
    print(f"{text.center(70)}")
    print(f"{'='*70}{Style.RESET_ALL}")

def evol_num_formula(n, seed, c):
    x, y = seed
    formula_buffer = [0] * n
    formula_buffer[0] = x
    for i in range(1, n - 1):
        formula_buffer[i] = 2 ** (i - 1) * (x + y + c)
    formula_buffer[n - 1] = (2 ** (n - 3) * (x + y + c)) - c
    return formula_buffer

def print_test_case(params, buffer, color_index):
    color = TEST_COLORS[color_index % len(TEST_COLORS)]
    print(f"\n{color}Test Case {color_index + 1}")
    print("-" * 50)
    print(f"Parameters:")
    for key, value in params.items():
        print(f"  {key:<10} = {value}")
    print(f"Result = {buffer}")
    
    # Check doubling relationship
    doubling_check = all(buffer[i] == 2 * buffer[i - 1] for i in range(2, len(buffer) - 1))
    if doubling_check:
        print(f"{color}Doubling Check Passed: True{Style.RESET_ALL}")
    else:
        print(f"{color}Doubling Check Passed: False{Style.RESET_ALL}")
    
    # Compute buffer using the formula
    formula_buffer = evol_num_formula(params['n'], params['seed'], params['c'])
    match_check = buffer == formula_buffer
    if match_check:
        print(f"{color}Formula Match Passed: True{Style.RESET_ALL}")
    else:
        print(f"{color}Formula Match Passed: False{Style.RESET_ALL}")
        print(f"Expected by Formula: {formula_buffer}")
    print(f"{'-'*50}{Style.RESET_ALL}")

def explore_variable_c():
    print_header("Exploring Different Values of Constant c")
    for i, c in enumerate(range(1, 5)):
        params = {
            'c': c,
            'n': 8,
            'seed': [3, 1]
        }
        buffer = evol_nums(8, [3, 1], c)
        print_test_case(params, buffer, i)

def explore_variable_n():
    print_header("Exploring Different Buffer Sizes (n)")
    for i, n in enumerate([4, 6, 8, 10]):
        params = {
            'c': 1,
            'n': n,
            'seed': [3, 1]
        }
        buffer = evol_nums(n, [3, 1], 1)
        print_test_case(params, buffer, i)

def explore_initial_buffer():
    print_header("Exploring Different Seeds")
    initial_buffers = [[3, 1], [5, 2], [7, 3], [10, 5]]
    for i, init in enumerate(initial_buffers):
        params = {
            'c': 1,
            'n': 8,
            'seed': init
        }
        buffer = evol_nums(8, init, 1)
        print_test_case(params, buffer, i)

def explore_c_seed_dynamics():
    print_header("Exploring C and Seed Dynamics")
    # Test cases with corresponding c values and seeds
    test_cases = [
        (2, [0, 4]),
        (2, [1, 3]),
        (2, [2, 2]),
        (2, [-8, 12])
    ]
    n = 9
    for i, (c, seed) in enumerate(test_cases):
        params = {
            'c': c,
            'n': n,
            'seed': seed
        }
        buffer = evol_nums(n, seed, c)
        print_test_case(params, buffer, i)

# Run all explorations
print_header("PARAMETER EXPLORATION ANALYSIS")
explore_variable_c()
explore_variable_n()
explore_initial_buffer()
explore_c_seed_dynamics()
