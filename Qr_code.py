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

    # Custom CSS for styling
    st.markdown(
        """
        <style>
        body {
            background-color: #f4f6f9;
            font-family: 'Arial', sans-serif;
            color: #333;
        }
        
        .title {
            text-align: center;
            font-size: 36px;
            color: #3f51b5;
            margin-top: 50px;
            font-weight: bold;
        }

        .description {
            text-align: center;
            font-size: 18px;
            margin-top: 10px;
            color: #555;
        }

        .input-container {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }

        .input-field {
            width: 60%;
            padding: 10px;
            font-size: 16px;
            border: 2px solid #4caf50;
            border-radius: 8px;
            outline: none;
            margin-right: 10px;
        }

        .input-field:focus {
            border-color: #3f51b5;
        }

        .button {
            padding: 10px 20px;
            background-color: #4caf50;
            color: white;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s ease;
        }

        .button:hover {
            background-color: #45a049;
        }

        .qr-container {
            text-align: center;
            margin-top: 40px;
            width: 100%;
            display: flex;
            justify-content: center;
            flex-direction: column;
            align-items: center;
        }

        .download-btn {
            display: block;
            width: 200px;
            margin: 20px auto;
            padding: 10px;
            background-color: #3f51b5;
            color: white;
            font-size: 16px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .download-btn:hover {
            background-color: #303f9f;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # Title and description
    st.markdown('<div class="title">🔗 QR Code Generator</div>', unsafe_allow_html=True)
    st.markdown('<div class="description">Easily generate a QR code for any URL. Enter the URL below, and get a downloadable QR code image.</div>', unsafe_allow_html=True)

    # URL input field
    with st.container():
        st.markdown('<div class="input-container">', unsafe_allow_html=True)
        url_input = st.text_input("Enter the URL", placeholder="https://example.com", key="url_input", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

        # Generate button
        if st.button("Generate QR Code", key="generate_btn", help="Click to generate your QR code"):
            if url_input:
                img = generate_qr_code(url_input)
                
                # Convert Pillow Image to bytes
                buffered = BytesIO()
                img.save(buffered, format="PNG")  # Save image as PNG format
                img_bytes = buffered.getvalue()
                
                # Display the generated QR code and download button inside a container
                st.markdown('<div class="qr-container">', unsafe_allow_html=True)
                st.image(img_bytes, caption="Your QR Code", use_column_width=False)  # Set width to medium size
                st.download_button(
                    label="Download QR Code",
                    data=img_bytes,
                    file_name="qrcode.png",
                    mime="image/png",
                    key="download_btn"
                )
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning("Please enter a valid URL.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
