import cv2
import numpy as np

# Load the pre-trained Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to calculate average color of skin
def get_skin_color(face_region):
    # Convert the face region to the RGB color space (OpenCV uses BGR by default)
    face_region_rgb = cv2.cvtColor(face_region, cv2.COLOR_BGR2RGB)
    
    # Calculate the average color of the skin (mean of all pixels)
    avg_color = np.mean(face_region_rgb, axis=(0, 1))  # Mean along height and width
    return avg_color

# Start capturing from webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)
    
    # Convert to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # If a face is detected, extract the face region and calculate average skin color
    for (x, y, w, h) in faces:
        face_region = frame[y:y+h, x:x+w]
        
        # Calculate average skin color
        skin_color = get_skin_color(face_region)
        
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Display the average color as a rectangle beside the face
        color_bar = np.zeros((100, 200, 3), dtype=np.uint8)
        color_bar[:] = skin_color  # Fill with the average skin color
        frame[0:100, x+w+10:x+w+210] = color_bar  # Place the color bar next to the face
    
    # Display the frame with face detection and color shade
    cv2.imshow("Human Photo and Color Shade", frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
