from PIL import Image

def main():
	img = Image.new("RGB", (512, 512), "red")
	img.save("image_1", "JPEG")

if __name__ == "__main__":
	main()
