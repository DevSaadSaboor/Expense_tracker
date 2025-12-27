import os 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR  = os.path.dirname(BASE_DIR)
FILE_PATH = os.path.join(PROJECT_DIR,'data','data.txt')



def load_expenses():
    expense = []
    try:
        with open(FILE_PATH , 'r') as file:
              for line in file:
                    line = line.strip()
                    if not line:
                          continue
                    id,amount,category,note,date = line.split(',')
                    expenses = {
                   'id' : int(id),
                   'amount' : float(amount),
                   'category' : category,
                   'note' : note,
                   'date' : date
                    }
                    expense.append(expenses)
          
    except FileNotFoundError:
           return []
    
    return expense
           
def save_expenses(expense):
      try:
        with open(FILE_PATH , 'w') as file:
             for i in expense:
                  file.write(f'{i['id']},{i['amount']},{i['category']},{i['note']},{i['date']}\n')
             return True
      except OSError:
           return False

          
      
            