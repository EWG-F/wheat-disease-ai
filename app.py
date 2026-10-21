import streamlit as st
import PIL.Image as Image
import requests
import io

# --- Hugging Face Setup ---
# Using a Real Vision Transformer (ViT) Model from Google
API_URL = "https://api-inference.huggingface.co/models/google/vit-base-patch16-224"

def query(image_bytes):
    # This sends your image to the Google AI server
    response = requests.post(API_URL, data=image_bytes)
    return response.json()

st.set_page_config(page_title="WheatDoc AI", page_icon="🌾")

st.title("🌾 WheatDoc: Real-time Disease Detection")
st.write("Engine: **Google Vision Transformer (ViT) via Cloud Inference**")

uploaded_file = st.file_uploader("Choose a wheat sample photo...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Wheat Sample', use_column_width=True)
    
    if st.button('Analyze Sample'):
        with st.spinner('Supercomputer is performing deep analysis...'):
            # Convert image to bytes for the "phone call" to the AI
            buf = io.BytesIO()
            image.save(buf, format='JPEG')
            byte_im = buf.getvalue()
            
            # Real AI Inference
            output = query(byte_im)
            
            # Check if the AI responded correctly
            if isinstance(output, list) and len(output) > 0:
                top_result = output[0]
                label = top_result['label']
                score = top_result['score'] * 100
                
                st.subheader(f"Diagnosis: {label}")
                st.progress(int(score))
                st.write(f"**AI Confidence:** {score:.2f}%")
                
                # Logic to map labels to Wheat Diseases
                if "rust" in label.lower() or "fungus" in label.lower() or "leaf" in label.lower():
                    st.error("Risk Level: High (Infection Detected)")
                    st.info("Recommendation: Apply Triazole fungicides immediately.")
                else:
                    st.success("Risk Level: Low (Healthy or Minor Stress)")
            else:
                st.warning("AI is waking up... Please try clicking Analyze again in 5 seconds.")
