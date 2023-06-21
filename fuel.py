def main():
    while True:
        try:
            fraction = input()
            x, y = map(int, fraction.split('/'))

            if x <= 0 or y <= 0 or x > y:
                raise ValueError

            percent = (x / y) * 100

            if percent <= 1:
                result = "E"
            elif percent >= 99:
                result = "F"
            else:
                rounded_percent = round(percent)
                result = f"{rounded_percent}%"

            print(f"Дробь: {result}")
            break

        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")
        except ZeroDivisionError:
            print("Деление на ноль. Попробуйте снова.")



main()
