from frase_predict import chama_classificacao, classifica_gestos
from model_training import classifica_imagem

if __name__ == '__main__':
    print('Iniciando...')
    lista_classificacao = chama_classificacao()
    result = classifica_gestos(lista_classificacao)
    print('Resultado: ' +str(result[0]))