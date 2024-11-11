from browser import document, html, window
import qrcode
from io import BytesIO
import base64

def generate_qr(event):
    user_input = document["user-input"].value
    error_level = document["error-level"].value
    box_size = int(document["box-size"].value)
    border_size = int(document["border-size"].value)

    if user_input:
        error_correction = {
            "L": qrcode.constants.ERROR_CORRECT_L,
            "M": qrcode.constants.ERROR_CORRECT_M,
            "Q": qrcode.constants.ERROR_CORRECT_Q,
            "H": qrcode.constants.ERROR_CORRECT_H
        }

        qr = qrcode.QRCode(
            version=1,  # You can modify this to fit more data if needed
            error_correction=error_correction[error_level],
            box_size=box_size,
            border=border_size,
        )
        qr.add_data(user_input)
        qr.make(fit=True)
        
        img = qr.make_image(fill='black', back_color='white')
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        img_element = html.IMG(src=f"data:image/png;base64,{img_str}")
        qr_code_container.clear()  # Clear any previous QR code
        qr_code_container <= img_element  # Append the new QR code image
    else:
        window.alert("Please enter text or URL.")

qr_code_container = document["qr-code-container"]
document["generate-btn"].bind("click", generate_qr)
