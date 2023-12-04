from collections import defaultdict

file = "data.txt"
with open(file) as f:
    content = f.readlines()

winning_nrs = []
elf_nrs = []
saved = defaultdict(int)

for i, line in enumerate(content):
    saved[i] += 1
    parts = line.split(':')
    nrs_before = parts[1].split('|')[0]
    nrs_after = parts[1].split('|')[1]

    winning_nrs = [int(nr) for nr in nrs_before.split()]
    elf_nrs = [int(nr) for nr in nrs_after.split()]

    print(winning_nrs, elf_nrs)

    winning_set = set(winning_nrs)
    elf_set = set(elf_nrs)

    matching_nrs = winning_set.intersection(elf_set)
    num_matching = len(matching_nrs)

    print(num_matching)

    for j in range(num_matching):
        saved[i + 1 + j] += saved[i]

print(sum(saved.values()))