pip install -r requirements.txt
python twitter.py -> to fetch data
&
python process.py -> to process data

uses rabbitmq server to publish and consume twitter data.
and python gspread module to push the data to spreadsheet.