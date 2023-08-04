def insertEndereco(endereco):
    return f"INSERT INTO ENDERECOS (TIPO_LOGRADOURO, LOGRADOURO, BAIRRO, CIDADE, ESTADO, GEOLOCALIZACAO) VALUES ('{endereco.tipo}', '{endereco.logradouro}', '{endereco.bairro}', '{endereco.cidade}', '{endereco.estado}', POINT({endereco.latlong[0]},{endereco.latlong[1]}));"

def insertNoticia(noticia):
    return f"""INSERT INTO NOTICIA (
        URL, DESCRICAO, DATA_NOTICIA, HORA, CRIME, GRAVIDADE, ID_ENDERECO) 
        VALUES (
            '{noticia.url}', 
            '{noticia.descricao}', 
            '{noticia.data}', 
            '{noticia.hora}', 
            '{noticia.crime}',
            '{noticia.id_endereco}');"""

