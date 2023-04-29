# 定义计算函数
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return None

# 获取用户输入
num1 = float(input("请输入第一个数字："))
operator = input("请输入运算符号（+、-、*、/）：")
num2 = float(input("请输入第二个数字："))

# 计算结果并输出
result = calculate(num1, num2, operator)
if result is not None:
    print("结果为：", result)
else:
    print("无效的运算符号！")