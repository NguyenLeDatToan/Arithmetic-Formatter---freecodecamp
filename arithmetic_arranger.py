def calculate(num1, num2, operation):
  num1 = int(num1); num2 = int(num2)
  match operation:
    case "+":
      return str(num1 + num2)
    case "-":
      return str(num1 - num2)
    case _:
      return False

def isNum(num):
  try:
    int(num); return True
  except:
    return False

def arithmetic_arranger(problems, result=False):
  if len(problems)>5: return "Error: Too many problems."
  temp = ['']*4
  for index, arrValue in enumerate(problems):
    arranged_problems = arrValue.split(" ")
    if len(arranged_problems[0]) > 4 or len(arranged_problems[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    elif isNum(arranged_problems[0])==False or isNum(arranged_problems[2])==False:
      return "Error: Numbers must only contain digits."
    else:
      
      if len(arranged_problems[0])>len(arranged_problems[2]):
        temp[0] += (' '*2+arranged_problems[0])
        temp[1] += (arranged_problems[1]+' '*(max(len(arranged_problems[0]),len(arranged_problems[2]))-min(len(arranged_problems[0]),len(arranged_problems[2]))+1)+arranged_problems[2])
        temp[2] += ('-'*(max(len(arranged_problems[0]),len(arranged_problems[2]))+2))
      elif len(arranged_problems[0])<len(arranged_problems[2]):
        temp[0] += (' '*(max(len(arranged_problems[0]),len(arranged_problems[2]))+2-min(len(arranged_problems[0]),len(arranged_problems[2])))+arranged_problems[0])
        temp[1] += (arranged_problems[1]+' '+arranged_problems[2])
        temp[2] += ('-'*(max(len(arranged_problems[0]),len(arranged_problems[2]))+2))
      else:
        temp[0] += (' '*2+arranged_problems[0])
        temp[1] += (arranged_problems[1]+' '+arranged_problems[2])
        temp[2] += ('-'*(max(len(arranged_problems[0]),len(arranged_problems[2]))+2))
        
      if calculate(arranged_problems[0], arranged_problems[2], arranged_problems[1]) == False: 
        return "Error: Operator must be '+' or '-'."
        
      temp[3] += (' '*(max(len(arranged_problems[0]),len(arranged_problems[2]))-len(calculate(arranged_problems[0], arranged_problems[2], arranged_problems[1]))+2)+calculate(arranged_problems[0], arranged_problems[2], arranged_problems[1]))

      if index<len(problems)-1:
        temp[0]+=' '*4
        temp[1]+=' '*4
        temp[2]+=' '*4
        temp[3]+=' '*4
      
      arranged_problems = f"{temp[0]}\n{temp[1]}\n{temp[2]}"
      if result == True: arranged_problems += f"\n{temp[3]}"
  return arranged_problems