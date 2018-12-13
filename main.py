from frase_predict import classifica_gestos
from model_training import classifica_imagem, initialize_tensorflow
from frame_capture import frame_capture

if __name__ == '__main__':
    print('Iniciando...')
    nome_video = input('Digite o nome do vídeo: ')
    initialize_tensorflow()
    lista_classificacao = frame_capture(nome_video)
    result = classifica_gestos(lista_classificacao)
    print('Resultado: ' +str(result[0]))