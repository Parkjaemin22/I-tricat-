import math

class Calculator:
    def __init__(self, calculator_id):
        self.calculator_id = calculator_id
        self.result = None

    def calculate(self, expression):
        try:
            self.result = str(eval(expression, {}, {}))
            return self.result
        except Exception as e:
            self.result = f"Error: {e}"
            return self.result

    def get_final_result(self):
        return self.result


class EngineerCalculator(Calculator):
    def __init__(self, calculator_id):
        super().__init__(calculator_id)

    def calculate(self, expression):
        try:
            self.result = str(eval(expression, {"__builtins__": None}, {"sin": math.sin, "cos": math.cos, "tan": math.tan, "factorial": math.factorial}))
            return self.result
        except Exception as e:
            self.result = f"Error: {e}"
            return self.result

# 사용자 인터페이스
def main():
    calculators = {}

    while True:
        print("\n1. Basic Calculator\n2. Engineer Calculator\n3. Exit")
        choice = input("Choose a calculator (1/2/3): ")
        # 조건문을 사용하여 계산기를 선택할 수 있다
        if choice == '1':
            calculator_id = input("Enter Basic Calculator ID: ")
            calculators[calculator_id] = Calculator(calculator_id)
        elif choice == '2':
            calculator_id = input("Enter Engineer Calculator ID: ")
            calculators[calculator_id] = EngineerCalculator(calculator_id)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue  # 다시 반복문으로 돌아감

        expression = input(f"Enter expression for Calculator {calculator_id}: ")
        result = calculators[calculator_id].calculate(expression)
        print(f"Result: {result}")

    # 프로그램 종료 시 각 계산기의 최종 결과 출력
    print("\nFinal Results:")
    for calculator_id, calculator in calculators.items():
        final_result = calculator.get_final_result()
        print(f"Calculator {calculator_id}: {final_result}")

if __name__ == "__main__":
    main()
