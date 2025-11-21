def bits_range(string: str, start: int, end: int) -> str:
    bits = ""
    for idx in range(start, end):
        bits += string[idx % len(string)]
    return bits


def box(box_idx: int, block: str) -> str:
    boxes = {
        1: [
            ["101", "010", "001", "110", "011", "100", "111", "000"],
            ["001", "100", "110", "010", "000", "111", "101", "011"]
        ],
        2: [
            ["100", "000", "110", "101", "111", "001", "011", "010"],
            ["101", "011", "000", "111", "110", "010", "001", "100"]
        ]
    }

    chosen_box = boxes[box_idx]
    row = int(block[0])
    column = int(block[1:], 2)
    return chosen_box[row][column]


def expand_block(block: str) -> str:
    return block[0:2] + (block[3:1:-1] * 2) + block[4:6]


def split_block(block: str) -> tuple[str, str]:
    half = len(block) // 2
    return block[:half], block[half:]


def xor(a: str, b: str, bits: int) -> str:
    result = int(a, 2) ^ int(b, 2)
    return f"{result:0{bits}b}"
