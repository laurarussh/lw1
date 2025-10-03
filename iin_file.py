import hashlib

iin = "041006651442"

def find_hash_with_prefix(prefix, max_attempts=1000000):
    for i in range(max_attempts):
        input_str = f"{iin}+{i}"
        hash_val = hashlib.sha256(input_str.encode()).hexdigest()
        if hash_val.startswith(prefix):
            print(f"Найдено!\nВход: {input_str}\nХэш: {hash_val}")
            return
    print(f"Не найдено хэша с префиксом {prefix} за {max_attempts} попыток.")

print("Поиск хэша с двумя нулями:")
find_hash_with_prefix("00")

print("\nПоиск хэша с тремя нулями:")
find_hash_with_prefix("000")
