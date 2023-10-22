import pyautogui as pg
import math

hand_closed = False
timer = 0

def volume_control(hand_landmarks):
    global hand_closed, timer

    # Array di check per la dita
    check_close = [1, 2, 3, 4]
    check_12 = [0, 0, 3, 4]
    fingers = finger_status(hand_landmarks)
    hand_direction = get_direction(hand_landmarks)
    
    # Gesture per mutare il volume
    if fingers == check_close and hand_direction == "Up" and not hand_closed:
        # Esegue il comando solo se la mano è chiusa e non è già stata chiusa prima
        pg.press('volumemute')
        hand_closed = True
        timer = 5  # Imposta il timer a 5 secondi
        return "Volume Mute"
    
    #Gesture per alzare il volume
    if fingers == check_12 and hand_direction == "Up":
        pg.press('volumeup')
        timer = 5
        return "Volume Up"
    
    # Gesture per diminuire il volume
    if fingers == check_12 and hand_direction == "Down":
        pg.press('volumedown')
        timer = 5
        return "Volume down"
    
    if timer > 0:
        timer -= 1
    else:
        hand_closed = False

def finger_status(hand_landmarks):
    '''
    Questa funzione determina lo stato delle dita della mano (aperte o chiuse) in base alla direzione della mano..

    I treshold sono una soglia (distanza) che le dita devono raggiungere per essere considerate chiuse

    Restituisce:
        Una lista di valori (0 o il numero corrispondente del dito) che rappresenta lo stato delle dita 
        (1/2/3/4 per dita chiuse, 0 per dita aperte).
    '''
    # Coordinate delle dita
    wrist_x, wrist_y, wrist_z = get_landmark_3d(hand_landmarks, 0)
    index_x, index_y, index_z = get_landmark_3d(hand_landmarks, 8)
    middle_x, middle_y, middle_z = get_landmark_3d(hand_landmarks, 12)
    ring_x, ring_y, ring_z = get_landmark_3d(hand_landmarks, 16)
    pinky_x, pinky_y, pinky_z = get_landmark_3d(hand_landmarks, 20)

    direction = get_direction(hand_landmarks)
    # Soglia per determinare la chiusura della mano
    threshold = 0
    fingers = []

    if direction == "Up":  
        threshold = 0.2
        distance_index = abs(index_y - wrist_y)
        distance_middle = abs(middle_y - wrist_y)
        distance_ring = abs(ring_y - wrist_y)
        distance_pinky = abs(pinky_y - wrist_y)

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
    elif direction == "Down":
        threshold = 0.22
        distance_index = abs(wrist_y - index_y)
        distance_middle = abs(wrist_y - middle_y)
        distance_ring = abs(wrist_y - ring_y)
        distance_pinky = abs(wrist_y - pinky_y)

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
    elif direction == "Right":
        threshold = 0.2
        distance_index = abs(wrist_x - index_x)
        distance_middle = abs(wrist_x - middle_x)
        distance_ring = abs(wrist_x - ring_x)
        distance_pinky = abs(wrist_x - pinky_x)

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
    elif direction == "Left":
        threshold = 0.2
        distance_index = abs(index_x - wrist_x)
        distance_middle = abs(middle_x- wrist_x)
        distance_ring = abs(ring_x - wrist_x)
        distance_pinky = abs(pinky_x - wrist_x)

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
        
    return fingers

def get_direction(hand_landmarks):
   
    '''
    Questa funzione calcola la direzione in cui punta la mano utilizzando i landmark delle mani rilevati.
    
    Parametri:
        - hand_landmarks: I landmark delle mani rilevati con mediapipe
    
    Restituisce:
        Una stringa che rappresenta la direzione in cui la mano è orientata ("Right" per destra, "Down" per il basso,
        "Up" per l'alto, "Left" per sinistra).
    '''

    wrist_x, wrist_y, wrist_z = get_landmark_3d(hand_landmarks, 0)
    index_x, index_y, index_z = get_landmark_3d(hand_landmarks, 8)
    middle_x, middle_y, middle_z = get_landmark_3d(hand_landmarks, 12)
    ring_x, ring_y, ring_z = get_landmark_3d(hand_landmarks, 16)
    pinky_x, pinky_y, pinky_z = get_landmark_3d(hand_landmarks, 20)

    wrist = (wrist_x, wrist_y, wrist_z)
    index_tip = (index_x, index_y, index_z)
    middle_tip = (middle_x, middle_y, middle_z)

    # Calcola un vettore che rappresenta la direzione dalla punta dell'indice al polso.
    vector = (index_tip[0] - wrist[0], index_tip[1] - wrist[1], index_tip[2] - wrist[2])

    # Normalizzazione del vettore
    length = math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)
    normalized_vector = (vector[0] / length, vector[1] / length, vector[2] / length)

    # Calcolo dell'angolo rispetto all'asse x (in radianti) rispetto al vettore normalizzato
    angle = math.atan2(normalized_vector[1], normalized_vector[0])
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


def next_gesture(hand_landmarks):
    global hand_closed, timer

    check_close = [0, 2, 3, 4]
    fingers = finger_status(hand_landmarks)
    hand_direction = get_direction(hand_landmarks)
    
    # Gesture per mutare il volume
    if fingers == check_close and hand_direction == "Right" and not hand_closed:
        # Esegue il comando solo se la mano è chiusa e non è già stata chiusa prima
        pg.press('right')
        hand_closed = True
        timer = 20  # Imposta il timer a 5 secondi
        return "Freccia destra"
    
    #Gesture per alzare il volume
    if fingers == check_close and hand_direction == "Left" and not hand_closed:
        pg.press('left')
        timer = 20
        return "Freccia sinistra"
  
    if timer > 0:
        timer -= 1
    else:
        hand_closed = False