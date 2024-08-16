import streamlit as st
import qrcode
from io import BytesIO

# Function to generate QR code
def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    return img

# Streamlit app layout
def main():
    # Set page configuration
    st.set_page_config(
        page_title="QR Code Generator",
        page_icon="🔗",
        layout="centered",
        initial_sidebar_state="expanded"
    )

    st.title("🔗 QR Code Generator")

    st.write("Easily generate a QR code for any URL. Enter the URL below, and get a downloadable QR code image.")

    # URL input field
    url_input = st.text_input("Enter the URL", placeholder="https://example.com")

    # Generate button
    if st.button("Generate QR Code"):
        if url_input:
            img = generate_qr_code(url_input)
            
            # Convert Pillow Image to bytes
            buffered = BytesIO()
            img.save(buffered, format="PNG")  # Save image as PNG format
            img_bytes = buffered.getvalue()
            
            # Display the generated QR code
            st.image(img_bytes, caption="Your QR Code", use_column_width=True)
            
            # Download button
            st.download_button(
                label="Download QR Code",
                data=img_bytes,
                file_name="qrcode.png",
                mime="image/png"
            )
        else:
            st.warning("Please enter a valid URL.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
