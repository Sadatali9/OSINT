from google.cloud import vision

def image_analyzer(file_path):
    """
    Analyze an image using Google Cloud Vision API.
    """
    client = vision.ImageAnnotatorClient()
    with open(file_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    for label in labels:
        print(label.description)

def main():
    file_path = input("Enter the image file path: ")
    image_analyzer(file_path)

if __name__ == "__main__":
    main()