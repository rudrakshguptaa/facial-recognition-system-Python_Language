******Facial Recognition Attendance System******

****Project Overview****

This project is a real-time attendance system using facial recognition technology. It identifies and records attendance for known faces from a live video feed, with separate logs for unknown faces.

****Key Features****
Real-Time Face Recognition: Identifies faces from a live webcam feed in real-time.
Attendance Logging: Logs recognized faces along with the time of attendance in attendance.csv.
Unknown Face Logging: Logs unidentified faces in unknown.csv for future reference.
Attendance Folders: Automatically creates a folder with the current date to store attendance records.
Dynamic Face Addition: Easily add new faces to the system by placing images in the Faces folder.

****Project Outputs****
Attendance Records: A CSV file named attendance.csv containing the names and times of recognized attendees.
Unknown Face Logs: A CSV file named unknown.csv containing entries for faces that were not recognized.
Date-Based Storage: Each day’s attendance data is saved in a separate folder named with the current date.

****Visualizations****
Name Overlays: Each detected face is labeled with its corresponding name or marked as "Unknown" in the video feed.
Bounding Box: Displays a rectangular box around detected faces to indicate successful face recognition.

****Benefits****
Automation: Automates attendance-taking, saving time and reducing manual effort.
Accuracy: Ensures accurate attendance recording with facial recognition.
Security: Logs unknown faces for review, enhancing system security.

****Usage Instructions****
**Prerequisites:**
-->Install Python 3.7 or higher.
-->Ensure cmake is installed on your system.

**Data Preparation:**
-->Create a folder named Faces in the project directory.
-->Add face images to the Faces folder, with the image name matching the person’s name (e.g., Rudraksh.jpg).

**Run the System:**
-->Execute the following command to start the attendance system: face_regocnition_system.py OR by click run the py file.
Stopping the System:
-->Press q to stop the system and save attendance records.

****Contributions****
Contributions are welcome! Here's how you can contribute:

Fork the Repository: Create a fork to make changes without affecting the main repository.
Create a Branch: Create a new branch for each feature or bug fix.
Submit a Pull Request: Once changes are complete, submit a pull request with a clear description.
Coding Standards: Follow PEP 8 for Python code style.
Documentation: Update the documentation if your changes affect project usage.

****Additional Notes****
Data Privacy: Ensure compliance with privacy laws and policies when using personal face images.
Customization: The project can be extended or modified to meet specific business or personal requirements.
Collaboration: We encourage collaboration to improve and expand the project.
By leveraging this facial recognition attendance system, organizations can improve attendance management, enhance accuracy, and streamline operations.
