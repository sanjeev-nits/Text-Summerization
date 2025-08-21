import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import time 

st.set_page_config(page_title="Text Summarization App", layout="wide")

@st.cache_resource
def load_model():
    model_path = "artifacts/model_trainer/pegasus-samsung-model"   
    tokenizer_path = "artifacts/model_trainer/tokenizer"          
    
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    return tokenizer, model

tokenizer, model = load_model()


st.title("📝 Text Summarization App")
st.write("Summarize long text into concise form using your fine-tuned Pegasus model.")


input_text = st.text_area("✍️ Enter your text here:", height=200)

uploaded_file = st.file_uploader("📂 Or upload a .txt file", type=["txt"])
if uploaded_file is not None:
    input_text = uploaded_file.read().decode("utf-8")


summary = ""
if st.button("🚀 Summarize"):
    if input_text.strip() == "":
        st.warning("⚠️ Please enter or upload some text.")
    else:
        with st.spinner("Summarizing... ⏳"):
            time.sleep(1)  # just for UX
            inputs = tokenizer([input_text], max_length=1024, truncation=True, return_tensors="pt")
            summary_ids = model.generate(
                inputs["input_ids"],
                max_length=150,
                min_length=40,
                length_penalty=2.0,
                num_beams=4,
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

