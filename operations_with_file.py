import os


def read_file_as_bytes(file_path):
    with open(file_path, 'rb') as file:
        return bytearray(file.read())


def write_encrypted_data(file_path, encrypted_data):
    # Разделяем путь на основание и расширение
    base, _ = os.path.splitext(file_path)
    new_file_path = base + "_encrypted.txt"

    with open("" + new_file_path, "w") as file:
        file.write(encrypted_data)


def read_encrypted_data(file_path):
    _, ext = os.path.splitext(file_path)
    if ext != ".txt":
        return ""
    with open(file_path, 'r') as file:
        return file.read()


def write_bytes_to_file(file_path, bytes_data, extension):
    base, _ = os.path.splitext(file_path)
    with open(base[:-10] + "_decrypted" + extension, 'wb') as file:
        file.write(bytes_data)
