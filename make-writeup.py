import argparse
import os

Author = "barrythecanary"

def create_markdown(author, title, category, difficulty, path):
    filename = f"{title}.md"
    full_path = os.path.join(path, filename)

    if os.path.exists(full_path):
        overwrite = input(f"File '{full_path}' already exists. Overwrite? (y/n): ").strip().lower()
        if overwrite != 'y':
            print("Operation cancelled.")
            exit(0)

    content = f"""# {title} - Writeup

| Author           | Title             | Category   | Difficulty |
|------------------|-------------------|------------|------------|
| {author} | {title} | {category} | {difficulty} |

## Description

## Solution
"""

    with open(full_path, 'w') as f:
        f.write(content)
    print(f"Writeup '{full_path}' created successfully.")

def main():
    parser = argparse.ArgumentParser(description="Create a markdown writeup.")
    parser.add_argument('-a', '--author', required=False, default=Author, help='Author name')
    parser.add_argument('-t', '--title', required=True, help='Title of the writeup')
    parser.add_argument('-c', '--category', required=True, help='Category')
    parser.add_argument('-d', '--difficulty', required=False, default='-', help='Difficulty')
    parser.add_argument('-p', '--path', default='.', help='Directory path to save the file (default: current directory)')

    args = parser.parse_args()

    create_markdown(args.author, args.title, args.category, args.difficulty, args.path)

if __name__ == "__main__":
    main()
