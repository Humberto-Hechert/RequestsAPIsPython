import requests

def main():
  print('#####################')
  print('#### CONSULTA CEP ###')
  print('#####################')

  cep = input('\nDigite o cep a ser consultado: ')

  if len(cep) != 8:
    print('CEP inválido')
    exit()

  req = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
  adress_data = req.json()

  if 'erro' in adress_data:
    print('\n{}, CEP não reconhecido!'.format(cep))
  else:
    print('\nCEP: {}'.format(adress_data['cep']))
    print('Rua: {}'.format(adress_data['logradouro']))
    print('Complemento: {}'.format(adress_data['complemento']))
    print('Bairro: {}'.format(adress_data['bairro']))
    print('Cidade: {}'.format(adress_data['localidade']))
    print('Estado: {}'.format(adress_data['uf']))

  print('-----------------------------------------')
  option = int(input('\nDeseja realizar uma nova consulta?\n1.Sim\n2.Não\n'))
  if option == 1:
    main()
  else:
    print('\nObrigado por utilizar nossa consulta!')

if __name__ == '__main__':
  main()