import streamlit as st
import base64
# Background image
st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:36px;">{"Nutrition analyzer and dietary choice recommendation using deep learning"}</h1>', unsafe_allow_html=True)

# Function to add background image from local file
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

# Call function to add background image
add_bg_from_local('1.avif')

# Trainer/Nutritionist Consultation header
st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:24px;">{"Trainer/Nutritionist Consultation"}</h1>', unsafe_allow_html=True)

# Location image and content alignment
location_column, content_column,col = st.columns([5, 6, 7])  # Adjust the column widths as needed

# Location information
with location_column:
    st.image("1.png", width=100)  # Location image
    st.write('HEMA')
    st.write('+91-9385637964')
    st.markdown('<i class="fas fa-building"></i> JAZZ fitness studio madurai', unsafe_allow_html=True)
    st.write('2nd Floor, 87A, Navavel Towers, S.S.Colony, Bypass Rd, next to Manyavar,')
    st.write('opp. to ICICI BANK, Madurai, Tamil Nadu 625010')
    st.text("----------------------------------------------------------------------------------")

# Content information
with content_column:
    st.image("1.png", width=100) 
    st.write('Prem kumar')
    st.write('+91-9385637964')
    st.markdown('<i class="fas fa-dumbbell"></i> ADROIT FITNESS ACADEMY', unsafe_allow_html=True)
    st.write('ricky towers 4th floor,SS Colony, plot no:85, Subramaniya Pillai St,')
    st.write('Madurai, Tamil Nadu 625010')
    st.text("----------------------------------------------------------------------------------")

with col:
    st.image("1.png", width=100) 
    st.write('Janani')
    st.write('+91-7492740294')
    st.markdown('<i class="fas fa-dumbbell"></i> Club19 The GYM', unsafe_allow_html=True)
    st.write('1st Floor, Hotel Jayasakthi, 22A, Ponni St, above Thalapakatti, nagar, Madurai,')
    st.write('Tamil Nadu 625016')
    st.text("----------------------------------------------------------------------------------")    