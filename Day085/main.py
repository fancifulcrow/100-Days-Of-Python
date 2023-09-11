from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageStat

def add_watermark(image_path, text):
    # open the image
    image = Image.open(image_path)

    # Creating draw object
    draw = ImageDraw.Draw(image)

    # choosing the font and making the font size dynamic (i.e relative to the image size)
    width, height = image.size
    font_size = int(min(width, height) * 0.05)
    font = ImageFont.truetype("arial.ttf", font_size)

    # Positioning the text to the bottom right
    text_width = draw.textlength(text, font)
    x = width - text_width - 10
    y = height - font_size - 10

    # A function to calulate the average brightness of the image and return a value from 0 to 1
    def brightness_checker(image):
        im = image.convert('L')
        stat = ImageStat.Stat(im)
        return stat.mean[0] / 255
    
    # Set the fill with respect to the brightness of the image
    if brightness_checker(image) > 0.5:
        fill = (0, 0, 0, 128)
    else:
        fill = (255, 255, 255, 128)

    # draw the watermark
    draw.text((x, y), text, fill=fill, font=font)

    # save the image in this directory
    output_path = f"./{image_path.split('/')[-1]}"
    image.save(output_path)
    image.show()


def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")])
    image_entry.delete(0, END)
    image_entry.insert(0, file_path)


def feedback_info():
    image_path = image_entry.get()
    watermark_text = watermark_entry.get()

    if not image_path or not watermark_text:
        message_label.config(text="Please fill in all fields.")
    else:
        add_watermark(image_path, watermark_text)
        message_label.config(text="Watermark added successfully!")


# Create the main window
window = Tk()
window.title("Image Watermarker")
window.config(padx=20, pady=20)

# heading
heading_label = Label(window, text="Image Watermarker", font=("Times New Roman", 24, "bold"))
heading_label.config(pady=12)
heading_label.grid(row=0, column=1)

# image path selector
image_label = Label(window, text="Select Image:")
image_label.grid(row=1, column=0)

image_entry = Entry(window)
image_entry.config(width=50)
image_entry.grid(row=1, column=1)

browse_button = Button(window, text="Browse", command=open_file)
browse_button.grid(row=1, column=2)

# watermark text
watermark_label = Label(window, text="Watermark Text:")
watermark_label.grid(row=2, column=0)

watermark_entry = Entry(window)
watermark_entry.config(width=50)
watermark_entry.grid(row=2, column=1)

# Add watermark button
watermark_button = Button(window, text="Add Watermark", command=feedback_info)
watermark_button.config(pady=4, padx=2)
watermark_button.grid(row=3, column=1)

# user feedback
message_label = Label(window, text="")
message_label.grid(row=4, column=1)

window.mainloop()
