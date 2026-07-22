import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    octet = r"(0|[1-9]\d{0,2})"
    match = re.fullmatch(rf"{octet}\.{octet}\.{octet}\.{octet}", ip)
    if not match:
        return False
    return all(0 <= int(part) <= 255 for part in match.groups())


if __name__ == "__main__":
    main()
