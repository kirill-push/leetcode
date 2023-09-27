import subprocess


def main():
    # Выполнение первой команды: poetry run black .
    subprocess.run(["poetry", "run", "black", "."], check=True)

    # Выполнение второй команды: poetry run isort .
    subprocess.run(["poetry", "run", "isort", "."], check=True)


if __name__ == "__main__":
    main()
