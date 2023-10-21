import pyautogui as pg
import math

hand_closed = False
timer = 0

def volume_mute(hand_landmarks):
    global hand_closed, timer
    
    wrist_x, wrist_y, wrist_z = get_landmark_3d(hand_landmarks, 0)
    index_x, index_y, index_z = get_landmark_3d(hand_landmarks, 8)
    middle_x, middle_y, middle_z = get_landmark_3d(hand_landmarks, 12)
    ring_x, ring_y, ring_z = get_landmark_3d(hand_landmarks, 16)
    pinky_x, pinky_y, pinky_z = get_landmark_3d(hand_landmarks, 20)

    distance_index = abs(index_y - wrist_y)
    distance_middle = abs(middle_y - wrist_y)
    distance_ring = abs(ring_y - wrist_y)
    distance_pinky = abs(pinky_y - wrist_y)

    # Soglia per determinare la chiusura della mano
    threshold = 0.2

    fingers = []
    check = [1, 2, 3, 4]

    if distance_index < threshold:
        fingers.append(1)
    else:
        fingers.append(0)

    if distance_middle < threshold:
        fingers.append(2)
    else:
        fingers.append(0)

    if distance_ring < threshold:
        fingers.append(3)
    else:
        fingers.append(0)

    if distance_pinky < threshold:
        fingers.append(4)
    else:
        fingers.append(0)

    if fingers == check and not hand_closed:
        # Esegui il comando solo se la mano è chiusa e non è già stata chiusa prima
        pg.press('volumemute')
        hand_closed = True
        timer = 5  # Imposta il timer a 5 secondi
        return "Volume Mute"
    
    if timer > 0:
        timer -= 1
    else:
        hand_closed = False


def get_direction(hand_landmarks):
   
    wrist_x, wrist_y, wrist_z = get_landmark_3d(hand_landmarks, 0)
    index_x, index_y, index_z = get_landmark_3d(hand_landmarks, 8)
    middle_x, middle_y, middle_z = get_landmark_3d(hand_landmarks, 12)
    ring_x, ring_y, ring_z = get_landmark_3d(hand_landmarks, 16)
    pinky_x, pinky_y, pinky_z = get_landmark_3d(hand_landmarks, 20)

    wrist = (wrist_x, wrist_y, wrist_z)
    index_tip = (index_x, index_y, index_z)
    middle_tip = (middle_x, middle_y, middle_z)

    # Calcolo del vettore
    vector = (index_tip[0] - wrist[0], index_tip[1] - wrist[1], index_tip[2] - wrist[2])

    # Normalizzazione del vettore
    length = math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)
    normalized_vector = (vector[0] / length, vector[1] / length, vector[2] / length)

    # Calcolo dell'angolo rispetto all'asse x (in radianti)
    angle = math.atan2(normalized_vector[1], normalized_vector[0])

    # Converte l'angolo in gradi
    angle_degrees = math.degrees(angle)

    if -45 <= angle_degrees <= 45:
        return "Right"
    elif 45 < angle_degrees <= 135:
        return "Down"
    elif -135 <= angle_degrees < -45:
        return "Up"
    else:
        return "Left"
  

def get_landmark_3d(hand_landmarks, landmark_id):
    landmark = hand_landmarks.landmark[landmark_id]
    return landmark.x, landmark.y, landmark.z


def okay_gesture(hand_landmarks):

    wrist_x, wrist_y, wrist_z = get_landmark_3d(hand_landmarks, 0)  # polso
    thumb_x, thumb_y, thumb_z = get_landmark_3d(hand_landmarks, 4)  # pollice
    index_x, index_y, index_z = get_landmark_3d(hand_landmarks, 8)  # indice
    middle_x, middle_y, middle_z = get_landmark_3d(hand_landmarks, 12) # indice
    ring_x, ring_y, ring_z = get_landmark_3d(hand_landmarks, 16) # indice
    pinky_x, pinky_y, pinky_z = get_landmark_3d(hand_landmarks, 20) # indice

    # Calcoliamo le direzioni lungo gli assi X, Y e Z
    direction_x = index_x - thumb_x
    direction_y = index_y - thumb_y
    direction_z = index_z - thumb_z

    
    '''coordinate tridimensionali di alcune landmarks (direzioni) appunti
                direction_x: Questa variabile rappresenta la direzione lungo l'asse X ed è calcolata sottraendo la coordinata X 
                del pollice dalla coordinata X dell'indice. 
                - se positiva, indica che l'indice è a destra del pollice lungo l'asse X 
                - se negativa, indica che l'indice è a sinistra del pollice lungo l'asse X.

                direction_y: Questa variabile rappresenta la direzione lungo l'asse Y ed è calcolata sottraendo la coordinata Y 
                del pollice dalla coordinata Y dell'indice.
                - se positiva, indica che l'indice è sopra al pollice lungo l'asse Y 
                - se negativa, indica che l'indice è sotto al pollice lungo l'asse Y.

                direction_z: Questa variabile rappresenta la direzione lungo l'asse Z ed è calcolata sottraendo la coordinata Z 
                del pollice dalla coordinata Z dell'indice. 
                - se direction_z è positiva, indica che l'indice è più vicino alla fotocamera rispetto al pollice lungo l'asse Z 
                - se è negativa, indica che l'indice è più lontano rispetto al pollice lungo l'asse Z.

                sottrarre cordinate x delle dita per determinare se si sta facendo "okay" con la mano
                '''
    

    return (f"Direzione X: {direction_x}, Direzione Y: {direction_y}, Direzione Z: {direction_z}")