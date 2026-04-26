import sys
from PIL import Image
from PIL import ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    if not input_file.endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid input")
    if not output_file.endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid output")
    if input_file.split(".")[-1] != output_file.split(".")[-1]:
        sys.exit("Input and output have different extensions")
    
    
    try:
        input_img = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")
    shirt_img = Image.open("shirt.png")
    size = shirt_img.size
    input_img = ImageOps.fit(input_img, size)
    input_img.paste(shirt_img, shirt_img)
    input_img.save(output_file)
main()