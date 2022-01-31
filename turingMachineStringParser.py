from turingMachineStateClass import State

'''
Not the most elegant string parser due to the messy nature of string parsing. But this is a robust 
string parser that can handle 1000 states (or more with a change of 1 value).

This parser will read a standardized string containing a turing machine based on the format used 
in the hadnout. The parser loops through the input string 2 times and this is to allow for out of 
order state declarations. Ie. STATE 1 could be declared before STATE 0. 
'''
def turningMachineParser(turing_machine_str):
    max_num_states = 3 # 3 digits of states so up to a 1000 states
    tm_string_len = len(turing_machine_str)
    state_obj_list = [] 
    state_enumeration = {}

    parser_end_len = 0

    # find out how many states there are
    while parser_end_len < tm_string_len:
        state_start_index = turing_machine_str.find("STATE ", parser_end_len, -1)
        state_end_index = turing_machine_str.find(":", state_start_index, state_start_index + max_num_states + len("STATE ")) 

        # if valid state transition block
        if (state_start_index != -1) and (state_end_index != -1):
            # enumerate the states to easily map between state chars and an actual enumeration 
            state_enumeration[turing_machine_str[state_end_index - 1 : state_end_index]] = len(state_enumeration.keys())

            # create a state object and save it for later use
            state_enum_value = state_enumeration[turing_machine_str[state_end_index - 1 : state_end_index]] 
            state_obj_list.append(State(state_enum_value, state_start_index, -1 ))

            # update the parser end index if not the first index
            if len(state_obj_list) > 1:
                state_obj_list[len(state_obj_list) - 2].state_index_end = state_start_index
            
        # no more valid state transition blocks
        if (state_start_index == -1) and (state_end_index == -1):
            break
    
        parser_end_len = state_start_index + len("STATE ")

    # add the accept and reject states into the state enumeration
    state_enumeration['a'] = len(state_enumeration.keys()) 
    state_enumeration['r'] = len(state_enumeration.keys()) 


    # now that all the states have been discretized, find the transitions
    for state in state_obj_list:
        # split states based on the 2 tabs worth of spaces => 8 spaces
        state_transitions = turing_machine_str[state.state_index_start: state.state_index_end].split("        ")
        # make filter out non transitions 
        state_transitions = [transition_candidate for transition_candidate in state_transitions if "case" in transition_candidate]

        # loop through all the cases and get the transitions and populate that in the state object
        for transition in state_transitions:
            state_case = transition[10:11]
            tape_replacement_value = transition[23:24] 
            tape_incrament = transition[28:29]  
            next_state = state_enumeration[transition[44:45]] # get the enumeration for the next state
            state.processAndStoreTransition(state_case, tape_replacement_value, tape_incrament, next_state)
        
    return state_obj_list, state_enumeration

