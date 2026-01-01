import streamlit as st
import tempfile
import os
from PIL import Image


# from code import (
#     extract_pdf_data,
#     generate_answer,
#     select_images_for_query,
#     build_embeddings
# )


st.set_page_config(
    page_title="Multimodal RAG (Phi-3 Vision)",
    layout="wide",
)

st.title(" Multimodal RAG with Phi-3 Vision")
st.markdown("Upload a PDF and ask questions using text + images.")


uploaded_file = st.file_uploader(
    "Upload a PDF document",
    type=["pdf"]
)

if uploaded_file:
    with st.spinner(" Processing PDF..."):
        # Save temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            pdf_path = tmp.name


        process_pdf(pdf_path)

    st.success("PDF processed successfully!")


    query = st.text_input("Ask a question about the document")

    if query:
        with st.spinner("🔍 Searching and reasoning..."):
            answer = generate_answer(query, top_k=3, max_tokens=200)
            

        st.subheader(" Answer")
        st.write(answer)



else:
    st.info(" Upload a PDF to begin")
