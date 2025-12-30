
from storage.expense_storage import load_expenses,save_expenses

def add_expense(amount,category,note,date):
    expense = load_expenses()
    next_id = 1 if  not expense else max(i['id'] for i in expense) + 1 

    new_expense = {
        'id' : next_id,
        'amount' :amount,
        'category' : category,
        'note' : note,
        'date' : date
    }
    expense.append(new_expense)

    if not save_expenses(expense):
        return False , 'NOT SAVED'
    

    return True,'NEW EXPENSES ADDED'


def list_expenses():
    return load_expenses()

def delete_expeses(expense_id):
    expense = load_expenses()
    expense_id = int(expense_id)
    
    updated_expenses = [i for i in expense if i['id'] !=  expense_id]

    if len(updated_expenses) == len(expense):
        return False , 'EXPENSES NOT FOUND'
    
    if not save_expenses(updated_expenses):
        return False, 'EXPENSES NOT SAVED'
    
    return True, 'EXPENSES SAVED SUCCESSFULLY'






   
   

