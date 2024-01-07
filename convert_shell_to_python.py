import sys
from sh2py import ShParser

def convert_shell_to_python(shell_script_path):
    with open(shell_script_path, 'r') as shell_file:
        shell_script_content = shell_file.read()

    sh_parser = ShParser(shell_script_content)
    python_code = sh_parser.to_python()

    python_script_path = shell_script_path.replace('.sh', '_converted.py')

    with open(python_script_path, 'w') as python_file:
        python_file.write(python_code)

    print(f"Conversion successful. Python script saved to {python_script_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert_shell_to_python.py <shell_script_path>")
        sys.exit(1)

    shell_script_path = sys.argv[1]
    convert_shell_to_python(shell_script_path)
