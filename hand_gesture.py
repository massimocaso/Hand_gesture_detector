def hand_status(hand_landmarks):
    wrist_x = hand_landmarks.landmark[0].x

    # Coordinata X del pollice e dell'indice
    index_x = hand_landmarks.landmark[8].x
    middle_x = hand_landmarks.landmark[12].x
    ring_x = hand_landmarks.landmark[16].x
    pinky_x = hand_landmarks.landmark[20].x

    # Calcolo la distanza tra il pollice e l'indice
    distance_index = abs(wrist_x - index_x)
    distance_middle = abs(wrist_x - middle_x)
    distance_ring = abs(wrist_x - ring_x)
    distance_pinky = abs(wrist_x - pinky_x)

    # Soglia per determimare la chiusura della mano
    threshold = 0.03

    if distance_index and distance_middle and distance_ring and distance_pinky > threshold:
        return "Aperta"
    else:
        return "Chiusa"


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