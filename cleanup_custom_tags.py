import os
import re

# List of custom tags to remove or convert
CUSTOM_TAGS = [
    "Card", "CardGroup", "Accordion", "AccordionGroup", "Note", "Warning", "Tip", "Check", "Steps"
]

def convert_card_to_md(line):
    # Convert <Card title="..." href="...">Text</Card> to - [Title](href): Text
    card_open = re.match(r'<Card\s+title="([^"]+)"\s+icon="[^"]*"\s+href="([^"]+)"\s*>', line)
    if card_open:
        title, href = card_open.groups()
        return f'- [{title}]({href}): '
    return None

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    inside_tag = None
    for line in lines:
        # Remove import lines for custom components
        if line.strip().startswith('import ') and any(tag in line for tag in CUSTOM_TAGS):
            continue

        # Convert <Card ...> to Markdown link
        if '<Card ' in line:
            converted = convert_card_to_md(line)
            if converted is not None:
                inside_tag = 'Card'
                new_lines.append(converted)
                continue

        # Remove opening tags for other custom components
        for tag in CUSTOM_TAGS:
            open_tag = f'<{tag}'
            close_tag = f'</{tag}>'
            if open_tag in line:
                inside_tag = tag
                # For non-Card tags, just skip the tag and keep the content
                if tag != 'Card':
                    continue
            if close_tag in line:
                inside_tag = None
                continue

        # If inside a custom tag, keep the content (for Card, append to previous line)
        if inside_tag:
            if inside_tag == 'Card':
                # Append content to last line
                if new_lines:
                    new_lines[-1] += line.strip() + '\n'
                continue
            else:
                # For other tags, just keep the content
                new_lines.append(line)
                continue

        # Remove self-closing custom tags
        if any(f'<{tag} ' in line and '/>' in line for tag in CUSTOM_TAGS):
            continue

        new_lines.append(line)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"Cleaned: {filepath}")

def main():
    for root, dirs, files in os.walk('docs'):
        for file in files:
            if file.endswith('.md'):
                clean_file(os.path.join(root, file))

if __name__ == '__main__':
    main()
