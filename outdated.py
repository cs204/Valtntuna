months = ["январь", "февраль", "март", "апрель",
          "май", "июнь", "июль", "август", "сентябрь", "октябрь",
          "ноябрь", "декабрь"]

def is_valid_date(date_str):
    parts = date_str.split()
    if len(parts) != 3:
        return False

    day, month, year = parts
    if not day.isdigit() or not year.isdigit():
        return False

    month = month.lower()
    if month not in months and not month.isdigit():
        return False

    day = int(day)
    year = int(year)

    if day < 1 or day > 31:
        return False

    if month.isdigit():
        month = int(month)
        if month < 1 or month > 12:
            return False

    return True

def convert_to_iso_date(date_str):
    parts = date_str.split()
    day, month, year = parts

    if month.isdigit():
        month = int(month)
    else:
        month = months.index(month.lower()) + 1

    iso_date = "{:04d}-{:02d}-{:02d}".format(int(year), month, int(day))
    return iso_date

def main():
    line_number = 1
    while True:
        try:
            date = input("Дата: ")
            if is_valid_date(date):
                iso_date = convert_to_iso_date(date)
                print(f"{line_number} строка: Дата: Дата: {iso_date}")
                line_number += 1
                break
            else:
                print(f"{line_number} строка: Дата: Неправильный формат даты. Попробуйте снова.")
                line_number += 1
        except EOFError:
            break

if __name__ == "__main__":
    main()

