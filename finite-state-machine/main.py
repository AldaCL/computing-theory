import pandas as pd
import argparse
# Lexical analysis based on a csv file that represents transition table of a Defined Finite Automata
# The csv file is read and the transition table is created
# The transition table is used to determine if a given string is accepted by the DFA
# The string is read from a file and the result of the lexical analysis is printed to the console

# The program accepts as arguments the name of the file that contains the transition table and the string to be analyzed


if __name__ == "__main__":
    # get inputs from user
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--table", help="The name of the file that contains the transition table, in csv format")
    parser.add_argument("-s", "--string", help="The name of the file that contains the string to be analyzed")
    args = parser.parse_args()
    
    file_name = args.table + ".csv" if args.table else 'transition_table.csv'
    string_tba = args.string if args.string else '1234.5'
    string_tba = string_tba.strip()

    transition_table = pd.read_csv(file_name)
    states = transition_table['state']
    syntaxis = transition_table.columns.to_list()
        
    print("Transition table:")
    print(transition_table)

    # Initialize the state of the DFA   
    state = 1
    len_of_string = len(string_tba) -1
    # Read the string to be analyzed
    print("\nString to be analyzed: ", string_tba)
    print("\nAnalysis:")
    for index, original_symbol in enumerate(string_tba):
        # Check if the symbol is a number, then corresponds to column "number"
        
        symbol = 'number' if original_symbol.isdigit() else original_symbol
        if symbol in syntaxis:
            # breakpoint()
            state = int(transition_table[symbol][state-1])
            print(f"Symbol: {original_symbol} with state: {state}")
            
            if symbol == "error":
                state = "error"
                print("Symbol {symbol} with state {state}")
                break
        else:
            print(f"Symbol {symbol} not recognized")
            print("String not accepted")
            break
        if index == len_of_string:
            state = transition_table["eos"][state-1]

    print(f"Final state: {state}")
    if state == "error":
        print("String not accepted")
    elif state == "accept":
        print("String accepted")
