import mysql.connector

class Conector:
    
    def __init__(self, config):
        try:
            self.conexao = mysql.connector.connect(**config)
            print('Conexão com Sucesso')
        except mysql.connector.Error as error:
            print(error)
        
    def inserir(self, sql):
        cursor = self.conexao.cursor()
        try:
            cursor.execute(sql)
            self.conexao.commit()
            cursor.close()
        except mysql.connector.Error as error:
            print(error)

    def consulta(self, sql):
        cursor = self.conexao.cursor()
        try:
            cursor.execute(sql)
            array = cursor.fetchall()
        except mysql.connector.Error as error:
            print(error)
        finally:
            cursor.close()
        return array

    def encerrar(self):
        self.conexao.close()
        print('--- Encerrada com Sucesso - 200 ---')





