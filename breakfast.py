menu = {
   "кофе": 20.00,
   "чай": 10.00,
   "булочка": 5.00,
   "салат": 30.40,
   "пирожное": 45.50
}

def main():
    total_cost = 0.0
    while True:
        try:
            dish = input("Блюдо: ").lower()

            if dish == "":
                break

            if dish in menu:
                total_cost += menu[dish]
            else:
                print("Блюдо отсутствует в меню. Попробуйте снова.")

        except EOFError:
            break

    print("\n" + f"Сумма: {total_cost:.2f}")
main()
