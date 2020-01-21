import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from os import getenv


def test_db_add(request):

    cert = getenv("KEY")
    cred = credentials.Certificate(cert)

    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://testproject-a749d.firebaseio.com/'
    })

    ref = db.reference('StudentsInfo')

    request_json = request.get_json()
    if request_json and 'StudentsInfo' in request_json:
        for i in request_json['StudentsInfo']:
            for stud in request_json['StudentsInfo'][i]:
                ref.child(i).push(stud)
        return "Data updated"
    else:
        return 'Error'
