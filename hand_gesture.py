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
