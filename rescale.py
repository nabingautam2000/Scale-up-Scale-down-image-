from PIL import Image

# Set the target limits for resize
TARGETX = 1080
TARGETY = 1920

# Specify the image file name
entry = "lion.jfif"

try:
    tx = 0
    ty = 0
    im = Image.open(entry)
    (x, y) = im.size
    ratio = y / x
    if y < TARGETY and x < TARGETX:
        # need to adjust size
        if ratio > 1.0:
            # Tall picture - use y for scale
            scale = TARGETY / y
        else:
            scale = TARGETX / x
        tx = x * scale
        ty = y * scale
        newsize = (int(tx), int(ty))
        print(f"> Processing {entry} - scaling up from {x}x{y} to {tx}x{ty}")
        # resize
        im2 = im.resize(newsize)
        im2.save(entry)
    else:
        # already right size
        print(f"> Processing {entry} - no change {x}x{y}")
except FileNotFoundError:
    print(f"Error: The file {entry} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

