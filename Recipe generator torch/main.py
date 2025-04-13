import streamlit as st 
from transformers import T5Tokenizer, T5ForConditionalGeneration

model = T5ForConditionalGeneration.from_pretrained("./recipe_model")
tokenizer = T5Tokenizer.from_pretrained("./recipe_model")

st.title("Recipe Generator app in pytorch")
st.write("This is a simple app to generate recipes using pytorch.")
st.write("You can enter a list of ingredients and the app will generate a recipe for you.")
text_input = st.text_input("Enter a list of ingredients:", "chicken, rice, vegetables")
submit_button = st.button("Generate Recipe")

if submit_button:
    inputs = tokenizer.encode(text_input, return_tensors="pt")
    outputs = model.generate(inputs, max_length=50, num_beams=5, early_stopping=True)
    recipe = tokenizer.decode(outputs[0], skip_special_tokens=True)
    st.write("Generated Recipe:")
    st.write(recipe)
