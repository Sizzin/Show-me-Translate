import cv2
import numpy as np


# Usa a biblioteca Opencv Python para ler o vídeo e
# capturar alguns frames em imagens
def frame_capture(nome_video):
    # Utiliza o vídeo que estiver dentro do diretório "video"
    video = cv2.VideoCapture('./video/'+str(nome_video)+'.mp4')
    counter = 0

    while True:
        check, frame = video.read()
        frame_array = np.array(frame)
        
        if not check:
            break
        # Pega um frame a cada 15 frames
        if (counter > 0 and counter % 15 == 0):
            # resize = cv2.resize(frame, (640, 480))
            cv2.imshow('Capturando...', frame)
            # Cria uma imagem do frame atual
            cv2.imwrite('./imgs/'+str(counter)+'.png', frame)
            key = cv2.waitKey(10)
            # A tecla 'q' do teclado encerra o programa
            if key==ord('q'):
                break
        counter += 1

    video.release()
    cv2.destroyAllWindows