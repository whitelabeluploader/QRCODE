from browser import document, html, window

def generate_qr(event):
    user_input = document["user-input"].value
    error_level = document["error-level"].value
    box_size = int(document["box-size"].value)
    message_container = document["message-container"]

    # Clear any previous messages
    message_container.clear()

    if user_input.strip():  # Check for valid input
        # Create a new QRious instance with the user's input and settings
        qr = window.QRious.new(
            value=user_input,  # The data to encode in the QR code
            errorCorrectionLevel=error_level,  # Set the error correction level
            size=box_size * 10,  # Scale the size based on user input
            foreground="black",   # Set the QR code color
            background="white"    # Set the background color
        )

        # Get the QR code's Data URL
        qr_code_image_url = qr.toDataURL()  # Use QRious to convert to data URL

        # Set the src attribute of the image element to the QR code data URL
        qr_code_element = document["qr-code-image"]
        qr_code_element.attrs['src'] = qr_code_image_url  # Update source to Data URL
        qr_code_element.style.display = 'block'  # Make the image visible

        # Show a success message
        message_container <= html.P("QR Code generated successfully!", style={"color": "green"})
    else:
        # Show an error message if no input is provided
        message_container <= html.P("Please enter text or URL.", style={"color": "red"})

# Bind the button click event to the generate_qr function
document["generate-btn"].bind("click", generate_qr)
