# Step 1: Install Required Libraries
# Ensure you have Flask and face_recognition installed
# pip install flask face_recognition opencv-python

from flask import Flask, request, jsonify
import face_recognition
import numpy as np
import cv2
import os
import requests
from datetime import datetime

app = Flask(__name__)

# Load registered student faces (stored during registration)
KNOWN_FACES_DIR = 'known_faces'
known_face_encodings = []
known_face_names = []

# Load known faces from the directory
for filename in os.listdir(KNOWN_FACES_DIR):
    image_path = os.path.join(KNOWN_FACES_DIR, filename)
    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)
    
    if encodings:
        known_face_encodings.append(encodings[0])
        known_face_names.append(os.path.splitext(filename)[0])
    else:
        print(f"⚠️ Warning: No face found in {filename}")

# Attendance endpoint (your Java API)
ATTENDANCE_API_URL = "http://localhost:8080/SetAttendance"

@app.route('/verify-face', methods=['POST'])
def verify_face():
    try:
        # Get image from the request
        file = request.files['image']
        image_np = np.frombuffer(file.read(), np.uint8)
        img = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

        # Detect faces in the uploaded image
        face_encodings = face_recognition.face_encodings(img)

        if not face_encodings:
            return jsonify({"success": False, "message": "No face detected."})

        recognized_faces = []

        for uploaded_face_encoding in face_encodings:
            # Compare with known faces and get distances
            face_distances = face_recognition.face_distance(known_face_encodings, uploaded_face_encoding)
            best_match_index = np.argmin(face_distances)

            # Check if the closest match is within a safe threshold
            if face_distances[best_match_index] < 0.5:
                student_name = known_face_names[best_match_index]
                recognized_faces.append(student_name)

                # Send attendance record to your Java backend
                mark_attendance(student_name)

        if recognized_faces:
            return jsonify({"success": True, "recognized_faces": recognized_faces})
        else:
            return jsonify({"success": False, "message": "Face not recognized."})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

def mark_attendance(student_name):
    """Send attendance data to the Java backend."""
    try:
        data = {
            "student_name": student_name,
            "timestamp": datetime.now().isoformat(),
            "subject": "Java"
        }
        response = requests.post(ATTENDANCE_API_URL, json=data)

        if response.status_code == 200:
            print(f"✅ Attendance marked for {student_name}")
        else:
            print(f"❌ Error marking attendance: {response.text}")
    except Exception as e:
        print(f"❌ Attendance API error: {str(e)}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
