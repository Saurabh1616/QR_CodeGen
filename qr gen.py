import qrcode
from PIL import Image  # Importing Image from the Pillow library

def generate_qr(data, filename='qr_code.png'):
    
    # Create a QR Code instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
        box_size=10,  # controls how many pixels each "box" of the QR code is
        border=4,  # controls how many boxes thick the border should be
    )
    
    # Add data to the QR Code
    qr.add_data(data)
    qr.make(fit=True)

    # Generate image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(filename)
    print(f"QR code generated and saved as {filename}")

    # Open the image using PIL
    img.show()

if __name__ == "__main__":
    data = input("Enter text or URL to generate QR code: ")
    generate_qr(data)
