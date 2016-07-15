transition_function = [
	{'0':[0],'1':[0,1,2]},
	{'0':[2]},
	{'1':[3]},
	{'0':[3],'1':[3]}
]

def nfa(input,init,final,transition_function):
	cur_state = []
	cur_state.append(init)
	for i in input:
		next_state = []
		for j in cur_state:
			if i in transition_function[j].keys():
				next_state += transition_function[j][i]
		cur_state=next_state
		if final in cur_state:
			print 'accept'
			return
	print 'not accept'
	
nfa("0010101000111",0,3,transition_function)
nfa("0110000001000",0,3,transition_function)
nfa("0000010000100010100",0,3,transition_function)
nfa("000001000100",0,3,transition_function)
nfa("010000001000",0,3,transition_function)
nfa("010001000010000100",0,3,transition_function)
