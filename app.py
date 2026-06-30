import json

def load_data():
    with open("data.json", "r", encoding="utf-8") as f:
        return json.load(f)

def show_users(data):
    print("=== USERS ===")
    for user in data["users"]:
        print(f"ID: {user['id']}")
        print(f"ФИО: {user['full_name']}")
        print(f"Логин: {user['login']}")
        print(f"Телефон: {user['phone']}")
        print("-" * 20)

def show_devices(data):
    print("=== DEVICES ===")
    for device in data["devices"]:
        print(f"User ID: {device['user_id']}")
        print(f"Устройство: {device['device_name']}")
        print(f"Тип: {device['device_type']}")
        print(f"RAM: {device['characteristics']['ram']}")
        print(f"Storage: {device['characteristics']['storage']}")
        print("-" * 20)

def main():
    data = load_data()
    show_users(data)
    show_devices(data)

if __name__ == "__main__":
    main()
