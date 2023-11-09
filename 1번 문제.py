#1번 문제
#클래스 정의, 각 계산기 인스턴스는 'calculator_id'와 빈 스택을 가짐
class Calculator:
    def __init__(self, calculator_id):
        self.calculator_id = calculator_id
        self.stack = []
#조건문을 사용하여 연산할 수 있음
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

# 예시 사용
calc1 = Calculator(calculator_id=1)
result = calc1.calculate("(3+5)*2")
print(result)  # 출력 결과: 16