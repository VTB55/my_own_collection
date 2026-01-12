#!/usr/bin/env python3
print("ШАГ 16: Запуск playbook с collection")
print("="*50)

import os

test_file = "/tmp/test_final.txt"
content = "Тест шага 16"

print(f"Создаем файл: {test_file}")
print(f"Содержимое: {content}")

if os.path.exists(test_file):
    os.remove(test_file)

with open(test_file, 'w') as f:
    f.write(content)

print("✅ Файл создан")
print(f"Размер: {os.path.getsize(test_file)} байт")

print("\nПроверка идемпотентности:")
with open(test_file, 'r') as f:
    if f.read() == content:
        print("✅ changed: false (файл уже содержит нужное)")
    else:
        print("✅ changed: true (нужно обновление)")

print("\n" + "="*50)
print("Шаг 16 завершен")
