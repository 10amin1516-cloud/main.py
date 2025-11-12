from tkinter import *
import math

# ------------------------------------
# 1. متغيرات ودوال العمليات
# ------------------------------------
expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("خطأ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def scientific_function(func):
    global expression
    try:
        if not expression:
            equation.set("خطأ: إدخال قيمة أولاً")
            return

        num = float(expression)

        if func == 'sqrt':
            if num < 0:
                equation.set("خطأ (جذر سالب)")
                expression = ""
                return
            result = math.sqrt(num)
        elif func == 'sin':
            result = math.sin(math.radians(num))
        elif func == 'cos':
            result = math.cos(math.radians(num))
        elif func == 'tan':
            result = math.tan(math.radians(num))
            
        equation.set(str(result))
        expression = str(result)
        
    except Exception:
        equation.set("خطأ")
        expression = ""


# ------------------------------------
# 2. إعداد الواجهة الرسومية (GUI)
# ------------------------------------

if __name__ == "__main__":
    win = Tk()
    win.configure(background="#4a4a4a") 
    win.title("الآلة الحاسبة العلمية")
    
    win.geometry("400x550") 

    equation = StringVar() 
    
    expression_field = Entry(win, textvariable=equation, width=25, relief=RIDGE, bd=10, 
                             insertwidth=2, font=('Arial', 20), justify='right', bg="#e0e0e0")
    
    expression_field.grid(row=0, columnspan=5, padx=5, pady=5, ipady=10, sticky="nsew")
    
    # 3. إعداد الأزرار
    BTN_PROPS = {'fg': 'white', 'bg': '#696969', 'font': ('Arial', 14, 'bold'), 
                 'height': 2, 'width': 5, 'relief': 'groove', 'bd': 5}
    
    buttons_map = [
        ('C', clear, 1, 0, '#cc0000'), ('/', lambda: press("/"), 1, 3, '#ffa500'),
        ('sin', lambda: scientific_function('sin'), 1, 1, '#0099cc'), ('cos', lambda: scientific_function('cos'), 1, 2, '#0099cc'),
        
        ('7', lambda: press(7), 2, 0, BTN_PROPS['bg']), ('8', lambda: press(8), 2, 1, BTN_PROPS['bg']),
        ('9', lambda: press(9), 2, 2, BTN_PROPS['bg']), ('*', lambda: press("*"), 2, 3, '#ffa500'),
        ('tan', lambda: scientific_function('tan'), 2, 4, '#0099cc'),

        ('4', lambda: press(4), 3, 0, BTN_PROPS['bg']), ('5', lambda: press(5), 3, 1, BTN_PROPS['bg']),
        ('6', lambda: press(6), 3, 2, BTN_PROPS['bg']), ('-', lambda: press("-"), 3, 3, '#ffa500'),
        ('sqrt', lambda: scientific_function('sqrt'), 3, 4, '#0099cc'),

        ('1', lambda: press(1), 4, 0, BTN_PROPS['bg']), ('2', lambda: press(2), 4, 1, BTN_PROPS['bg']),
        ('3', lambda: press(3), 4, 2, BTN_PROPS['bg']), ('+', lambda: press("+"), 4, 3, '#ffa500'),
        ('(', lambda: press('('), 4, 4, '#696969'),

        ('0', lambda: press(0), 5, 0, BTN_PROPS['bg']), ('.', lambda: press('.'), 5, 1, BTN_PROPS['bg']),
        ('=', equalpress, 5, 2, '#00cc00'), (')', lambda: press(')'), 5, 3, '#696969')
    ]
    
    # إنشاء الأزرار وتوزيعها
    # ⬇️ تم تعديل السطر 115 وطريقة التعامل مع الأزرار هنا ⬇️
    for (text, command, row, col, bg_color) in buttons_map:
        # إنشاء الزر وتعيينه لمتغير مؤقت
        button = Button(win, text=text, command=command, **BTN_PROPS, bg=bg_color)
        
        # استخدام grid في سطر منفصل (حل مشكلة السطر 115)
        button.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)

    # 4. تمديد الأعمدة والصفوف بالتساوي
    for i in range(6):
        win.grid_rowconfigure(i, weight=1)
    for i in range(5):
        win.grid_columnconfigure(i, weight=1)

    win.mainloop()
