from base64 import b64decode
from collections import Counter
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits

__all__ = [
    "ascii_alphanumeric",
    "ascii_letters",
    "ascii_lowercase",
    "ascii_uppercase",
    "ascii_to_binary",
    "base64_decode",
    "binary_to_ascii",
    "digits",
    "hex_to_bytes",
    "literal_to_binary_str",
    "morse_to_ascii",
    "most_freq_char",
    "xor_bytes"
]

ascii_alphanumeric = ascii_letters + digits


def ascii_to_binary(ascii_str: str) -> str:
    return "".join(f"{ord(char):08b}" for char in ascii_str)


def base64_decode(base64_str: str) -> bytes:
    return b64decode(base64_str.encode("ascii"))


def binary_to_ascii(binary_str: str) -> str:
    return (int(binary_str, 2)
            .to_bytes(len(binary_str) // 8)
            .decode("ascii"))


def hex_to_bytes(hex_str: str) -> bytes:
    return (int(hex_str, 16)
            .to_bytes(len(hex_str) // 2))


def literal_to_binary_str(binary_str: str) -> str:
    return (binary_str
            .replace(" ", "")
            .replace("ZERO", "0")
            .replace("ONE", "1"))


def morse_to_ascii(morse_str: str) -> str:
    morse_code_dict = {
        '.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..': 'D',
        '.': 'E',
        '..-.': 'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---': 'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '-----': '0',
        '--..--': ',',
        '.-.-.-': '.',
        '..--..': '?',
        '-..-.': '/',
        '-....-': '-',
        '-.--.': '(',
        '-.--.-': ')'
    }

    ascii_string = ""
    for character in morse_str.split(" "):
        ascii_string += morse_code_dict[character]
    return ascii_string


def most_freq_char(string: bytes) -> int:
    # Counter treats bytes like integers
    return Counter(string).most_common()[0][0]


def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes([a ^ b for a, b in zip(a, b)])
