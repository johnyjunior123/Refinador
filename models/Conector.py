import psycopg2

class Conector:
    
    def __init__(self, config):
        try:
            self.conexao = psycopg2.connect(user=config[0], password=config[1],host=config[2],database=config[3])
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