import streamlit as st
from groq import Groq

st.set_page_config(page_title="Amar AI")
st.title("🤖 Amar AI")
st.write("বাংলায় যা খুশি প্রশ্ন করেন!")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("এখানে লিখেন..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        chat = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{"role": "system", "content": "তুমি একজন বন্ধুর মত, সব সময় বাংলায় উত্তর দিবে।"}] + st.session_state.messages
        )
        reply = chat.choices[0].message.content
        st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
