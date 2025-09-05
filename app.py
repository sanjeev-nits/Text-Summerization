import time
import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

st.set_page_config(page_title="Text Summarization App", layout="wide")

# ------------------------------
# Load Model
# ------------------------------
@st.cache_resource
def load_model():
    model_name = "sanjeevnits24/summerizer"  # your Hugging Face repo

    tokenizer = AutoTokenizer.from_pretrained(model_name, token=os.getenv("HF_TOKEN"))
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name, token=os.getenv("HF_TOKEN"))

    # Move model to GPU if available
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)

    return tokenizer, model, device

tokenizer, model, device = load_model()

# ------------------------------
# UI
# ------------------------------
st.title("📝 Text Summarization App")
st.write("Summarize long text into concise form using your fine-tuned Pegasus model.")

input_text = st.text_area("✍️ Enter your text here:", height=200)

uploaded_file = st.file_uploader("📂 Or upload a .txt file", type=["txt"])
if uploaded_file is not None:
    input_text = uploaded_file.read().decode("utf-8")

# ------------------------------
# Summary Length Control
# ------------------------------
st.markdown("### ⚙️ Summary Settings")
summary_length = st.slider("📏 Select maximum summary length (tokens)", 50, 400, 150)
min_summary_length = int(summary_length * 0.5)

# ------------------------------
# Summarization
# ------------------------------
summary = ""
if st.button("🚀 Summarize"):
    if input_text.strip() == "":
        st.warning("⚠️ Please enter or upload some text.")
    else:
        with st.spinner("Summarizing... ⏳"):
            time.sleep(1)  # for UX only

            # Prepare input
            inputs = tokenizer(
                input_text,
                max_length=1024,
                truncation=True,
                return_tensors="pt"
            ).to(device)

            # Generate summary
            summary_ids = model.generate(
                **inputs,
                max_length=summary_length,
                min_length=min_summary_length,
                num_beams=5,
                no_repeat_ngram_size=3,
                repetition_penalty=2.0,
                length_penalty=0.8, 
                early_stopping=True
            )

            summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        st.subheader("🔍 Summary:")
        st.success(summary)

        # Download Button
        st.download_button(
            label="💾 Download Summary",
            data=summary,
            file_name="summary.txt",
            mime="text/plain"
        )

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.caption("created by SanjeevNits")
