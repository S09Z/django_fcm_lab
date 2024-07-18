import firebase_admin
from firebase_admin import credentials, firestore
import time

# Path to the firebase_credentials.json file
FIREBASE_CREDENTIALS = 'firebase_credentials.json'

# Initialize Firebase Admin SDK
cred = credentials.Certificate(FIREBASE_CREDENTIALS)
firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()

def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        print(f'Received message: {doc.to_dict()}')

def main():
    # Reference to the collection where messages are stored
    messages_ref = db.collection(u'messages')

    # Watch the collection
    print('Listening for new messages...')
    query_watch = messages_ref.on_snapshot(on_snapshot)

    # Keep the script running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('Listener stopped.')

if __name__ == '__main__':
    main()
