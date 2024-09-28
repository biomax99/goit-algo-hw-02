from collections import deque

# Функція для перевірки, чи є рядок паліндромом
def is_palindrome(input_string):
    # Приведення рядка до нижнього регістру, видалення пробілів і неалфавітних символів
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())

    # Створюємо двосторонню чергу
    char_deque = deque(cleaned_string)

    # Перевіряємо символи з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Основний цикл програми для перевірки паліндромів
def main():
    input_string = input("Введіть рядок для перевірки на паліндром: ")
    if is_palindrome(input_string):
        print(f'"{input_string}" є паліндромом.')
    else:
        print(f'"{input_string}" не є паліндромом.')

if __name__ == "__main__":
    main()
