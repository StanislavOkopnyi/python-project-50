from gendiff.cli import args
from gendiff import generate_diff


def main():
    difference = generate_diff(args.first_file, args.second_file,
                               args.format)
    print(difference)


if __name__ == "__main__":
    main()
