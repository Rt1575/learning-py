def write_and_count_lines(filename, lines):
    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")

    with open(filename, "r") as f:
        return len(f.readlines())
