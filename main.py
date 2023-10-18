import cv2
import mediapipe as mp

#
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# prendiamo il video
camera = cv2.VideoCapture(0)
image_to_overlay = cv2.imread('data/la_roccia.jpg')


with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while camera.isOpened():
        success, image = camera.read()
        if not success:
            print("Sorgente video non trovata.")
            continue

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]  # Prendiamo solo la prima mano

            # Coordinata X del pollice e dell'indice
            thumb_x = hand_landmarks.landmark[4].x
            index_x = hand_landmarks.landmark[8].x
            middle_x = hand_landmarks.landmark[12].x
            ring_x = hand_landmarks.landmark[16].x
            pinky_x = hand_landmarks.landmark[20].x
            

            # Calcola la distanza tra il pollice e l'indice
            distance12 = abs(thumb_x - index_x)
            distance23 = abs(index_x - middle_x)
            distance34 = abs(middle_x - ring_x)
            distance45 = abs(ring_x - pinky_x)

            # Sogliola per determimare la chiusura della mano
            threshold = 0.1

            if distance12 > threshold:
                hand_status = "Aperta"
                image_to_overlay = cv2.resize(image_to_overlay, (image.shape[1], image.shape[0]))

                # Sovrapposizione dell'immagine quando rileva che la mano è aperta
                image= cv2.addWeighted(image, 1, image_to_overlay, 0.8, 0)

            else:
                hand_status = "Chiusa"

            # Testo che visualizza lo stato della mano 
            cv2.putText(image, f"Mano: {hand_status}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # Disegna le landmarks delle mani
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow('Riconoscimento Mano', image)

        if cv2.waitKey(5) & 0xFF == 27:
            break

camera.release()
cv2.destroyAllWindows()
