import os
import pandas as pd
from model_training import classifica_imagem
from frame_capture import frame_capture

# Percorre todas as imagens na pasta 'imgs' e, uma por uma,
# verifica qual é o gesto atrelado à elas
# Junta todos esses resultados e retorna uma lista
def chama_classificacao():
    # Nome do vídeo sem extensão (precisa ser mp4)
    nome_video = input('Digite o nome do vídeo: ')
    frame_capture(nome_video)
    # Percorre o diretório onde estão os frames extraídos do vídeo
    lista_imagens = os.listdir('./imgs')
    lista_classificacao = []
    for imagem in lista_imagens:
        resultado = classifica_imagem('./imgs/'+imagem)
        # Ignora quando o resultado é 'parada' porque isso ainda não foi implementado
        if resultado != 'parada':
            lista_classificacao.append(resultado)
    
    return lista_classificacao

# Faz uma classificação bayesiana de todos os gestos computados
# para dizer qual é a frase dita
def classifica_gestos(lista_classificacao):
    gestos = pd.read_csv('./dataset/gestos.csv', encoding='ISO-8859-1')
    # Todos os gestos computados até o momento
    lista_de_gestos = {'ajuda_gesto1': 0, 'ajuda_gesto2': 0, 'alergia_gesto1': 0, 'alergia_gesto2': 0, 'banheiro_gesto1': 0, 
                        'banheiro_gesto2': 0, 'bom_dia_gesto1': 0, 'bom_dia_gesto2': 0, 'bom_dia_gesto3': 0, 'desculpa_gesto1': 0, 
                        'enjoo_gesto1': 0, 'enjoo_gesto2': 0, 'estou_mal_gesto1': 0, 'estou_mal_gesto2': 0, 'frase9_gesto1': 0, 
                        'frase9_gesto2': 0, 'meu_nome_e_gesto1': 0, 'meu_nome_e_gesto2': 0, 'por_favor_gesto1': 0}
    from sklearn.naive_bayes import MultinomialNB
    X = gestos[gestos.columns[1:]]
    # O gesto 'Parada' ainda não foi implementado
    X = X.drop(['parada'], axis=1)
    y = gestos['frase']
    modelo = MultinomialNB()
    modelo.fit(X, y)
    # Percorre todos os gestos recebidos pelo pela função chama_classificacao
    # e atualiza o dicionário 'lista_de_gestos' com o valor 1 em todo gesto que aparecer
    for gesto in lista_classificacao:
        lista_de_gestos.update({gesto: 1})

    lista = modelo.predict([list(lista_de_gestos.values())])
    return lista