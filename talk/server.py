import socket
import threading


# IP-адреса сервера
# 0.0.0.0 означає:
# "приймати підключення з усіх мережевих інтерфейсів цього ПК"
HOST = "0.0.0.0"

# Порт, через який працюватиме чат
PORT = 5000


# Тут зберігатимемо всіх підключених клієнтів
clients = []


# Відправляємо повідомлення всім підключеним клієнтам
def broadcast(message, sender):
    for client in clients:
        # Не відправляємо повідомлення назад тому,
        # хто його надіслав

            try:
                client.send(message)

            except:
                # Якщо клієнт від'єднався
                if client in clients:
                    clients.remove(client)


# Робота з одним конкретним клієнтом
def handle_client(client, address):
    print(f"Підключився клієнт: {address}")

    while True:
        try:
            # Чекаємо повідомлення від клієнта
            message = client.recv(1024)

            # Якщо повідомлення порожнє,
            # клієнт від'єднався
            if not message:
                break

            # Показуємо повідомлення на сервері
            print(message.decode())

            # Передаємо повідомлення іншим клієнтам
            broadcast(message, client)

        except:
            break

    # Клієнт від'єднався
    if client in clients:
        clients.remove(client)

    client.close()

    print(f"Клієнт від'єднався: {address}")


# Створюємо серверний socket
server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)


# Дозволяємо повторно використовувати порт
server.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_REUSEADDR,
    1
)


# Прив'язуємо сервер до IP та порту
server.bind((HOST, PORT))


# Починаємо слухати підключення
server.listen()


print("==============================")
print("     ЛОКАЛЬНИЙ ЧАТ")
print("==============================")
print(f"Сервер запущено на порту {PORT}")
print("Очікування підключень...")


# Постійно чекаємо нових клієнтів
while True:

    # Очікуємо підключення
    client, address = server.accept()

    # Додаємо клієнта до списку
    clients.append(client)

    # Для кожного клієнта створюємо окремий потік
    thread = threading.Thread(
        target=handle_client,
        args=(client, address)
    )

    thread.start()