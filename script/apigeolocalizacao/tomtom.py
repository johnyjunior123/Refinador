from requests import request
from keytomtom import key

def geocode(endereco):
    requisicao = request('GET', f"https://api.tomtom.com/search/2/geocode/{endereco}.json?key={key}")
    json = requisicao.json()
    return tratamento(json)

def tratamento(json):
    dadosComplementares = []
    try:
        dadosComplementares.append(json['results'][0]['address']['municipalitySubdivision'])
    except:
        dadosComplementares.append('nao encontrado')
    dadosComplementares.append(json['results'][0]['address']['municipality'])
    dadosComplementares.append(json['results'][0]['address']['countrySubdivision'])
    position = [json['results'][0]['position']['lat'], json['results'][0]['position']['lon']]
    if(dadosComplementares[0] == 'nao encontrado'):
        requisicao = request('GET', f"https://api.tomtom.com/search/2/reverseGeocode/{position[0]},{position[1]}.json?key={key}&radius=100")
        decoding = requisicao.json()
        try:
            dadosComplementares[0] = decoding['addresses'][0]['address']['municipalitySubdivision']
        except:
            print(json['results'][0]['address'])
    dadosComplementares.append(position)
    return dadosComplementares

print(geocode('povoado itaporanga ,penedo al'))