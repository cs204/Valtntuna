def main():
    amount_due = 50
    total_amount = 0

    while total_amount < amount_due:
        remaining_due = amount_due - total_amount
        print(f"Нужная сумма: {remaining_due}")
        coin = int(input("Вставьте монету: "))
        total_amount += coin

    change_owed = total_amount - amount_due
    print(f"Ваша сдача: {change_owed}")
main()
