import sys

DATABASE_PATH = "naves.csv"

if "pytest" in sys.argv[0]:
    DATABASE_PATH = "tests/naves_test.csv"