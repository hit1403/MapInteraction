import streamlit as st
import subprocess
import sys

# Specify the Python executable path
PYTHON_PATH = sys.executable
# Define paths to scripts
getmap_script = r"C:\Users\S HITESH\PycharmProjects\pythonProject2\GetControlPoints\get_map.py"
getpolygon_script = r"C:\Users\S HITESH\PycharmProjects\pythonProject2\GetCountryPolygon\get_countries.py"
getcountry_script = r"C:\Users\S HITESH\PycharmProjects\pythonProject2\CountryName\country_name.py"
# Title and description
st.title("Interactive Mapping")
st.write("This application allows you to interactively mark points on a map or image, define custom polygons for regions of interest, and dynamically annotate regions using hand gestures.")

# Sidebar menu to select the operation
operation = st.sidebar.selectbox("Select Operation", ["Set corner Points", "Add countries", "Test your world map skills"])

# Function to run the selected Python file
process = None  # Initialize subprocess variable

def run_python_file(file_path):
    global process  # Use the global process variable
    if process and process.poll() is None:
        st.warning("A process is already running. Stop it before starting a new one.")
        return
    process = subprocess.Popen([PYTHON_PATH, file_path])


# Execute the selected operation
if operation == "Set corner Points":
    st.write("Use this option to mark points on a map or image.")
    if st.button("Run the operartion"):
        run_python_file(getmap_script)  # Update the file path

elif operation == "Add countries":
    st.write("Use this option to define custom polygons for countries or regions.")
    st.write("NOTE : Press e to EXIT")
    if st.button("Run the operartion"):
        run_python_file(getpolygon_script)  # Update the file path

elif operation == "Test your world map skills":
    st.write("Use this option for real-time hand tracking and dynamic region annotation.")
    st.write("NOTE : Press e to EXIT")
    if st.button("Run the operartion"):
        run_python_file(getcountry_script)  # Update the file path





