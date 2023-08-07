def updateCrime(crime, url):
    return f"UPDATE NOTICIA SET CRIME = '{crime}' WHERE CRIME IS NULL AND URL = '{url}'"

def updateEndereco(id_endereco, url):
    return f"UPDATE NOTICIA SET ID_ENDERECO = {id_endereco} WHERE ID_ENDERECO IS NULL AND URL = '{url}'"