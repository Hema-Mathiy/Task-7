import datetime

def create_timestamp():
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_name = f"{current_timestamp}.txt"
    file_name = file_name.replace(":", "-")

    with open(file_name, "w") as file:
        file.write(current_timestamp)

    print(f"File '{file_name}' created with the current_timestamp.")

create_timestamp()