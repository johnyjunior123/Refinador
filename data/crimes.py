equivalencia = [
    {"roubo" : ["roubo", "roubar", "roubado", "roubada", "assalto", "veículo levado", "locomoção levado", "assaltantes"]},
    {"furto" : ["furto", "furtar", "furtad",]},
    {"homicídio" : ["assassinato", "assassinad", "assassinados", "homicídio", "encontraram um corpo", "encontrando o cadáver", "baleado" , "acusado de matar", "morte","morta","morto", "encontrada mort", "óbito"]},
    {"estupro" : ["estrupo", "acusado de estuprar"]},
    {"sequestro" : ["sequestro", "desaparecimento", "desaparecido", "desapareceu"]},
    {"tentativa de homicídio" : ["agressão", "tentativa de homicídio", "agressão fisica", "tentativa de matar", "lesão corporal", "atentado", "ameaçar", "violência física", "troca de tiros", "disparo da arma de fogo", "disparos de arma de fogo", "acusado de agre"]},
    {"tráfico de drogas" : ["tráfico de drogas", "entorpecente", "crack", "maconha", "cocaína"]},
    {"estelionato" : ["estelionato", "golpe", "apropriação indébita"]},
    {"suicídio" : ["suicídio", "tentado contra sua vida"]},
    {"violencia contra mulher" : ["maria da penha", "agredir a própria esposa", "violência doméstica", "violência contra mulher", "agredida"]},
    {"assédio" : ["assédio","assédi"]},
    {"violência sexual" : ["violência sexual", "abuso infantil", "abuso",]},
    {"maus-tratos" : ["maus-tratos", "animais silvestres"]},
    {"acidente de trânsito" : ["atropelad", "acidente de trânsito", "embriagado"]},
    {"vandalismo" : ["dano a propriedade", "vandalismo", "confusão generalizada", "invadir", "perturbação do sossego"]},
    {"fake-news" : ["denunciação caluniosa", "apologia ao crime", "Disseminar fake news", "ataque a escola"]},
    {"porte de armas" : ["porte irregular de arma de fogo", "arma de fogo"]},
    {"pensão alimentícia" : ["pensão alimentícia"]},
    {"mandato em aberto" : ["mandado de prisão em aberto"]},
    {"desobediência" : ["desobedecerem uma ordem policial", "desacat"]}
]

crimes = [
    "roubo", 
    "furto", 
    "homicídio", #
    "estupro", #
    "sequestro", #
    "tentativa de homicídio", #
    "tráfico de drogas", #
    "estelionato", #
    "violência sexual",#
    "suicídio", #
    "violência contra mulher", #
    "maria da penha", #
    "assédio",#
    "assédi",
    "maus-tratos", #
    "acidente de trânsito", #
    "vandalismo", #
    "Disseminar fake news", #
    "porte irregular de arma de fogo", #
    "pensão alimentícia", #
    "mandado de prisão em aberto", #
    "desobedecerem uma ordem policial", #
    "abuso infantil", #
    "tentativa de matar", #
    "entorpecente", #
    "agredir a própria esposa", #
    "violência doméstica", #
    "roubar", 
    "roubado", 
    "roubada", 
    "assalto", #
    "furtar", 
    "furtad", #
    "atropelad", #
    "agressão",
    "assassinato",
    "assassinado",
    "assassinados", #
    "dano a propriedade", #
    "agressão fisica", #
    "abuso", #
    "denunciação caluniosa", #
    "desaparecimento", #
    "golpe", #
    "lesão corporal", #
    "embriagado", #
    "atentado", #
    "ameaçar", #
    "violência física", #
    "encontraram um corpo", #
    "troca de tiros", #
    "confusão generalizada", #
    "crack", #
    "cocaína", #
    "encontrando o cadáver", #
    "veículo levado", #
    "baleado", #
    "acusado de estuprar", #
    "acusado de matar", #
    "apologia ao crime", #
    "disparo da arma de fogo", #
    "disparos de arma de fogo", #
    "invadir", #
    "locomoção levado", #
    "desaparecido", #
    "morte", #
    "morta", #
    "morto", #
    "perturbação do sossego", #
    "ataque a escola", #
    "encontrada mort", #
    "desacat", #
    "acusado de agre", #
    "arma de fogo", #
    "desapareceu", #
    "assaltantes",
    "tentar matar", #
    "animais silvestres", #
    "óbito", #
    "apropriação indébita", #
    "agredida", #
    "tentado contra sua vida", #
]

# atualização do banco
# a 1º atualização através dos 30 primeiros tokens
# a 2º através dos 45
# a 3º através dos 66

print(len(equivalencia))
print(len(crimes))