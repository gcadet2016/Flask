def display(param1,param2):
	print(param1)
	print(param2)

display("Bonjour","tout le monde")

def display(param1,param2):
	print(param1,param2)

display("Bonjour","tout le monde")

test_retour_display = display("Bonjour","tout le monde")
print(test_retour_display)

type(test_retour_display)

def display(param1):
	print(param1)
	return param1

retour_display = display("Bonjour")
print(retour_display)

def display(param1,param2):
	print(param1)
	print(param2)
	return param1, param2

