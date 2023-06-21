def feet2meter(v):
    v = v.replace("ft", "")
    return float(v) * 0.3048

def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

main()
