#!/usr/bin/env python3
print("=" * 70)
print("ШАГ 15: Установка collection из локального архива")
print("=" * 70)
print()

import os

archive = "my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz"

if os.path.exists(archive):
    print(f"✅ Архив найден: {archive}")
    print(f"📊 Размер: {os.path.getsize(archive)} байт")
else:
    print(f"❌ Архив не найден")
    exit(1)

print()
print("Команда для установки:")
print(f"ansible-galaxy collection install {archive}")
print()
print("После установки collection будет доступна в:")
print("~/.ansible/collections/ansible_collections/my_own_namespace/yandex_cloud_elk/")
print()
print("Содержимое collection:")
print("- my_own_namespace/yandex_cloud_elk/galaxy.yml")
print("- my_own_namespace/yandex_cloud_elk/README.md")
print("- my_own_namespace/yandex_cloud_elk/plugins/modules/create_file.py")
print("- my_own_namespace/yandex_cloud_elk/roles/create_file_role/tasks/main.yml")
print("- my_own_namespace/yandex_cloud_elk/roles/create_file_role/defaults/main.yml")
print("- my_own_namespace/yandex_cloud_elk/playbooks/site.yml")
print()
print("=" * 70)
print("✅ Collection готова к установке")
print("=" * 70)
