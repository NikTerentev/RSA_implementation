import random
import math
import os
from sympy import randprime


class RSA:
    def __init__(self, number_of_digits):
        self.number_of_digits = number_of_digits

    def __generate_prime(self):
        min_value = 10 ** (self.number_of_digits // 2 - 1)
        max_value = (10 ** (self.number_of_digits // 2)) - 1
        return randprime(min_value, max_value)

    def key_gen(self):
        P = self.__generate_prime()
        Q = self.__generate_prime()
        N = P * Q

        print(f"P = {P}")
        print(f"Q = {Q}")

        phi_n = (P - 1) * (Q - 1)

        s = random.randint(3, phi_n - 1)
        while math.gcd(s, phi_n) != 1:
            s = random.randint(3, phi_n - 1)

        e = pow(s, -1, phi_n)

        return (s, N), (e, N)

    @staticmethod
    def encrypt(data, primary_key, type_of_data):
        key, N = primary_key

        if type_of_data == 'str':
            # Преобразуем текст в байты с помощью кодировки UTF-8
            message_bytes = data.encode('utf-8')
            # Преобразуем байты в число
            message_number = int.from_bytes(message_bytes, 'big')
            # Определяем размер блока в битах
            block_size = N.bit_length() - 1
            # Создаем маску для извлечения блоков
            mask = (1 << block_size) - 1
            # Создаем список для хранения зашифрованных блоков
            encrypted_blocks = []
            # Пока число не станет нулем
            while message_number > 0:
                # Извлекаем очередной блок с помощью маски
                block = message_number & mask
                # Сдвигаем число вправо на размер блока
                message_number >>= block_size
                # Зашифровываем блок с помощью публичного ключа RSA
                encrypted_block = pow(block, key, N)
                # Добавляем зашифрованный блок в список
                encrypted_blocks.append(encrypted_block)
            # Возвращаем список зашифрованных блоков
            return encrypted_blocks

        elif type_of_data == "file":
            # Открываем файл в бинарном режиме для чтения
            with open(data, "rb") as f:
                # Определяем размер блока в байтах
                block_size = (N.bit_length() - 1) // 8
                #print(block_size)
                sum = 0
                original_len_last_block = 0
                base, ext = os.path.splitext(data)
                new_file_path = base + ext + "_encrypted.bin"

                # Открываем файл для записи зашифрованных блоков
                with open(new_file_path, "wb") as out_f:
                    # Считываем файл по блокам
                    block = f.read(block_size)
                    #print(block)
                    #print(f"block len = {len(block)}")

                    while block:
                        # Если блок меньше block_size, дополняем его нулевыми байтами
                        if len(block) < block_size:
                            original_len_last_block = len(block)
                            block = block.ljust(block_size, b'\x00')

                        # Преобразуем блок в число
                        block_number = int.from_bytes(block, "big")
                        # Зашифровываем блок с помощью публичного ключа RSA
                        encrypted_block = pow(block_number, key, N)

                        encrypted_block_bytes = encrypted_block.to_bytes(
                            block_size + 1, 'big')
                        #print(f"encrypted_block_len = {len(encrypted_block_bytes)}")
                        sum += len(encrypted_block_bytes)
                        #print(sum)
                        # Записываем зашифрованный блок в файл
                        out_f.write(encrypted_block_bytes)
                        # Считываем следующий блок
                        next_block = f.read(block_size)

                        # Если это последний блок, записываем его размер в конец файла
                        if not next_block:
                            out_f.write(original_len_last_block.to_bytes(1, 'big'))

                        block = next_block
                        #print(block)
                        #print(f"block len = {len(block)}")

            return ""

    @staticmethod
    def decrypt(data, primary_key, type_of_data):
        key, N = primary_key
        if type_of_data == "str":

            # Создаем список для хранения расшифрованных блоков
            decrypted_blocks = []
            # Для каждого зашифрованного блока в списке
            for encrypted_block in data:
                # Расшифровываем блок с помощью секретного ключа RSA
                decrypted_block = pow(int(encrypted_block), key, N)
                # Добавляем расшифрованный блок в список
                decrypted_blocks.append(decrypted_block)

            # Определяем размер блока в битах
            block_size = N.bit_length() - 1

            # Создаем переменную для хранения числа, которое представляет текст
            message_number = 0

            # Для каждого расшифрованного блока в обратном порядке списка
            for decrypted_block in reversed(decrypted_blocks):
                # Сдвигаем число влево на размер блока и добавляем очередной блок с помощью побитового ИЛИ
                message_number = (
                                         message_number << block_size) | decrypted_block

            # Преобразуем число в байты
            message_bytes = message_number.to_bytes(
                message_number.bit_length() // 8 + 1, 'big').lstrip(b'\x00')

            # Преобразуем байты в текст с помощью кодировки UTF-8
            message_text = message_bytes.decode('utf-8')

            # Возвращаем текст
            return message_text


        elif type_of_data == "file":
            block_size = (N.bit_length() - 1) // 8
            original_file_path = data.rpartition('_')[0]
            base, ext = os.path.splitext(original_file_path)
            new_file_path = base + "_decrypted" + ext

            # Открываем файл в бинарном режиме для записи
            with open(new_file_path, "wb") as out_f:

                # Открываем файл в бинарном режиме для чтения
                with open(data, 'rb') as f:

                    # Считываем и обрабатываем файл по блокам
                    while True:

                        # Считываем блок байтов
                        encrypted_block = f.read(block_size + 1)

                        if len(encrypted_block) == 1:
                            last_block_size = int.from_bytes(encrypted_block, 'big')
                            #print(f"last_block_size = {last_block_size}")
                            break
                        #print(f"encrypted_block = {encrypted_block}")
                        #print(len(encrypted_block))
                        # Удаляем все нулевые байты с начала и конца блока
                        #encrypted_block = encrypted_block.rstrip(b'\x00')
                        #print(len(encrypted_block))
                        #print(f"encrypted_block_changed = {encrypted_block}")
                        # Преобразуем блок в число
                        encrypted_block = int.from_bytes(encrypted_block, 'big')

                        # Расшифровываем блок с помощью секретного ключа RSA
                        decrypted_block = pow(encrypted_block, key, N)
                        #print(f"decrypted_block = {decrypted_block}")
                        # Преобразуем блок в байты
                        block = decrypted_block.to_bytes(block_size, "big")
                        #print(block)

                        out_f.write(block)

            # Обрезаем последний блок до его исходного размера
            with open(new_file_path, "rb+") as f:
                f.seek(-(block_size - last_block_size), 2)
                f.truncate()
            return ""
