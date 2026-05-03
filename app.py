import streamlit as st
from generator import generate_content
st.set_page_config(
    page_title="AI Content Generator",
    page_icon="Icon",
    layout="centered"
)
st.title("AI Contenet Generator")
st.subheader("Generate Blogs,Posts,and Threads using AI")
st.markdown(
    """
    <style>
   .custom-label{
        font-size:22px !important;
        font-weight:bold !imporant;
    }
    </style>
    """,unsafe_allow_html=True 
)
st.markdown('<p class="custom-label"> Enter topic</p>',unsafe_allow_html=True)
topic=st.text_input(
    label="hidden",
    label_visibility="collapsed",
    placeholder="Example :benifits of learning ai"
)
st.markdown('<p class="custom-label">Type</p>',unsafe_allow_html=True)
content_type=st.selectbox(
    label="hidden",
    label_visibility="collapsed",
    options=["Blog post","LinkedIn post","Twitter","Thread"]
)
st.markdown('<p class="custom-label">Select Tone</p>',unsafe_allow_html=True)
tone=st.selectbox(
    label="hidden",
    label_visibility="collapsed",
    options=["Professional","Casual","Technical","Creative"]
)
st.markdown('<p class="custom-label">Word Limit</p>',unsafe_allow_html=True)
word_limit=st.slider(
    label="hidden",
    label_visibility="collapsed",
    min_value=100,
    max_value=1000,
    step=50
)
st.markdown('<p class="custom-label">Additional instructions</p>',unsafe_allow_html=True)
extra_instruction=st.text_area(
    label="hidden",
    label_visibility="collapsed",
    placeholder="Example :Make it begineer Friendly"
)
generate=st.button("Generate Content")
if generate:
    if topic.strip()=="":
        st.error("Please Enter topic")
    else:
        st.success("Generating content..")
        content=generate_content(
            topic,
            content_type,
            tone,
            word_limit,
            extra_instruction,
        )
        st.markdown("<div id='output'></div>",unsafe_allow_html=True)
        st.subheader("Generated Content")
        if content.startswith("Error"):
            st.error(content)
        else:
            st.markdown(content)
            st.markdown("""
                        <script>
                        document.getElementById("output").scroolIntoView({
                            behaviour:"smooth"
                        });
                        </script>
                        """,unsafe_allow_html=True)

        
