''' 
Simple state class that has a method to ingest string data and store it appopriately 
within the object and another method that helps the interpreter determine the next tape value 
'''
class State:
    def __init__(self, state_name, state_index_start, state_index_end):
        self.state_name = state_name
        self.state_index_start = state_index_start
        self.state_index_end = state_index_end

    def processAndStoreTransition(self,tape_value, tape_replacement_value, tape_incrament, next_state):
        if tape_value == 'a':
            self.a_tape_replacement = tape_replacement_value
            self.a_increment = 1 if tape_incrament == '+' else -1
            self.a_next_state = next_state 
        if tape_value == 'b':
            self.b_tape_replacement = tape_replacement_value
            self.b_increment = 1 if tape_incrament == '+' else -1
            self.b_next_state = next_state 
        if tape_value == '-':
            self.blank_tape_replacement = tape_replacement_value
            self.blank_increment = 1 if tape_incrament == '+' else -1
            self.blank_next_state = next_state 
    def executeOnRead(self, tape_value):
        if tape_value == 'a':
            return (self.a_tape_replacement, self.a_increment, self.a_next_state)
        if tape_value == 'b':
            return (self.b_tape_replacement, self.b_increment, self.b_next_state)
        if tape_value == '-':
            return (self.blank_tape_replacement, self.blank_increment, self.blank_next_state)


