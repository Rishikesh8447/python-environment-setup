import sys
from pathlib import Path


GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"


def check_python_version():
    version = (
        f"{sys.version_info.major}."
        f"{sys.version_info.minor}."
        f"{sys.version_info.micro}"
    )

    print(f"{GREEN}✓ Python version: {version}{RESET}")

    if sys.version_info >= (3, 8):
        print(
            f"{GREEN}"
            f"✓ Python version requirement satisfied"
            f"{RESET}"
        )
        return True

    print(
        f"{RED}"
        f"✗ Python 3.8 or higher is required"
        f"{RESET}"
    )

    return False


def create_directories(project_dir):
    directories = ["src", "tests", "docs", "logs"]

    for directory in directories:
        directory_path = project_dir / directory

        directory_path.mkdir(
            parents=True,
            exist_ok=True
        )

        print(
            f"{GREEN}"
            f"✓ Created directory: {directory}"
            f"{RESET}"
        )


def create_requirements_file(project_dir):
    requirements_file = project_dir / "requirements.txt"

    requirements_file.write_text(
        "requests\n"
        "pytest\n"
    )

    print(f"{GREEN}✓ Created requirements.txt{RESET}")


def create_gitignore(project_dir):
    gitignore_file = project_dir / ".gitignore"

    gitignore_file.write_text(
        "__pycache__/\n"
        "*.py[cod]\n"
        "venv/\n"
        ".env\n"
        ".pytest_cache/\n"
    )

    print(f"{GREEN}✓ Created .gitignore{RESET}")


def main():
    try:
        if not check_python_version():
            return

        project_dir = Path.cwd()

        create_directories(project_dir)
        create_requirements_file(project_dir)
        create_gitignore(project_dir)
        print(f"{GREEN}✓ Project setup completed successfully!{RESET}")

    except OSError as error:
        print(f"{RED}✗ Setup failed: {error}{RESET}")


if __name__ == "__main__":
    main()