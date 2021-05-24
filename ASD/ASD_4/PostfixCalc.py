def postfics_calculus(string):
    s = []
    if len(string) == 1:
        return string[0]
    else:
        for i in string:
            if i.isdigit() == True:
                s.append(i)
            elif i in '*-/+':
                operand1 = int(s.pop())
                operand2 = int(s.pop())

                if i == '+':
                    s.append(operand2 + operand1)
                elif i == '-':
                    s.append(operand2 - operand1)
                elif i == '*':
                    s.append(operand2 * operand1)
                elif i == '/' and operand2 != 0:
                    s.append(operand2 / operand1)
    return(s[0])
print(postfics_calculus("12+5*"))