import streamlit as st
import requests

# API URL and key
API_URL = 'https://api.api-ninjas.com/v1/textsimilarity'
API_KEY = 'RSmEdCvXyJE98mRGl9fdlg==5cgp3b06X3U62ZSF'

# Streamlit app
st.title("Matn o'xshashligini tekshirish")
st.write("Ushbu dastur ikkita matn o'rtasidagi o'xshashlikni tekshiradi")

# Input fields for the texts
text_1 = st.text_area("Birinchi matnni kiriting:", "Bu misol matn.")
text_2 = st.text_area("Ikkinchi matnni kiriting:", "Bu faqat boshqa misol matn.")

# Button to submit
if st.button("O'xshashlikni tekshirish"):
    body = {'text_1': text_1, 'text_2': text_2}

    # Make the API request
    response = requests.post(API_URL, headers={'X-Api-Key': API_KEY}, json=body)

    if response.status_code == requests.codes.ok:
        # Display the result
        result = response.json()
        similarity = result.get('similarity', 'N/A')
        
        if similarity != 'N/A':
            # Round the similarity to 2 decimal places
            similarity = round(similarity, 2)
        
        st.success(f"The similarity score is: {similarity}")
    else:
        # Display error message
        st.error(f"Error {response.status_code}: {response.text}")



# import streamlit as st
# import requests

# # API URL and key
# API_URL = 'https://api.api-ninjas.com/v1/textsimilarity'
# API_KEY = 'RSmEdCvXyJE98mRGl9fdlg==5cgp3b06X3U62ZSF'

# # Streamlit app
# st.title("Matn o'xshashligini tekshirish")
# st.write("Ushbu dastur ikkita matn o'rtasidagi o'xshashlikni tekshiradi")

# # Input fields for the texts
# text_1 = st.text_area("Birinchi matnni kiriting:", "Bu misol matn.")
# text_2 = st.text_area("Ikkinchi matnni kiriting:", "Bu faqat boshqa misol matn.")

# # Button to submit
# if st.button("O'xshashlikni tekshirish"):
#     body = {'text_1': text_1, 'text_2': text_2}

#     # Make the API request
#     response = requests.post(API_URL, headers={'X-Api-Key': API_KEY}, json=body)

#     if response.status_code == requests.codes.ok:
#         # Display the result
#         result = response.json()
#         similarity = result.get('similarity', 'N/A')
#         st.success(f"The similarity score is: {similarity}")
#     else:
#         # Display error message
#         st.error(f"Error {response.status_code}: {response.text}")
