usuario_correto='admin'
senha_correta='1234'




usuario=input("\n"'Digite o usuario:  ')
senha=input('digite a senha:  ')
if usuario==usuario_correto and senha==senha_correta:
    print('login bem sucedido')
elif usuario != usuario_correto and senha == senha_correta:
    print('Usuario não encontrado!')
elif usuario == usuario_correto and senha != senha_correta:
    print('senha incorreta!')
else:
    print('Informações de login incorretas!')


print("\n"'fim do programa')