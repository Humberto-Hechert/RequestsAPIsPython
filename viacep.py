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
    for i in adress_data:
      print('\n{}: {}'.format(i, adress_data[i]))

  print('-----------------------------------------')
  option = int(input('\nDeseja realizar uma nova consulta?\n1.Sim\n2.Não\n'))
  if option == 1:
    main()
  else:
    print('\nObrigado por utilizar nossa consulta!')

if __name__ == '__main__':
  main()