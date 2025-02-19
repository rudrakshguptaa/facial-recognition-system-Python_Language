import face_recognition  # Library for facial recognition
import cv2  # OpenCV for video capture and image processing
import csv  # For writing attendance data to CSV files
from datetime import datetime  # For date and time operations
import os  # For file and directory operations

# Function to load known face encodings and their corresponding names from a folder
def load_known_face_encodings(folder_path):
    known_face_encodings = []  # List to store face encodings
    known_face_names = []  # List to store corresponding names

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        name = os.path.splitext(filename)[0]  # Extract the name from the file name
        image_path = os.path.join(folder_path, filename)
        try:
            # Load the image and extract the face encoding
            face_image = face_recognition.load_image_file(image_path)
            face_encoding = face_recognition.face_encodings(face_image)[0]
            known_face_encodings.append(face_encoding)
            known_face_names.append(name)
        except Exception as e:
            print(f"Error loading {filename}: {e}")

    return known_face_encodings, known_face_names

# Function to create a new attendance folder for the current date
def create_attendance_folder():
    folder_name = datetime.now().strftime("%Y-%m-%d")  # Get the current date as folder name
    folder_path = os.path.join(os.getcwd(), folder_name)
    os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist
    return folder_path

# Initialize the video capture from the default camera (0)
video_capture = cv2.VideoCapture(0)

# Load known face encodings and names from the "Faces" folder
known_face_encodings, known_face_names = load_known_face_encodings("Faces")

# Create a list of students from the loaded face names
students = known_face_names.copy()

# Create an attendance folder for today and prepare the attendance CSV file
attendance_folder = create_attendance_folder()
attendance_csv_path = os.path.join(attendance_folder, "attendance.csv")
attendance_writer = csv.writer(open(attendance_csv_path, "w", newline=""))
attendance_writer.writerow(["Name", "Time"])  # Write the header row to the CSV file

# Font settings for displaying text on the video frames
font = cv2.FONT_HERSHEY_COMPLEX
font_scale = 1
font_color = (255, 255, 255)  # White text
background_color = (0, 0, 0)  # Black background
thickness = 3

# Coordinates for displaying text (top-left corner of the frame)
frame_corner = "top-left"
if frame_corner == "top-left":
    corner_x = 50
    corner_y = 50

# Prepare a separate CSV file to log unknown faces
unknown_csv_path = os.path.join(attendance_folder, "unknown.csv")
unknown_writer = csv.writer(open(unknown_csv_path, "w", newline=""))
unknown_writer.writerow(["Name", "Time"])  # Write the header row for unknown faces

# Start the main loop to capture video frames and perform facial recognition
while True:
    _, frame = video_capture.read()  # Capture a frame from the video
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)  # Resize frame for faster processing
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)  # Convert the frame to RGB

    # Detect face locations and encode the faces in the frame
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    # Iterate through each face found in the frame
    for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
        # Compare the face encoding with known face encodings
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.4)
        name = "Unknown"  # Default name if no match is found

        if True in matches:
            # Get the index of the first matching face and retrieve the corresponding name
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Log the student's attendance if they are recognized
        if name in students:
            students.remove(name)  # Remove the student to avoid duplicate entries
            current_time = datetime.now().strftime("%H:%M:%S")  # Get the current time
            attendance_writer.writerow([name, current_time])  # Log the student's attendance
        elif name == "Unknown":
            # Log unknown faces with the current time
            current_time = datetime.now().strftime("%H:%M:%S")
            unknown_writer.writerow([name, current_time])

        # Display the name on the frame
        text = f"Name: {name}"
        (text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, thickness)
        x = corner_x
        y = corner_y
        # Draw a rectangle behind the text
        cv2.rectangle(frame, (x, y - text_height - 5), (x + text_width + 5, y + 5), background_color, cv2.FILLED)
        # Put the text on the frame
        cv2.putText(frame, text, (x + 5, y), font, font_scale, font_color, thickness)

    # Display the frame with the recognized faces
    cv2.imshow("Attendance", frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture and close all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
