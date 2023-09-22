import requests

class Get_comments:
    array_publicacoes = []
    id_publicacao = '' # Substitua pelo ID da sua publicação
    access_token = 'EAALpZAgFrRJMBO8IpVE8cqFxpi22tnYPsnVRBqlFnlhirbhdiKwfeIWw2LFNkdIhqXQpkCbzLYVUhIhZBJ81ZCzvpGfeeuMZBfpF1cQ5XS1ZAysPDXtnVmm4eWlDCj7yTn93sZCK9gA2hnZCRBMq0coSRTc7nx8ClVqsuQ5kv1DlWYfl9yuw6cCBZAxsSgCYqRwD0po8YNTB3CABs9xGLcPMQZCEmNnSMb3KakH4ZD'  # Substitua pelo seu token de acesso

    url = f'https://graph.facebook.com/{id_publicacao}/comments?access_token={access_token}'

    def get_comments_http(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Lançará uma exceção se a resposta for um erro HTTP

            comentarios = response.json()
            print(comentarios)

            
            # Itera sobre os comentários e os imprime
            for comentario in comentarios['data']:
                print(f"Data e Hora de Post: {comentario['timestamp']}")
                print(f"Comentário: {comentario['text']}")
                print(f"ID: {comentario['id']}")

        except requests.exceptions.RequestException as e:
            print(f"Erro durante a solicitação: {e}")
        except requests.exceptions.HTTPError as e:
            print(f"Erro HTTP: {e}")
        except ValueError as e:
            print(f"Erro ao analisar a resposta JSON: {e}")

if __name__ == '__main__':
    run = Get_comments()
    run.get_comments_http()
