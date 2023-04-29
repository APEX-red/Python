import math

def calculator():
    print("欢迎使用科学计算器！")
    while True:
        try:
            expr = input("请输入要计算的表达式（输入q退出）：")
            if expr == 'q':
                break
            result = eval(expr, {'__builtins__': None}, {
                          'sin': math.sin,
                          'cos': math.cos,
                          'tan': math.tan,
                          'log': math.log,
                          'exp': math.exp})
            print(f"结果为：{result}")
        except Exception as e:
            print("输入错误，请重新输入！")
            print(e)
