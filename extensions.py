def main():
    file_name = input("File name: ")

    if file_name.lower() == "hello.jpg":
        print("image/jpeg")
    elif file_name.lower() == "document.pdf":
        print("application/pdf")
    else:
        print("application/octet-stream")
main()
