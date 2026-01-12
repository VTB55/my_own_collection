#!/usr/bin/python3

DOCUMENTATION = '''
---
module: create_file
short_description: Creates a text file with specified content
version_added: "1.0.0"
description:
  - This module creates a text file at the specified path with given content.
options:
  path:
    description:
      - Path where the file should be created
    required: true
    type: path
  content:
    description:
      - Content to write to the file
    required: false
    type: str
    default: ''
  mode:
    description:
      - Permissions of the created file (in octal)
    required: false
    type: str
    default: '0644'
author:
  - VTB55
'''

EXAMPLES = '''
# Create a simple file
- name: Create a test file
  create_file:
    path: /tmp/test.txt
    content: "Hello World!"
    mode: '0644'
'''

RETURN = '''
path:
  description: Path of the created/modified file
  type: str
  returned: always
  sample: '/tmp/test.txt'
content:
  description: Content written to the file
  type: str
  returned: always
  sample: 'Hello World!'
changed:
  description: Whether the file was changed
  type: bool
  returned: always
'''

import os
import json
import sys

def main():
    # Читаем аргументы из stdin (как это делает Ansible)
    if len(sys.argv) > 1 and sys.argv[1] == '--check-syntax':
        print("Syntax OK")
        sys.exit(0)
    
    # Читаем входные данные
    input_data = sys.stdin.read()
    try:
        args = json.loads(input_data)
        module_args = args.get('ANSIBLE_MODULE_ARGS', {})
    except:
        module_args = {}
    
    # Получаем параметры
    path = module_args.get('path', '')
    content = module_args.get('content', '')
    mode = module_args.get('mode', '0644')
    
    # Проверяем обязательные параметры
    if not path:
        result = {
            'failed': True,
            'msg': 'Parameter "path" is required'
        }
        print(json.dumps(result))
        sys.exit(1)
    
    # Проверяем текущее состояние
    changed = False
    if os.path.exists(path):
        with open(path, 'r') as f:
            current_content = f.read()
        if current_content != content:
            changed = True
    else:
        changed = True
    
    # Если в режиме проверки, просто возвращаем результат
    if 'check_mode' in args:
        result = {
            'changed': changed,
            'path': path,
            'content': content
        }
        print(json.dumps(result))
        sys.exit(0)
    
    # Реальный режим - создаем/изменяем файл
    if changed:
        # Создаем директорию если нужно
        dir_path = os.path.dirname(path)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
        
        # Создаем файл
        with open(path, 'w') as f:
            f.write(content)
        
        # Устанавливаем права
        os.chmod(path, int(mode, 8))
    
    # Возвращаем результат
    result = {
        'changed': changed,
        'path': path,
        'content': content
    }
    
    print(json.dumps(result))

if __name__ == '__main__':
    main()
