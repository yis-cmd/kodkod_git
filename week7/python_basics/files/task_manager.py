def load_tasks(filename):
    '''
    :dicts קוראת את הקובץ ומחזירה רשימה של
    [{'id': 1, 'status': 'PENDING', 'desc': 'ללמוד Python'}, ...]
    אם הקובץ לא קיים — מחזירה רשימה ריקה
    '''
    dict_form = ["id", "status", "desc"]
    try:
        with open(filename, "x"):
            pass
    except FileExistsError:
        pass 
    
    with open(filename, "r") as file:
        return [(dict(zip(dict_form, line.strip().split(sep="|")))) for line in file]
    

def save_tasks(filename, tasks):
    '''
    שומרת את רשימת המשימות לקובץ
    description|status|id :פורמט כל שורה
    '''
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task["id"]}|{task["status"]}|{task["desc"]}\n")

def add_task(filename, description):
    '''
    :מוסיפה משימה חדשה עם
    מספר המשימה הבאה = ID -
    - status = 'PENDING'
    הפרמטר שניתן = description -
    '''
    task_id = len(load_tasks(filename))
    with open(filename, "a") as file:
        file.write(f"{task_id}|PENDING|{description}\n")

def complete_task(filename, task_id):
    '''
    DONE-ל PENDING-מ id_task של משימה status משנה את
    לא קיים — מדפיסה הודעת שגיאה ID-אם ה
    '''
    tasks = load_tasks(filename)
    for task in tasks:
        if task["id"] == str(task_id):
            task["status"] = "DONE"
            break
    save_tasks(filename, tasks)

def list_tasks(filename):
    '''
    :מציגה את כל המשימות בפורמט מסודר
    ]✓[ 2 [ 2 |לכת תרתרג 1
    ] [ 3 | לסיים את הפרויקט
    '''
    tasks = load_tasks(filename)
    print("\n".join([f"id: {task["id"]}, status: {task["status"]} description: {task["desc"]}" for task in tasks]))

def main():
    FILENAME = "tasks.txt"
    while True:
        print('\n=== To-Do List Manager ===')
        print('הצג משימות 1.')
        print('הוסף משימה 2.')
        print('סמן כהושלם 3.')
        print('יציאה 4.')
        choice = input('בחירה:')
        if choice == '1':
            list_tasks(FILENAME)
        elif choice == '2':
            desc= input(' :תיאור המשימה')
            add_task(FILENAME, desc)
            print('!המשימה נוספה')
        elif choice == '3':
            task_id = int(input('משימה מספר:'))
            complete_task(FILENAME, task_id)
        elif choice == '4':
            print('!להתראות')
            break
        else:
            print('בחירה לא תקינה')
if __name__ == '__main__':
    main()