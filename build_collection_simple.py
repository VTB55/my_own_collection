#!/usr/bin/env python3
import os
import tarfile

print("=" * 60)
print("Сборка Ansible Collection")
print("=" * 60)

collection_dir = "my_own_namespace/yandex_cloud_elk"
output_file = "my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz"

print(f"\nДиректория collection: {collection_dir}")
print(f"Выходной файл: {output_file}")

# Создаем архив
with tarfile.open(output_file, "w:gz") as tar:
    for root, dirs, files in os.walk(collection_dir):
        for file in files:
            full_path = os.path.join(root, file)
            arcname = full_path  # Используем полный путь
            tar.add(full_path, arcname=arcname)
            print(f"Добавлен: {file}")

print(f"\n✅ Collection собрана: {output_file}")
print(f"Размер: {os.path.getsize(output_file)} байт")
print("=" * 60)
