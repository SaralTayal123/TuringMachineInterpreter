from turingMachineStringParser import turningMachineParser
from turningMachineInterpreter import turingMachineInterpreter

# main function
if __name__ == "__main__":
 
    # sample turing machine input string format
    sample_turing_machine_str = """
def M(x):
    i = 0
    STATE 0: 
        switch(x[i]):
            case 'a':  x[i] = 'a'; i++; go to STATE 1;
            case 'b':  x[i] = '-'; i--; go to STATE 0;
            case '-':  x[i] = 'b'; i++; go to STATE reject;
    STATE 1: 
        switch(x[i]):
            case 'a':  x[i] = 'b'; i--; go to STATE accept;
            case 'b':  x[i] = 'a'; i++; go to STATE reject;
            case '-':  x[i] = '-'; i--; go to STATE 0;
"""
    ### Sample Data ###
    # sample input string, expected output "abbbb" and "ACCEPT"
    sample_string_pass = "aabbb"
    # infinite loop test
    sample_string_infinite_loop = "a-"
    # sample string input that will reject
    sample_string_reject = "bb" # reject bc reading out of bounds
    sample_string_reject2 = "ab" 

    # parse the turing machine string
    (state_obj_list, state_enumeration) = turningMachineParser(sample_turing_machine_str)

    # run the interpreter
    print("Input: ", sample_string_pass, ", Output: ", turingMachineInterpreter(state_obj_list, state_enumeration, sample_string_pass))
    print("Input: ", sample_string_reject, ", Output: ", turingMachineInterpreter(state_obj_list, state_enumeration, sample_string_reject))
    print("Input: ", sample_string_reject2, ", Output: ", turingMachineInterpreter(state_obj_list, state_enumeration, sample_string_reject2))