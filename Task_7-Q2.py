def read_text(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            print(f"Content of '{file_name}':\n")
            print(content)
    except FileNotFoundError:
        print("Not able to read the text file")

file_name = "requirement.txt"
read_text(file_name)
