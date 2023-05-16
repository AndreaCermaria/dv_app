# JBI100 App

## About this app
Visualization app to explore outliers in the World Cup Dataset
## Requirements
- Python 3 (add it to your path (system variables) to make sure you can access it from the command prompt)
- Git (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## How to run this app
We suggest you to create a virtual environment for running this app with Python 3. Clone this repository
and open your terminal/command prompt in the root folder.
download a zip file of this folder, unzip it and copy it to a folder of choice on your computer
open a command prompt and run the following commands:

1. Open your terminal/command prompt and navigate to the `dv_app` folder.

2. Create a virtual environment:
   - In Windows:
     ```
     > python -m venv venv
     > venv\Scripts\activate
     ```
   - In Unix system:
     ```
     > python -m venv venv
     > source venv/bin/activate
     ```

   (Note: If `python` is not recognized, use `python3` instead.)

   Alternatively, if you're using Anaconda or Miniconda, you can create and activate a conda environment:
     ```
     > conda create -n yourenvname
     > conda activate yourenvname
     ```
   
3. Install all the required packages by running:
     ```
     > pip install -r requirements.txt
     ```

4. Run the app locally:
     ```
     > python index.py
     ```
   
5. You will get an HTTP link. Open this link in your browser to see the results. You can edit the code in any editor (e.g., PyCharm) and when you save it, you will see the results in the browser.

## Resources
- Dash (https://dash.plotly.com/)

