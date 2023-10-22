import cv2
import mediapipe as mp
import hand_gesture as hg


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Recuperiamo la sorgente video
camera = cv2.VideoCapture(0)


with mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
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
            #hand_landmarks = results.multi_hand_landmarks[0]  # Prendiamo solo la prima mano

            for hand_landmarks in results.multi_hand_landmarks:
                # Mettiamo a schermo lo stato delle dita
                hg.volume_control(hand_landmarks)
                hand_status = hg.get_direction(hand_landmarks)
                hg.next_gesture(hand_landmarks)
                fingers = hg.finger_status(hand_landmarks)
                index = fingers[0]
                middle = fingers[1]
                ring = fingers[2]
                pinky = fingers[3]
                cv2.putText(image, f"Index: {index} | Middle: {middle}| Ring: {ring}| Pinky: {pinky}", (10, image.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 2)
                # Testo che visualizza lo stato della mano 
                cv2.putText(image, f"Direzione: {hand_status}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
                # Disegna le landmarks delle mani
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow('Riconoscimento Mano', image)

        if cv2.waitKey(5) & 0xFF == 27:
            break

camera.release()
cv2.destroyAllWindows()