import pytest

def largestJoltage(pack: str) -> str:
    highest = pack[-2]
    second = pack[-1]
    for j in pack[-3::-1]:
        second = highest if j >= highest and highest > second else second
        highest = j if j > highest else highest
    return highest + second

def largerLargestJoltage(pack: str, size:int) -> str:
    if size == 1:
        return max(pack)
    else:
        j = pack.find(max(pack[:-size+1]))
        return pack[j] + largerLargestJoltage(pack[j+1:], size - 1)

def main():
    # Read the file
    with open('input/input_day3.txt','r') as f:
        lines = f.readlines()
    
    solution1 = 0
    solution1bis = 0
    solution2 = 0
    for pack in lines:
        solution1 += int(largestJoltage(pack[:-1]))
        solution1bis += int(largerLargestJoltage(pack[:-1], 2))
        solution2 += int(largerLargestJoltage(pack[:-1], 12))

    print(f'The solution for day3/part1 = { solution1}')    
    print(f'The solution for day3/part1 using generic algo = { solution1}')  
    print(f'The solution for day3/part2 = { solution2}')
 
if __name__=="__main__":
    main()

@pytest.mark.parametrize(
    "pack, expected_result",
    [
        ("987654321111111", "98"),
        ("811111111111119", "89"),
        ("234234234234278","78"),
        ("818181911112111","92"),
        ("1564299121512","99"),
        ("135165131389","89"),
        ("135165131398","98"),
    ],
)
def test_largestJoltage(pack, expected_result):
    assert largestJoltage(pack) == expected_result

@pytest.mark.parametrize(
    "pack, expected_result",
    [
        ("987654321111111", "987654321111"),
        ("811111111111119", "811111111119"),
        ("234234234234278","434234234278"),
        ("818181911112111","888911112111"),
        ("2222222353222142222221122722122222232221122115232121242211242252227251322225222222222231247222252252","777555555544")
    ],
)
def test_largerLargestJoltage(pack, expected_result):
    assert largerLargestJoltage(pack,12) == expected_result