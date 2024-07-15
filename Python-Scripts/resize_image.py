import os



def resize_image(image_dir, image_name, new_width, new_height):
    try:
        from PIL import Image
        image_path = os.path.join(image_dir, image_name)
        # Open the image using PIL
        image = Image.open(image_path)
        # Resize the image
        resized_image = image.resize((new_width, new_height))
        # Save the resized image
        resized_image_name = f"{os.path.splitext(image_name)[0]}_resized_{new_width}x{new_height}{os.path.splitext(image_name)[1]}"
        resized_image_path = os.path.join(image_dir, resized_image_name)
        resized_image.save(resized_image_path)
        print(f"Image '{image_name}' resized to {new_width}x{new_height} successfully.")
    except ImportError:
        print("Error: The PIL library is not installed. Please install it using 'pip install pillow'.")

if __name__ == "__main__":
    image_dir = input("Enter the path to the directory containing the image: ")
    image_name = input("Enter the name of the image file: ")
    image_dim = input("Enter the desired width and height of the resized image (separated by a space): ")
    width, height = map(int, image_dim.split())

    if not os.path.isdir(image_dir):
        print("Error: The specified directory does not exist.")
        exit(1)
    resize_image(image_dir, image_name, width, height)