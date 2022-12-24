def main(expr):
  operands = []
  operators = []
  buffer = ''
  for c in expr:
    if c in ['&', '|', '^']:
      operands.append(buffer)
      buffer = ''
      operators.append(c)
    else:
      buffer += c
  operands.append(buffer)

  values = []
  for i in range(2**len(operands)):
    values.append([int(x) for x in bin(i)[2:].zfill(len(operands))])
  results = []
  for row in values:
    result = expr
    for i, operand in enumerate(operands):
      result = result.replace(operand, str(row[i]).lower())
    results.append(eval(result))

  output = ' '.join(operands) + ' | ' + expr + '\n'
  output += '-' * len(expr) * 2 + '\n'
  for row, result in zip(values, results):
    output += ' '.join([str(x).replace('1', 'T').replace('0', 'F') for x in row]) + ' | ' + str(result) + '\n'
  print(output)
  return output


main("a&b|c")