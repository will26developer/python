


def arithmetic_arrange(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    line1, line2, line3, line4 = [], [], [], []

    for problem in problems:
        op1, sign, op2 = problem.split()

        if sign != '+' and sign != '-':
            return "Error: Operator must be '+' or '-'."
        if not op1.isdigit() or not op2.isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(op1) > 4 or len(op2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        width = max(len(op1), len(op2)) + 2
        result = int(op1) + int(op2) if sign == '+' else int(op1) - int(op2)

        line1.append(op1.rjust(width))
        line2.append(sign + op2.rjust(width - 1))
        line3.append('-' * width)
        line4.append(str(result).rjust(width))

    gap = ' ' * 4
    lines = [gap.join(line1), gap.join(line2), gap.join(line3)]
    if show_answers:
        lines.append(gap.join(line4))
    return '\n'.join(lines)
        
print(arithmetic_arrange(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],show_answers=True))