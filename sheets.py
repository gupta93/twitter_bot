import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_worksheet_object():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('API Project-4a4df87e3dcb.json', scope)

    gc = gspread.authorize(credentials)

    sh = gc.open('Twitter Data')
    sh.share('tushar.gp.93@gmail.com', perm_type='user', role='writer')
    #worksheet = sh.worksheet('worksheet2')
    worksheet = sh.add_worksheet(title="worksheet2")
    return worksheet

if __name__ == "__main__":
    get_worksheet_object()