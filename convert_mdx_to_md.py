import os
import re

def strip_jsx(content):
    # Remove single-line JSX tags like <Card ... /> or <Card>...</Card>
    # Remove multi-line JSX blocks
    # Remove import lines for components
    lines = content.splitlines()
    new_lines = []
    inside_jsx = False
    jsx_tag = None
    jsx_open = re.compile(r'^<([A-Z][A-Za-z0-9]*)\\b')
    jsx_close = re.compile(r'^</([A-Z][A-Za-z0-9]*)>')
    import_re = re.compile(r'^import .* from .*[\'"].*[\'"];?')
    for line in lines:
        if import_re.match(line.strip()):
            continue  # skip import lines
        if not inside_jsx:
            m = jsx_open.match(line.strip())
            if m:
                tag = m.group(1)
                if line.strip().endswith('/>'):
                    continue  # skip self-closing JSX
                if not line.strip().endswith('>'):
                    inside_jsx = True
                    jsx_tag = tag
                    continue
                # If it's an opening tag, check if it closes on the same line
                if f'</{tag}>' in line:
                    continue  # skip single-line open/close
                inside_jsx = True
                jsx_tag = tag
                continue
        else:
            # Inside a JSX block
            if jsx_close.match(line.strip()):
                inside_jsx = False
                jsx_tag = None
            continue
        new_lines.append(line)
    return '\n'.join(new_lines)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = strip_jsx(content)
    new_filepath = filepath[:-4] + '.md'
    with open(new_filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    os.remove(filepath)
    print(f"Converted: {filepath} -> {new_filepath}")

def main():
    for root, dirs, files in os.walk('docs'):
        for file in files:
            if file.endswith('.mdx'):
                process_file(os.path.join(root, file))

if __name__ == '__main__':
    main()
