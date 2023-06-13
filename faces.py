def convert(s):
    if ":)" in s:
        s = s.replace(":)", "\N{Slightly Smiling Face}")
    if ":(" in s:
        s = s.replace(":(", "\N{Slightly Frowning Face}")
    return s
s = str(input())
def main():
    print(convert(s))
main()