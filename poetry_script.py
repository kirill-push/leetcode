import subprocess


def main():
    # poetry run black .
    subprocess.run(["poetry", "run", "black", "."], check=True)

    # poetry run isort .
    subprocess.run(["poetry", "run", "isort", "."], check=True)


if __name__ == "__main__":
    main()
