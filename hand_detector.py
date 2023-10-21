import cv2
import mediapipe as mp
import hand_gesture as hg


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# prendiamo il video
camera = cv2.VideoCapture(0)
image_to_overlay = cv2.imread('data/la_roccia.jpg')


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
                

                # Cordinate landmarks del pollice e dell'indice
                cv2.putText(image, hg.okay_gesture(hand_landmarks), (10, image.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 2)
                
                hand_status = hg.volume_mute(hand_landmarks)
                # Testo che visualizza lo stato della mano 
                cv2.putText(image, f"Comando: {hand_status}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
                # Disegna le landmarks delle mani
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)


        # cv2.namedWindow('Riconoscimento Mano', cv2.WND_PROP_FULLSCREEN)
        # cv2.setWindowProperty('Riconoscimento Mano', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        cv2.imshow('Riconoscimento Mano', image)

        if cv2.waitKey(5) & 0xFF == 27:
            break

camera.release()
cv2.destroyAllWindows()

# Sovrapposizione dell'immagine quando rileva una certa posizione della mano
#image_to_overlay = cv2.resize(image_to_overlay, (image.shape[1], image.shape[0]))

# Sovrapposizione dell'immagine quando rileva che la mano è aperta
#image= cv2.addWeighted(image, 1, image_to_overlay, 0.8, 0)