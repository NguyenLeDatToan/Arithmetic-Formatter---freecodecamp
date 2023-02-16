# arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

def calculate(num1, num2, operation):
  num1 = int(num1)
  num2 = int(num2)
  match operation:
    case "+":
      return str(num1 + num2)
    case "-":
      return str(num1 - num2)
    case _:
      return False
def isNum(num):
  try:
    int(num)
    return True
  except:
    return False
    
def test(num1, num2):
  if len(num1)>len(num2):
    print('*'*2+num1)
    print('+'+'*'*(max(len(num1),len(num2))-min(len(num1),len(num2))+1)+num2)
    print('-'*(max(len(num1),len(num2))+2))
    print('*'*(max(len(num1),len(num2))-len(calculate(num1, num2, '+'))+2)+calculate(num1, num2, '+'))
  elif len(num1)<len(num2):
    print('*'*(max(len(num1),len(num2))+2-min(len(num1),len(num2)))+num1)
    print('+'+'*'+num2)
    print('-'*(max(len(num1),len(num2))+2))
    print('*'*(max(len(num1),len(num2))-len(calculate(num1, num2, '+'))+2)+calculate(num1, num2, '+'))
  else:
    print('*'*2+num1)
    print('+'+'*'+num2)
    print('-'*(max(len(num1),len(num2))+2))
    print('*'*(max(len(num1),len(num2))-len(calculate(num1, num2, '+'))+2)+calculate(num1, num2, '+'))

def arithmetic_arranger(object, result=False): 
  # print('\n')
  # test("999", "9")
  # print('\n')
  if len(object)>5: return "Error: Too many problems."
  temp = ['']*4
  for arrValue in object:
    num = arrValue.split(" ")
    if len(num[0]) > 4 or len(num[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    elif isNum(num[0])==False or isNum(num[2])==False:
      return "Error: Numbers must only contain digits."
    else:
      
      if len(num[0])>len(num[2]):
        temp[0] += (' '*2+num[0]) +' '*4
        temp[1] += (num[1]+' '*(max(len(num[0]),len(num[2]))-min(len(num[0]),len(num[2]))+1)+num[2]) +' '*4
        temp[2] += ('-'*(max(len(num[0]),len(num[2]))+2)) +' '*4
      elif len(num[0])<len(num[2]):
        temp[0] += (' '*(max(len(num[0]),len(num[2]))+2-min(len(num[0]),len(num[2])))+num[0]) +' '*4
        temp[1] += (num[1]+' '+num[2]) +' '*4
        temp[2] += ('-'*(max(len(num[0]),len(num[2]))+2)) +' '*4
      else:
        temp[0] += (' '*2+num[0]) +' '*4
        temp[1] += (num[1]+' '+num[2]) +' '*4
        temp[2] += ('-'*(max(len(num[0]),len(num[2]))+2)) +' '*4

      if calculate(num[0], num[2], num[1]) == False: 
        return "Error: Operator must be '+' or '-'."
        
      temp[3] += (' '*(max(len(num[0]),len(num[2]))-len(calculate(num[0], num[2], num[1]))+2)+calculate(num[0], num[2], num[1])) +' '*4
      
      num = f"{temp[0]}\n{temp[1]}\n{temp[2]}"
      if result == True: num += f"\n{temp[3]}"
  return num