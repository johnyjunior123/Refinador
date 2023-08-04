CREATE TABLE ENDERECOS(
    ID_ENDERECO SMALLINT UNSIGNED PRIMARY KEY,
    TIPO_LOGRADOURO VARCHAR(30),
    LOGRADOURO VARCHAR(150) UNIQUE,
    BAIRRO VARCHAR(100),
    CIDADE VARCHAR(50),
    ESTADO VARCHAR(2),
    GEOLOCALIZACAO POINT
);

ALTER TABLE NOTICIA ADD (CRIME VARCHAR(50));
ALTER TABLE NOTICIA ADD COLUMN ID_ENDERECO SMALLINT UNSIGNED,
ADD CONSTRAINT FK_ID_ENDERECO
FOREIGN KEY (ID_ENDERECO) REFERENCES ENDERECOS(ID_ENDERECO);

