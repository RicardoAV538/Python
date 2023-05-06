from time import sleep #Biblioteca oara o programa esperar um tempo antes de executar cada função
saldo = 0
limite = 500 # Limite de valor por saque
extrato = confirmacao = ""
numero_saques = 0
LIMITE_SAQUES = 3 # Limite de saques diários

menu = '''

      Seja bem-vindo ao Banco DIO !!

Escolha a função desejada:

  [d] Depositar
  [s] Sacar
  [e] Extrato
  [q] Sair
  
=> '''

while True:
  sleep(1)
  opcao = input(menu)
  
  if opcao == "d": #Condicional para o depósito
    print("Depósito\n")
    sleep(1)
    
    #Condicional para depósito
    sleep(1)
    deposito = int(input("Digite o valor que deseja depositar: R$"))
    
    if deposito > 0:
      saldo += deposito
      extrato += f"Depósito = R${deposito:.2f}\n"   #Adiciona o depósito ao histórico do extrato
      sleep(1)
      print("Depósito efetuado com sucesso!!")

    else:
      print("Valor informado não reconhecido, favor tentar novamente.")

  elif opcao == "s": #Condicional para o saque
    print("Saque\n")
    sleep(1)
    
    saque = int(input("Digite o valor que deseja sacar: R$"))
    
    excedeu_valor = saldo < saque
    
    excedeu_saque = numero_saques >= LIMITE_SAQUES
    
    if saque > 0:
      
      if excedeu_valor:  #Limite de saque: 500 reais por saque
        print("Saldo insuficiente")
        sleep(1.5) 
        
      elif saque > 500:
        print("Limite de valor por saque: R$500,00")
        sleep(1.5) 

      elif excedeu_saque:
        print("Número máximo de saques excedido")
        sleep(1.5) 

      else:
        saldo -= saque
        numero_saques += 1
        extrato += f"Saque = R${saque:.2f}\n" #Adiciona o saque ao histórico do extrato
        print("Saque efetuado com sucesso!!")
    else:
      print("Valor informado não reconhecido, favor tentar novamente.")

  elif opcao == "e": #Condicional para o extrato
    print("================= EXTRATO =================") #Centraliza a mensagem
    sleep(1)
    print('Não houveram movimentações em sua conta' if not extrato else extrato) #Mostra todas as operações feitas (saques e depósitos)
    
    print(f"Seu saldo atual é de: R${saldo:.2f}")
    print('=' * 43)
    sleep(4)

  elif opcao == "q":
    print("Sair\n")
    sleep(1)
    break

  else:
    print("Operação Inválida, selecione novamente a opção que deseja.")

