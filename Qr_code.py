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

    st.markdown("""
        <style>
            .main-container {
                border: 2px solid #4CAF50;
                border-radius: 10px;
                padding: 20px;
                background-color: #f9f9f9;
                max-width: 800px;
                margin: auto;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            .title {
                text-align: center;
                color: #4CAF50;
                font-size: 2.5em;
                margin-bottom: 20px;
            }
            .description {
                text-align: center;
                font-size: 1.2em;
                margin-bottom: 30px;
            }
            .input-container {
                text-align: center;
                margin-bottom: 20px;
            }
            .button-container {
                text-align: center;
                margin-top: 20px;
            }
            .qr-container {
                text-align: center;
                margin-top: 30px;
                padding: 20px;
                border: 1px solid #ddd;
                border-radius: 10px;
                background-color: #fff;
            }
            .download-btn {
                margin-top: 15px;
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 1em;
                text-decoration: none;
                display: inline-block;
            }
            .download-btn:hover {
                background-color: #45a049;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>🔗 QR Code Generator</h1>", unsafe_allow_html=True)
    st.markdown("<p class='description'>Easily generate a QR code for any URL. Enter the URL below, and get a downloadable QR code image.</p>", unsafe_allow_html=True)

    # URL input field
    url_input = st.text_input("Enter the URL", placeholder="https://example.com", key="url_input")

    # Generate button
    st.markdown("<div class='button-container'>", unsafe_allow_html=True)
    if st.button("Generate QR Code"):
        if url_input:
            img = generate_qr_code(url_input)
            
            # Convert Pillow Image to bytes
            buffered = BytesIO()
            img.save(buffered, format="PNG")  # Save image as PNG format
            img_bytes = buffered.getvalue()
            
            # Display the generated QR code
            st.markdown("<div class='qr-container'>", unsafe_allow_html=True)
            st.image(img_bytes, caption="Your QR Code", use_column_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Download button
            st.markdown(
                st.download_button(
                    label="Download QR Code",
                    data=img_bytes,
                    file_name="qrcode.png",
                    mime="image/png",
                    key='download-btn',
                    button_text="Download QR Code",
                    style="""
                        .download-btn {
                            margin-top: 15px;
                            background-color: #4CAF50;
                            color: white;
                            padding: 10px 20px;
                            border: none;
                            border-radius: 5px;
                            cursor: pointer;
                            font-size: 1em;
                            text-decoration: none;
                            display: inline-block;
                        }
                        .download-btn:hover {
                            background-color: #45a049;
                        }
                    """
                )
            )
        else:
            st.warning("Please enter a valid URL.")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
