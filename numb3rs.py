import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.fullmatch(r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})", ip)
    if not match:
        return False
    return all(0 <= int(part) <= 255 for part in match.groups())


if __name__ == "__main__":
    main()
