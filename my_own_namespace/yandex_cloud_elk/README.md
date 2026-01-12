# yandex_cloud_elk Collection

Collection for creating and managing text files in Ansible.

## Modules

### create_file
Creates a text file with specified content.

**Parameters:**
- `path` (required): Path to the file
- `content` (optional): File content (default: '')
- `mode` (optional): File permissions (default: '0644')

## Installation

\`\`\`bash
ansible-galaxy collection install my_own_namespace.yandex_cloud_elk
\`\`\`

## Usage

\`\`\`yaml
- name: Create a file
  my_own_namespace.yandex_cloud_elk.create_file:
    path: "/tmp/test.txt"
    content: "Hello World"
    mode: '0644'
\`\`\`

## License

GPL-3.0-or-later
