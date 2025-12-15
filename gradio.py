import gradio as gr

def rag_query_interface(query):
    # Run RAG answer
    answer = generate_answer(query, top_k=1, max_tokens=10)

    # Retrieve top images
    imgs = select_images_for_query(query, top_k_images=1, prefer_text_pages=True)
    if len(imgs) == 0:
        imgs = [blank_image]

    return answer, imgs

with gr.Blocks(title="Multimodal RAG with Phi-3 Vision") as demo:
    gr.Markdown("#Multimodal RAG Demo (Text + Images + Phi-3 Vision)")
    gr.Markdown("Ask a question about the PDF. The system will retrieve text + images and generate a grounded answer.")

    query_input = gr.Textbox(label="Enter your question", placeholder="e.g. What is self-attention?")
    answer_output = gr.Textbox(label="Phi-3 Vision Answer")

  
    image_output = gr.Gallery(label="Retrieved Images (Relevant)")

    submit_btn = gr.Button("Run RAG")
    submit_btn.click(rag_query_interface, inputs=query_input, outputs=[answer_output, image_output])

demo.launch(debug=True, share=True)
