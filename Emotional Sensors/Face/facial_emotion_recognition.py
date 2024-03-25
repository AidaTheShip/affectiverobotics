import cv2
from deepface import DeepFace

emotion_labels = ['neutral', 'angry', 'fear', 'disgust', 'surprise', 'sad', 'happy']
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # used to detect faces in the frame
model = DeepFace.build_model("Emotion") ## Deep face has a pre-trained emotional classification model

# Capturing the video - note that the number parameter determines which camera it'll try to access. If 1 does not work, try switching to 0. 
cap = cv2.VideoCapture(1) 

while True:
    ret, frame = cap.read()

    # converting frame to grayscale for face detection
    grayed = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(grayed, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # extracting hte interesting region of interest from our boundary
        color_face = frame[y:y + h, x:x + w]

        resized_face = cv2.resize(color_face, (48, 48), interpolation=cv2.INTER_AREA)
        norm_face = resized_face / 255.0

        norm_face = norm_face.astype('float32') # we are setting the noramlized face as float.
        
        reshaped_face = norm_face.reshape(1, 48, 48, 3)  # we are reshaping the captured face to fit the model.
        predicted_emotions = model.predict(reshaped_face) # this predicts the emotions that are being felt.
        emotion_idx = predicted_emotions.argmax() # taking the one that has the highest probability fo showing up
        emotion = emotion_labels[emotion_idx]
        
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 4)

    cv2.imshow('Emotion Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() # this releases the capture and closes all the windos
cv2.destroyAllWindows()
