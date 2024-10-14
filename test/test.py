#!/usr/bin/env python3
import os
import subprocess
import glob
import argparse

# Constants
PROBLEM_NAME = os.path.basename(os.getcwd())
DEBUG = True
LANG = "cpp"

# Set targets and commands based on language
if LANG == "cpp":
    TARGET = PROBLEM_NAME
    EXECUTE = f"./{TARGET}.out"
    CLEAN_TARGETS = [TARGET]
elif LANG == "python":
    TARGET = f"{PROBLEM_NAME}.py"
    EXECUTE = f"python3 ./{TARGET}"
    CLEAN_TARGETS = []
else:
    raise ValueError(
        "Unknown language; please set TARGET, EXECUTE, and CLEAN_TARGETS manually"
    )

CXX = "g++"
CXXFLAGS = "-std=c++23 -I/home/mahad/cplib/ -Wall -Wextra -pedantic -Wshadow -Wformat=2 -Wfloat-equal -Wconversion -Wlogical-op -Wshift-overflow=2 -Wduplicated-cond -Wcast-qual -Wcast-align -Wno-unused-result -Wno-sign-conversion -Wsign-conversion"
DEBUG_CXXFLAGS = "-fsanitize=address -fsanitize=undefined -fsanitize=float-divide-by-zero -fsanitize=float-cast-overflow -fno-sanitize-recover=all -fstack-protector-all -D_FORTIFY_SOURCE=2 -D_GLIBCXX_DEBUG -D_GLIBCXX_DEBUG_PEDANTIC -DMAHAD_DEBUG"

if DEBUG:
    CXXFLAGS += " " + DEBUG_CXXFLAGS


def compile_cpp():
    source_file = f"{PROBLEM_NAME}.cpp"
    command = f"{CXX} {CXXFLAGS} {source_file} -o {TARGET}.out"
    subprocess.run(command, shell=True, check=True)


def clean():
    for target in CLEAN_TARGETS:
        if os.path.exists(f"{target}.out"):
            os.remove(f"{target}.out")
        elif os.path.exists(target):
            os.remove(target)


def veryclean():
    clean()
    for res_file in glob.glob("*.result"):
        os.remove(res_file)


def run():
    if LANG == "cpp":
        compile_cpp()
    subprocess.run(f"time -p {EXECUTE}", shell=True)
    if DEBUG:
        print("Built with DEBUG flags enabled, code may be slower than normal")


def run_tests():
    cases = sorted(glob.glob("*.in"))
    for case in cases:
        base = os.path.splitext(case)[0]
        res_file = f"{base}.result"
        with open(case, "r") as infile, open(res_file, "w") as outfile:
            subprocess.run(f"time {EXECUTE}", stdin=infile, stdout=outfile, shell=True)
        if DEBUG:
            print("Built with DEBUG flags enabled, code may be slower than normal")


def test():
    # from the current directory, get all the input and output files
    cases = sorted(glob.glob("*.in"))
    outs = sorted(glob.glob("*.output"))
    tests = [os.path.splitext(case)[0] for case in cases]

    # compile the cpp file
    compile_cpp()
    for test_case in tests:
        print(f"Running test case {test_case}...\n")
        subprocess.run(
            f"time -p {EXECUTE} < {test_case}.in > {test_case}.result",
            shell=True,
            text=True,
        )
        res_file = f"{test_case}.result"
        out_file = f"{test_case}.output"
        subprocess.run(f"diff --color='auto' {res_file} {out_file}", shell=True)


def main():
    parser = argparse.ArgumentParser(description="Build and test automation script")
    parser.add_argument(
        "command",
        choices=["clean", "veryclean", "run", "test"],
        help="Command to execute",
    )
    args = parser.parse_args()

    command = args.command
    print(f"Running command: {command}")
    if command == "clean":
        clean()
    elif command == "veryclean":
        veryclean()
    elif command == "run":
        run()
    elif command == "test":
        test()


if __name__ == "__main__":
    main()
