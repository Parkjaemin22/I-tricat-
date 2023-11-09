class Calculator:
    def __init__(self, calculator_id):
        self.calculator_id = calculator_id
        self.stack = []

    def calculate(self, expression):
        try:
            self.stack = []
            for char in expression:
                if char.isdigit():
                    self.stack.append(int(char))
                elif char in "+-*/":
                    if len(self.stack) < 2:
                        raise ValueError("Invalid expression")
                    b = self.stack.pop()
                    a = self.stack.pop()
                    if char == '+':
                        self.stack.append(a + b)
                    elif char == '-':
                        self.stack.append(a - b)
                    elif char == '*':
                        self.stack.append(a * b)
                    elif char == '/':
                        self.stack.append(a / b)
                elif char == '(':
                    self.stack.append(char)
                elif char == ')':
                    if '(' not in self.stack:
                        raise ValueError("Unmatched parentheses")
                    self.stack.pop()
            
            if '(' in self.stack:
                raise ValueError("Unmatched parentheses")
            
            if len(self.stack) != 1:
                raise ValueError("Invalid expression")

            return self.stack[0]

        except Exception as e:
            return f"Error: {e}"


import math
#Calculator 상속
class EngineerCalculator(Calculator):
    def __init__(self, calculator_id):
        super().__init__(calculator_id)

    def sin(self, angle):
        # math 모듈의 sin 함수 사용
        return math.sin(angle)

    def cos(self, angle):
        # math 모듈의 cos 함수 사용
        return math.cos(angle)

    def tan(self, angle):
        # math 모듈의 tan 함수 사용
        return math.tan(angle)

    def factorial(self, n):
        # 재귀적인 방식으로 팩토리얼 계산
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n-1)

# 예시 사용
engineer_calc = EngineerCalculator(calculator_id=2)
result_sin = engineer_calc.sin(math.pi / 2)
result_cos = engineer_calc.cos(math.pi)
result_tan = engineer_calc.tan(math.pi / 4)
result_factorial = engineer_calc.factorial(5)

print(result_sin)        # 출력 결과: 1.0 (sin(90도))
print(result_cos)        # 출력 결과: -1.0 (cos(180도))
print(result_tan)        # 출력 결과: 1.0 (tan(45도))
print(result_factorial)  # 출력 결과: 120 (5!)