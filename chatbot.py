import streamlit as st
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load model and tokenizer
@st.cache_resource
def load_model():
    model_path = r"C:\Users\Sachintha\Desktop\chatbot\University_chatbot"
    tokenizer = T5Tokenizer.from_pretrained(model_path)
    model = T5ForConditionalGeneration.from_pretrained(model_path)
    return tokenizer, model

tokenizer, model = load_model()

small_talk = {
    "hello": "Hi there! How can I help you with university questions?",
    "hi": "Hello! What would you like to ask about courses?",
    "how are you": "I’m just a bot, but I’m here to help you with university queries!"
}

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🤖 University Chatbot")

# Show previous chat history first
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Handle new user message
if user_question := st.chat_input("Type your question..."):

    # Show user message immediately
    with st.chat_message("user"):
        st.write(user_question)

    # Generate bot reply
    if user_question.lower().strip() in small_talk:
        answer = small_talk[user_question.lower().strip()]
    else:
        input_text = "question: " + user_question

        input_ids = tokenizer.encode(input_text, return_tensors="pt")

        outputs = model.generate(
            input_ids,
            max_length=128,
            num_beams=4,
            early_stopping=True
        )

        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

        if answer.strip() == "":
            answer = "I'm sorry, I don't know how to answer that. Please ask about university courses."

    # Show bot message immediately under user message
    with st.chat_message("assistant"):
        st.write(answer)

    # Save both user and bot messages to chat history
    st.session_state.messages.append({"role": "user", "content": user_question})
    st.session_state.messages.append({"role": "assistant", "content": answer})
