import tkinter as tk

# 创建计算器类
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Python 计算器")

        # 添加文本框组件
        self.display = tk.Entry(master, width=30, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # 定义数字按钮
        button_1 = self.create_button('1', 1, 0)
        button_2 = self.create_button('2', 1, 1)
        button_3 = self.create_button('3', 1, 2)
        button_4 = self.create_button('4', 2, 0)
        button_5 = self.create_button('5', 2, 1)
        button_6 = self.create_button('6', 2, 2)
        button_7 = self.create_button('7', 3, 0)
        button_8 = self.create_button('8', 3, 1)
        button_9 = self.create_button('9', 3, 2)
        button_0 = self.create_button('0', 4, 1)

        # 定义运算符号按钮
        button_addition = self.create_button('+', 1, 3)
        button_subtraction = self.create_button('-', 2, 3)
        button_multiplication = self.create_button('*', 3, 3)
        button_division = self.create_button('/', 4, 3)

        # 定义其他按钮
        button_clear = self.create_button('C', 4, 0)
        button_equal = self.create_button('=', 4, 2)

        # 定义事件处理函数
        self.equation = ''
    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, width=7, height=2, font=('Arial', 16), command=lambda: self.click(text))
        button.grid(row=row, column=column, padx=5, pady=5)
        return button

    def click(self, key):
        if key == 'C':
            self.equation = ''
            self.display.delete(0, tk.END)
        elif key == '=':
            result = str(eval(self.equation))
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
            self.equation = result
        else:
            self.equation += key
            self.display.insert(tk.END, key)

# 创建主窗口并运行程序
if __name__ == '__main__':
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()