import argparse
import os


def create_problem_files(problem_number, force):
    src_dir = os.path.join("src", "leetcode")
    tests_dir = "tests"

    # Create file with problem in src/leetcode
    problem_filename = f"problem_{problem_number}.py"
    problem_path = os.path.join(src_dir, problem_filename)

    if not force and os.path.isfile(problem_path):
        print(
            f"File {problem_path} already exists. \
To overwrite, use the -f option."
        )
    else:
        with open(problem_path, "w") as problem_file:
            problem_file.write("")

        print(f"Created file {problem_path}")

    # Create file with test in tests
    test_filename = f"test_{problem_number}.py"
    test_path = os.path.join(tests_dir, test_filename)

    if not force and os.path.isfile(test_path):
        print(
            f"File {test_path} already exists. To overwrite, use the -f option."
        )
    else:
        with open(test_path, "w") as test_file:
            test_file.write("import pytest\n\n")
            test_file.write(
                f"from leetcode.problem_{problem_number} import Solution\n\n"
            )
            test_file.write("test_data = [\n")
            test_file.write("    (),\n]\n\n\n")
            test_file.write(
                '@pytest.mark.parametrize("___, expected", test_data)\n'
            )
            test_file.write("def test(___, expected):\n")
            test_file.write("    assert Solution().____(___) == expected\n")

        print(f"Created file {test_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Create files with problem and test for LeetCode"
    )
    parser.add_argument("problem_number", type=int, help="Problem number")
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Overwrite files if they already exist",
    )

    args = parser.parse_args()

    create_problem_files(args.problem_number, args.force)


if __name__ == "__main__":
    main()
