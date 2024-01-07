#  python .\convertRm2KCharsetToXP.py
#  pip3 install pillow
from PIL import Image

def remove_most_abundant_color(img, width, height):
    color_freq = {}

  # Loop through every pixel in the image
    for x in range(width):
        for y in range(height):
          # Get the RGBA value of the pixel
            r, g, b, a = img.getpixel((x, y))
          # Convert the RGBA value to a hex string
            color = f"{r:02x}{g:02x}{b:02x}{a:02x}"
          # Increment the frequency of the color by 1
            color_freq[color] = color_freq.get(color, 0) + 1

  # Find the most abundant color by sorting the dictionary by values
    most_abundant_color = sorted(color_freq.items(), key=lambda x: x[1], reverse=True)[0][0]

  # Convert the most abundant color from hex to RGBA
    r, g, b, a = int(most_abundant_color[:2], 16), int(most_abundant_color[2:4], 16), int(most_abundant_color[4:6], 16), int(most_abundant_color[6:], 16)

  # Loop through every pixel in the image again
    for x in range(width):
        for y in range(height):
          # Get the RGB value of the pixel
            r2, g2, b2, a2 = img.getpixel((x, y))
          # If the pixel has the same color as the most abundant color, set it to transparent
            if r == r2 and g == g2 and b == b2 and a == a2:
                img.putpixel((x, y), (0, 0, 0, 0))

def reorder(img, fileIndex):
  # Open the original image and get its dimensions
  width, height = img.size

  # Define the dimensions of the smaller pictures
  small_width = 24
  small_height = 32

  # Create a list to store the smaller pictures
  small_pics = []

  # Loop through the original image and crop it into smaller pictures
  for i in range(0, height, small_height):
    for j in range(0, width, small_width):
      # Crop a smaller picture from the original image
      small_pic = img.crop((j, i, j + small_width, i + small_height))
      # Append the smaller picture to the list
      small_pics.append(small_pic)

  # Define the dimensions of the new image
  new_width = 4 * small_width
  new_height = 4 * small_height

  # Create a new image with the same mode and format as the original image
  new_img = Image.new(img.mode, (new_width, new_height), img.getpixel((0, 0)))

  # Define the order of repositioning the smaller pictures
  order = [8, 7, 8, 9,
          11, 10, 11, 12,
          5, 4, 5, 6,
          2, 1, 2, 3]

  # Loop through the new image and paste the smaller pictures according to the order
  for i in range(0, new_height, small_height):
    for j in range(0, new_width, small_width):
      # Get the index of the smaller picture from the order list
      index = order.pop(0) - 1
      # Get the smaller picture from the list
      small_pic = small_pics[index]
      # Paste the smaller picture to the new image
      new_img.paste(small_pic, (j, i))

  # Scale up the new image by 2 using nearest neighbor interpolation
  new_img = new_img.resize((new_img.width * 2, new_img.height * 2), Image.NEAREST)
  # Save the new image
  new_img.save(f"new_{fileIndex}.png", bits=24)

# Open the original image and get its dimensions
img = Image.open("example.png")
img = img.convert("RGBA")
width, height = img.size

mode = img.mode
palette = img.palette

remove_most_abundant_color(img, width, height)

# Define the dimensions of the smaller pictures
small_width = 72
small_height = 128

# Loop through the original image and crop it into smaller pictures
for k in range(0, height, small_height):
  for l in range(0, width, small_width):
    # Crop a smaller picture from the original image
    small_pic = img.crop((l, k, l + small_width, k + small_height))
    # Save the smaller picture with a unique name
    #small_pic.save(f"new_{k + l + 1}.png", bits=24)
    reorder(small_pic, k + l + 1)