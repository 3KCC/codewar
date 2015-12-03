def test_brackets(exp):
	openSign = ['(', '[', '{']
	closeSign = [')',']','}']
	stack = []
	for i in range(len(exp)):
		if exp[i] in openSign or exp[i] in closeSign:
			if exp[i] in openSign:
				stack.append(exp[i])
			elif exp[i] in closeSign and stack and closeSign.index(exp[i]) == openSign.index(stack[-1]):
				stack.pop()
			else:
				return -1
	if stack:
		return -1
	else:
		return True

print test_brackets(raw_input())
