file = "data.txt"
with open(file) as f:
    content = f.readlines()

winning_nrs = []
elf_nrs = []

sumOfall = 0

for line in content:
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

    if num_matching >= 1:
        sumOfpowers = 2**(num_matching-1)
    else:
        sumOfpowers = 0

    sumOfall = sumOfall + sumOfpowers

    print(num_matching)
    print(sumOfpowers)
    print(sumOfall)