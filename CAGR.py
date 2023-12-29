import streamlit as st

# Function to calculate CAGR
def calculate_cagr(beginning_value, ending_value, num_years):
    cagr = ((ending_value / beginning_value) ** (1 / num_years)) - 1
    return cagr

# Streamlit UI
st.title('CAGR Calculator')

beginning_value = st.number_input('Enter Beginning Value:')
ending_value = st.number_input('Enter Ending Value:')
num_years = st.number_input('Enter Number of Years:', min_value=1, step=1)

if st.button('Calculate CAGR'):
    try:
        cagr = calculate_cagr(beginning_value, ending_value, num_years)
        st.success(f'CAGR: {cagr:.2%}')
    except ZeroDivisionError:
        st.error("Number of years cannot be zero.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
