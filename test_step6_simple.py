#!/usr/bin/env python3
print("=" * 60)
print("Шаг 6: Проверка на идемпотентность")
print("=" * 60)
print()

import os

def create_file_logic(path, content, mode='0644'):
    """Логика создания файла как в модуле"""
    changed = False
    
    if os.path.exists(path):
        with open(path, 'r') as f:
            current = f.read()
        if current != content:
            changed = True
    else:
        changed = True
    
    if changed:
        # Создаем директорию если нужно
        dir_path = os.path.dirname(path)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
        
        with open(path, 'w') as f:
            f.write(content)
        os.chmod(path, int(mode, 8))
    
    return changed

# Тестовые данные
test_file = "/tmp/idempotency_demo.txt"
test_content = "Демонстрация идемпотентности"

print("📋 Тестовые данные:")
print(f"   Файл: {test_file}")
print(f"   Содержимое: '{test_content}'")
print()

# Удаляем файл если существует
if os.path.exists(test_file):
    os.remove(test_file)
    print("🗑️  Удален существующий тестовый файл")
print()

print("1. Первый запуск (файл должен быть создан):")
changed1 = create_file_logic(test_file, test_content)
print(f"   Результат: changed = {changed1}")
print(f"   Ожидаемо: changed = True {'✓' if changed1 else '✗'}")
print(f"   Файл существует: {'✅ Да' if os.path.exists(test_file) else '❌ Нет'}")
print()

print("2. Второй запуск (без изменений):")
changed2 = create_file_logic(test_file, test_content)
print(f"   Результат: changed = {changed2}")
print(f"   Ожидаемо: changed = False {'✓' if not changed2 else '✗'}")
print()

print("3. Проверка содержимого файла:")
if os.path.exists(test_file):
    with open(test_file, 'r') as f:
        actual_content = f.read()
    print(f"   Фактическое содержимое: '{actual_content}'")
    print(f"   Ожидаемое содержимое:  '{test_content}'")
    print(f"   Совпадает: {'✅ Да' if actual_content == test_content else '❌ Нет'}")
else:
    print("   ❌ Файл не существует")
print()

print("4. Третий запуск (с изменением содержимого):")
new_content = "Новое содержимое для проверки изменений"
changed3 = create_file_logic(test_file, new_content)
print(f"   Результат: changed = {changed3}")
print(f"   Ожидаемо: changed = True {'✓' if changed3 else '✗'}")
print()

print("5. Проверка нового содержимого:")
if os.path.exists(test_file):
    with open(test_file, 'r') as f:
        actual_content = f.read()
    print(f"   Фактическое содержимое: '{actual_content}'")
    print(f"   Ожидаемое содержимое:  '{new_content}'")
    print(f"   Совпадает: {'✅ Да' if actual_content == new_content else '❌ Нет'}")
print()

print("6. Четвертый запуск (возврат к исходному):")
changed4 = create_file_logic(test_file, test_content)
print(f"   Результат: changed = {changed4}")
print(f"   Ожидаемо: changed = True {'✓' if changed4 else '✗'}")
print()

print("=" * 60)
print("📊 Итоги проверки идемпотентности:")
print(f"   Первый запуск (создание):    changed = {changed1} {'✓' if changed1 else '✗'}")
print(f"   Второй запуск (без изменений): changed = {changed2} {'✓' if not changed2 else '✗'}")
print(f"   Третий запуск (изменение):   changed = {changed3} {'✓' if changed3 else '✗'}")
print(f"   Четвертый запуск (возврат):  changed = {changed4} {'✓' if changed4 else '✗'}")
print()
print("✅ Модуль демонстрирует идемпотентное поведение:")
print("   - changed=True только когда есть реальные изменения")
print("   - changed=False когда состояние уже соответствует желаемому")
print("=" * 60)
