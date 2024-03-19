import streamlit as st
import pickle
import pandas as pd

# Load the saved pipeline (including preprocessing and model)
with open('D:\Machine_learning\Projects\Student_Placement\Model\pipe.pkl', 'rb') as file:
    pipe = pickle.load(file)

# Define the Streamlit app
def main():
    st.sidebar.title('About Me')

    # Add links to GitHub profile, LinkedIn profile, and email
    st.sidebar.markdown('### Links')
    st.sidebar.markdown('[GitHub](https://github.com/rkmaurya93049)')
    st.sidebar.markdown('[LinkedIn](https://www.linkedin.com/in/raushan-kumar-74209b253/)')

    # Add about section
    st.sidebar.markdown('---')
    st.sidebar.markdown('### About')
    st.sidebar.markdown('This is a Streamlit app for predicting student placement.')

    st.title('Student Placement Prediction')

    # Add input fields for the user to enter data
    gender = st.selectbox('Gender', ['Male', 'Female'])
    ssc_percentage = st.number_input('SSC Percentage', min_value=0.0, max_value=100.0)
    degree_percentage = st.number_input('Degree Percentage', min_value=0.0, max_value=100.0)
    work_experience = st.selectbox('Work Experience', ['No', 'Yes'])
    emp_test_percentage = st.number_input('Employment Test Percentage', min_value=0.0, max_value=100.0)
    mba_percent = st.number_input('MBA Percentage', min_value=0.0, max_value=100.0)

    # Prepare the input data for prediction
    input_data = pd.DataFrame({
        'gender': [gender],
        'ssc_percentage': [ssc_percentage],
        'degree_percentage': [degree_percentage],
        'work_experience': [work_experience],
        'emp_test_percentage': [emp_test_percentage],
        'mba_percent': [mba_percent]
    })

    # Make predictions
    if st.button('Predict'):
        prediction = pipe.predict(input_data)
        if prediction[0] == 'Placed':
            st.success('The student is likely to be placed.')
        else:
            st.error('The student is not likely to be placed.')

if __name__ == '__main__':
    main()
