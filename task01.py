import queue
import random
import time

# Створюємо чергу
requests_queue = queue.Queue()

# Функція для генерації нових заявок
def generate_request():
    request_id = random.randint(1000, 9999)  # Генеруємо унікальний номер заявки
    requests_queue.put(f"Заявка {request_id}")
    print(f"Нова заявка додана до черги: Заявка {request_id}")

# Функція для обробки заявок
def process_request():
    if not requests_queue.empty():
        request = requests_queue.get()
        print(f"Обробляється {request}")
        time.sleep(1)  # Імітація часу на обробку заявки
        print(f"{request} оброблено")
    else:
        print("Черга пуста. Немає заявок для обробки.")

# Основний цикл програми
def main():
    while True:
        action = input("\n1 - Створити заявку\n2 - Обробити заявку\n3 - Вийти\nОберіть дію: ")
        if action == '1':
            generate_request()
        elif action == '2':
            process_request()
        elif action == '3':
            print("Програма завершена.")
            break
        else:
            print("Невірна команда. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
