import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
from PIL import Image


api_key = os.getenv('')
genai.configure(api_key=api_key)

def get_gemini_response(input_prompt,image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input_prompt,image[0]])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file  is not None:
        ##convert the pdf to image
        bytes_data =  uploaded_file.getvalue()

        

        image_parts = [
            {
                "mime_type":  uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded")
    


def main():
    input_prompt =""" 
    You are an expert nutritionist where you need to see the food items from
    the image and calculate the total calories, and also provide the details of every food items 
    with calories intake in below format

    1. Item 1 - no of calories
    2. Item 2 - no of calories
    ----
    ----

    Finally you can also mentioned that the food is healthy or not and also
    mentioned the
    percentage split of ratio of carbohydrates , fats , fibers, sugar and other important 
    things required in our diet.
    """



    st.set_page_config(page_title="Nutritionist  GenAI Doctor", page_icon="🦜")
    st.header("Nutritionist  GenAI Doctor")
    uploaded_file = st.file_uploader("Choose your Image..." , type=["jpg","jpeg" ,"png"])
    image=""
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image , caption="Uploaded Image" , use_column_width = True)

    submit = st.button("Calculate the calories..")

    if submit:
        image_data = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt,image_data)
        st.header("The Response is..")
        st.write(response)


if __name__ == "__main__":
    main()    