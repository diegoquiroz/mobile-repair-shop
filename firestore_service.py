import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential)

db = firestore.client()


def get_users():
	return db.collection('users').get()


def get_user(user_id):
	return db.collection('users').document(user_id).get()


def set_appointment(brand, model, problem, problem_explanation, email):
	appointment_collection_ref = db.collection('appointments')
	appointment_collection_ref.add(
		{
			'brand': brand[0],
			'model': model[0],
			'problem': problem[0],
			'problem_explanation': problem_explanation,
			'email': email
		}
	)
