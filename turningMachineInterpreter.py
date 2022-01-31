'''
This is the interpreter that takes a turing machine in the from of a list of state objects
and a dictionary of state enumerations and runs the turing machine on the input string.
'''
def turingMachineInterpreter(state_obj_list, state_enumeration, turing_machine_input_str):
    # now that the turing machine has been encoded, let's run it!!
    current_index = 0
    current_state = 0
    # run the interpreter while the state isn't accepting or rejecting
    while current_state != state_enumeration['r'] and current_state != state_enumeration['a']:
        tape_value = turing_machine_input_str[current_index]
        state_object = state_obj_list[current_state]

        # get the next index and state based on the current state and the tape value
        (new_tape_value, next_index_increment, next_state) = state_object.executeOnRead(tape_value)
        # ugly char replacement due to strings being immutable in python
        turing_machine_input_str = turing_machine_input_str[:current_index] + new_tape_value + turing_machine_input_str[current_index + 1:]
        current_index += next_index_increment
        current_state = next_state

    if current_state == state_enumeration['a']:
        return_string = "ACCEPT"
    # additional out of bounds check
    if current_state == state_enumeration['r'] or current_index < 0 or current_index >= len(turing_machine_input_str):
        return_string = "REJECT"

    return turing_machine_input_str, return_string
