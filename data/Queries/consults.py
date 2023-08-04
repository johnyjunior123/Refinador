def consultNoticiaBruta():
    return f"SELECT * FROM NOTICIA WHERE (URL LIKE '%PENEDO%' OR DESCRICAO LIKE '%PENEDO%');"

def consultCrimeBruto(crime):
    return f"SELECT URL FROM NOTICIA WHERE (URL LIKE '%Penedo%' OR DESCRICAO LIKE '%Penedo%') AND DESCRICAO LIKE '%{crime}%';"

def consultEnderecoBruto(tipo, endereco):
    return f"SELECT URL FROM NOTICIA WHERE (URL LIKE '%Penedo%' OR DESCRICAO LIKE '%Penedo%') AND DESCRICAO LIKE '%{tipo} {endereco}%';"

def consultEnderecoLograd(logradouro):
    return f"SELECT URL FROM NOTICIA WHERE (URL LIKE '%Penedo%' OR DESCRICAO LIKE '%Penedo%') AND DESCRICAO LIKE '%{logradouro}%';"

def consultEnderecos():
    return f"SELECT ID_ENDERECO, TIPO_LOGRADOURO, LOGRADOURO FROM ENDERECOS;"