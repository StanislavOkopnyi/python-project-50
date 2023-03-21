from gendiff.formatters.plain import make_plain
from gendiff.formatters.json import make_json
from gendiff.settings import args
from gendiff import generate_diff


def main():
    if args.format == "make_plain":
        difference = generate_diff(args.first_file, args.second_file,
                                   make_plain)
        print(difference)
    elif args.format == "json":
        difference = generate_diff(args.first_file, args.second_file,
                                   make_json)
        print(difference)
    else:
        difference = generate_diff(args.first_file, args.second_file)
        print(difference)


if __name__ == "__main__":
    main()
