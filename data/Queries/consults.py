def consultNoticiaBruta():
    return f"SELECT * FROM NOTICIA WHERE (URL ILIKE '%PENEDO%' OR DESCRICAO ILIKE '%PENEDO%');"

def consultCrimeBruto(crime):
    return f"SELECT URL FROM NOTICIA WHERE (URL ILIKE '%Penedo%' OR DESCRICAO ILIKE '%Penedo%') AND DESCRICAO ILIKE '%{crime}%';"

def consultEnderecoBruto(tipo, endereco):
    if(len(endereco) == 1):
        return f"SELECT URL FROM NOTICIA WHERE (URL ILIKE '%Penedo%' OR DESCRICAO ILIKE '%Penedo%') AND (DESCRICAO ILIKE '%{tipo} {endereco} %' OR DESCRICAO ILIKE '%{tipo} {endereco},%' OR DESCRICAO ILIKE '%{tipo} {endereco}.%');"
    return f"SELECT URL FROM NOTICIA WHERE (URL ILIKE '%Penedo%' OR DESCRICAO ILIKE '%Penedo%') AND DESCRICAO ILIKE '%{tipo} {endereco}%';"

def consultEnderecoLograd(logradouro):
    if(len(logradouro) == 1):
        # return f"SELECT URL FROM NOTICIA WHERE (URL ILIKE '%Penedo%' OR DESCRICAO ILIKE '%Penedo%') AND (DESCRICAO ILIKE '% {logradouro} %' OR DESCRICAO ILIKE '%{logradouro},%' OR DESCRICAO ILIKE '%{logradouro}.%') AND ID_ENDERECO IS NULL;"
        return KeyError
    return f"SELECT URL FROM NOTICIA WHERE (URL ILIKE '%Penedo%' OR DESCRICAO ILIKE '%Penedo%') AND DESCRICAO ILIKE '% {logradouro}%' AND ID_ENDERECO IS NULL;"

def consultEnderecos():
    return f"SELECT ID_ENDERECO, TIPO_LOGRADOURO, LOGRADOURO FROM ENDERECOS;"