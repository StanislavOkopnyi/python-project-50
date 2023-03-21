from gendiff.plain import plain
from gendiff.settings import args
from gendiff import generate_diff


def main():
    if args.format == "plain":
        difference = generate_diff(args.first_file, args.second_file, plain)
        print(difference)
    else:
        difference = generate_diff(args.first_file, args.second_file)
        print(difference)


if __name__ == "__main__":
    main()
