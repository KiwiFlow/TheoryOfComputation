#接受含有001的字符串的有穷自动机
transition_function = [
	{'0':1,'1':0},
	{'0':2,'1':0},
	{'0':2,'1':3},
	{'0':3,'1':3}
	]
	
def fa(input,transition_function,init_state,final_state):
	state=init_state
	for i in input:
		state = transition_function[state][i]
	if state == final_state:
		print "accept"
	else:
		print "not accept"

fa("0010",transition_function,0,3)
fa("1001",transition_function,0,3)
fa("001",transition_function,0,3)
fa("111111100111111111",transition_function,0,3)
fa("111111",transition_function,0,3)
fa("00000000000",transition_function,0,3)
