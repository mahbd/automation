import os

directory = "E:\\flutter\\book_store\\lib"

sub_dirs = [x[0] for x in os.walk(directory)]
all_files = []
for sub_dir in sub_dirs:
    all_files.extend([os.path.join(sub_dir, f) for f in os.listdir(sub_dir)])

total_lines = 0
total_words = 0
total_chars = 0
for file in all_files:
    if file.endswith(".py") or file.endswith(".txt") or file.endswith(".dart"):
        line_here = sum(1 for line in open(file))
        words_here = len(open(file).read().split())
        chars_here = sum(len(line) for line in open(file))
        total_lines += sum(1 for line in open(file))
        total_words += len(open(file).read().split())
        total_chars += sum(len(line) for line in open(file))
        # Output file name line count, word count, and char count
        file_name = file.split("\\")[-1]
        lines = f"{line_here} lines".ljust(12)
        words = f"{words_here} words".ljust(14)
        chars = f"{chars_here} chars".ljust(18)
        print(f"{file_name.ljust(35)} has {lines} {words} {chars}")
print("Summary\n--------------------------------")
print(f"There are {len(all_files)} files in {directory}")
print(f"There are {total_lines} lines in {directory}")
print(f"There are {total_words} words in {directory}")
print(f"There are {total_chars} characters in {directory}")
