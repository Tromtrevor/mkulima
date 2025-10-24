
import streamlit as st

st.sidebar.title('MKULIMA')
st.sidebar.page_link('app.py', label='Home')
st.sidebar.page_link('pages/crop_recommendation.py', label='Crop Recommendation')   
st.sidebar.page_link('pages/results.py', label = 'Results')

# -----------------------
# Page Setup
# -----------------------
st.set_page_config(page_title='MKULIMA', layout='centered')
st.title('MKULIMA')
    
st.markdown('''
Test your trained crop yield prediction model here.  
Enter the soil and climate parameters below to get the predicted yield.
'''
)


if st.button('GET STARTED'):
    st.switch_page('pages/crop_recommendation.py')

