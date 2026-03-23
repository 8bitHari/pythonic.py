def main():
    file = name(input("File name: "))
    return file

def name(extension):
    extension = extension.lower().strip()
    if extension.endswith(".gif"):
        print("image/gif")
    elif extension.endswith(".jpg") or extension.endswith("jpeg"):
        print("image/jpeg")
    elif extension.endswith(".txt"):
        print("text/plain")
    elif extension.endswith(".zip"):
        print("Application/zip")
    else:
        print("application/octet-stream")

main()