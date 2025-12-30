
from service.expense_service import add_expense,list_expenses,delete_expeses

# ANSI color codes (work in most terminals)
RESET = "\033[0m"
BOLD = "\033[1m"

CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"

while True:
    print(BOLD + CYAN  +'1) ADD EXPENSE' + RESET)
    print(BOLD + CYAN  + '2) SHOW EXPENSE' + RESET)
    print(BOLD + CYAN  +'3) DELETE EXPENSE', RESET)
    print(BOLD + CYAN  +'4) EXIT' + RESET)
    print('-' * 50)

    user_choice = input('Enter choice from 1 to 4 ')

    if user_choice == '1':
        amount = float(input('ENTER AMOUNT'))
        category = input('WHAT IS THE CATEGORY ')
        note = input('ANY EXTRA NOTE ')
        date = input('ENTER THE DATA IN DD/MM/YYYY FORMAT ')

        ok,msg = add_expense(amount,category,note,date)
        if ok:
            print(GREEN + msg + RESET)
        else:
            print(RED + msg + RESET)

        print("-" * 50)

    
    elif user_choice == '2':
        expenses = list_expenses()

        if not expenses:
             print(RED + 'NO EXPENSES YET' + RESET)
        else:
           print(
            BOLD + CYAN +
            f"{'ID':<4} {'DATE':<12} {'CATEGORY':<14} {'AMOUNT':<10} NOTE" +
            RESET
        )
        print('-' * 50)

        for e in expenses:
            print(
                f"{e['id']:<4} "
                f"{e['date']:<12} "
                f"{e['category']:<12} "
                f"{e['amount']:<10.2f} "
                f"{e['note']:<12}"                
            )
            print('-' * 50)
       
    elif user_choice == '3':
        expense_id = input('ENTER THE EXPENSE ID YOU WANT TO DELETE ')
        ok,msg = delete_expeses(expense_id)
        if ok:
              print(GREEN + msg + RESET)
        else:
            print(RED + msg + RESET)

        print("-" * 50)


    elif user_choice == '4':
        print('EXIT')
        break
    else:
        print(RED + "INVALID CHOICE" + RESET)
        print("-" * 50)
        





