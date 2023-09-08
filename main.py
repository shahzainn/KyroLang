variables = {
  "x": {'value': '30'},
  "k": {'value': '"hello"'}
}

while True:
  
  command = input(">>> ")

  if command[0:6] == "output":
    
    transpiledLine = "print("
    args = command.split('"')[1::2]
  
    if len(args) != 1:
      multipleArguments = True
    else:
      multipleArguments = False
  
    for argument in args:
      if multipleArguments == True and argument != args[0]:
        transpiledLine += ' + "' + argument + '"'
      else:
        transpiledLine += '"' + argument + '"'
  
    transpiledLine += ")"
  
    eval(transpiledLine)
  
  if "=" in command and command[0:6] != "output":
    
    variableName = command.split('=')[0]
  
    varname = [value for value in variableName if value != " "]
  
    variableName = ""
  
    for letter in varname:
      variableName += letter
  
    if variableName in variables:
  
      key = variables[variableName]
      key['value'] = command.split('=')[1]
      
    else:
      
      value = command.split('=')[1]
      datatype = type(value)
      
      variables[variableName] = {"value": value}
  
  if command in variables and "=" not in command:
    print(variables[command]['value'])

  if "+" in command:
    
    sides = command.split('+')
    numbers = []

    failed = False
    
    for number in sides:
      
      try:
        
        numbers.append(int(number))

        failed = False

      except ValueError:

        if number in variables:

          try:

            numbers.append(int(variables[number]['value']))

            failed = False

          except ValueError:

            print('Fatal error. Variable cannot be converted to number.')
            failed = True
        
    if not failed: print(sum(numbers))
