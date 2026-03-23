def main():
    file = name(input("File name: "))
    return file

def name(extensions):
    extensions = extensions.lower().strip().split(".")[-1]
    types = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip"
    }
    print(types.get(extensions, "application/octet_stream"))

main()