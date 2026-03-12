import os

def print_tree(root, indent=""):
    exclude = {".git", "node_modules", ".DS_Store", "__pycache__", "dist", ".vite"}
    
    if os.path.basename(root) in exclude:
        return

    items = sorted([i for i in os.listdir(root) if i not in exclude and not i.endswith(".py")])
    
    for i, item in enumerate(items):
        path = os.path.join(root, item)
        is_last = (i == len(items) - 1)
        
        marker = "└── " if is_last else "├── "
        
        print(f"{indent}{marker}{item}")
        
        if os.path.isdir(path):
            extension = "    " if is_last else "│   "
            print_tree(path, indent + extension)

def main():
    print(os.path.basename(os.getcwd()))
    print_tree(".")

if __name__ == '__main__':
    main()