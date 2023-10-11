part1 = ["p'_0 > p''_0", "p'_0 \leq p''_0"]
part2 = ["p'_0 > p''_1", "p'_0 \leq p''_1"]
part3 = ["p'_1 > p''_0", "p'_1 \leq p''_0"]
part4 = ["p'_1 > p''_1", "p'_1 \leq p''_1"]

for p1 in part1:
    for p2 in part2:
        for p3 in part3:
            for p4 in part4:
                print(p1, ", ",p2, ", ",p3, ", ",p4)