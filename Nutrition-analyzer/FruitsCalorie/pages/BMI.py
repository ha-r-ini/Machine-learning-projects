import streamlit as st

import base64
import cv2

# ================ Background image ===

st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:36px;">{"Nutrition analyzer and dietary choice recommendation using deep learning"}</h1>', unsafe_allow_html=True)


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('1.avif')


#====


st.title("BMI Calculator")
st.write("Enter your weight and height to calculate your BMI.")

weight = st.number_input("Enter your weight (in kg):", min_value=0.0, step=0.1)
height = st.number_input("Enter your height (in meters):", min_value=0.0, step=0.01)


if st.button("Calculate BMI"):


    bmi = weight/(height)**2
    
    
    if bmi < 18.5:
        st.text( "Underweight")
        
        import pandas as pd
         
        def hyperlink(url):
             return f'<a target="_blank" href="{url}">{url}</a>'
         
        dff = pd.DataFrame(columns=['page'])
        dff['page'] = ['FruitCalorie']
        dff['page'] = dff['page'].apply(hyperlink)
        dff = dff.to_html(escape=False)
     
        st.write(dff, unsafe_allow_html=True)           
        
        
    elif bmi >= 18.5 and bmi < 25:
        st.text( "Normal weight")
        
        import pandas as pd
         
        def hyperlink(url):
             return f'<a target="_blank" href="{url}">{url}</a>'
         
        dff = pd.DataFrame(columns=['page'])
        dff['page'] = ['FruitCalorie']
        dff['page'] = dff['page'].apply(hyperlink)
        dff = dff.to_html(escape=False)
     
        st.write(dff, unsafe_allow_html=True)           
        
        
        
    elif bmi >= 25 and bmi < 30:
        st.text( "Overweight")

        import pandas as pd
         
        def hyperlink(url):
             return f'<a target="_blank" href="{url}">{url}</a>'
         
        dff = pd.DataFrame(columns=['page'])
        dff['page'] = ['FruitCalorie']
        dff['page'] = dff['page'].apply(hyperlink)
        dff = dff.to_html(escape=False)
     
        st.write(dff, unsafe_allow_html=True)   


    else:
        st.text( "Obese")

        import pandas as pd
         
        def hyperlink(url):
             return f'<a target="_blank" href="{url}">{url}</a>'
         
        dff = pd.DataFrame(columns=['page'])
        dff['page'] = ['FruitCalorie']
        dff['page'] = dff['page'].apply(hyperlink)
        dff = dff.to_html(escape=False)
     
        st.write(dff, unsafe_allow_html=True)   