from gendiff.indentations import COMMON


def stylish(source: str) -> str:
    source_list = source.split("\n")

    indentation = " " * 2
    for index, string in enumerate(source_list[1:-1], start=1):

        if string[-1] == "}":
            indentation = indentation[:-4]
            source_list[index] = indentation + COMMON + string
            continue

        source_list[index] = indentation + string

        if string[-1] == "{":
            indentation += " " * 4

    return "\n".join(source_list)
