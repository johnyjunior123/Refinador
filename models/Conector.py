import psycopg2

class Conector:
    
    def __init__(self, config):
        try:
            self.conexao = psycopg2.connect(user="postgres",
                                            password="demon123",
                                            host="127.0.0.1",
                                            database="noticias")
            print('Conexão com Sucesso')
        except psycopg2.Error as error:
            print(error)
        
    def inserir(self, sql):
        cursor = self.conexao.cursor()
        try:
            cursor.execute(sql)
            self.conexao.commit()
            cursor.close()
        except psycopg2.Error as error:
            print(error)

    def consulta(self, sql):
        cursor = self.conexao.cursor()
        try:
            cursor.execute(sql)
            array = cursor.fetchall()
        except psycopg2.Error as error:
            print(error)
        finally:
            cursor.close()
        return array

    def encerrar(self):
        self.conexao.close()
        print('--- Encerrada com Sucesso - 200 ---')