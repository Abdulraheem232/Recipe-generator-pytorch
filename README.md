
---

# 🍲 Recipe Generator App

This is a simple and fun Recipe Generator App built using a transformer model in PyTorch and deployed with Streamlit. It generates recipes based on a small training dataset, so the outputs might not be perfect — but it’s a great starting point and a proof of concept!

## 🧠 Tech Stack

- **Model**: Transformer (implemented in **PyTorch**)  
- **Interface**: Built using **Streamlit**

## 🚀 Getting Started

1. **Run the Jupyter Notebook (`.ipynb`)**  
   This trains and/or prepares the model for usage.

2. **Unzip the `recipe_model` folder**  
   The folder contains the saved transformer model and tokenizer needed for generation.

3. **Run the Streamlit app**  
   Use the following command:
   ```bash
   streamlit run main.py
   ```

## ⚠️ Notes

- The model is trained on a **small dataset**, so generated recipes may not always be accurate or complete.
- This app is intended as a fun experiment and a demonstration of transformer capabilities in NLP tasks.

## 📝 Sample Prompts

Try using the following prompts to test the generator:

- `Generate a vegetarian recipe for dinner with lemongrass, tofu, tomato, sesame seeds, avoiding cucumber.`
- `Generate a dairy-free recipe for dinner with tomato, eggplant, pasta, sesame seeds, avoiding bell peppers.`
- `Generate a vegetarian recipe for dinner with tomato, soy sauce, spinach, chickpeas, avoiding basil.`
- `Generate a vegetarian recipe for dinner with lemongrass, garlic, potato, soy sauce, avoiding sesame seeds.`

These kinds of prompts guide the model to generate creative and tailored recipes based on your input!

## 📂 File Structure

```
├── main.py                 # Streamlit app
├── recipe_model.zip        # Compressed model folder
├── Recipe_Generator_App.ipynb     # Model training or loading notebook
├── README.md               # This file
```

---

