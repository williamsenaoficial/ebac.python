# codigo: if / elif        / else
# significado: se / se não se / se não
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')

    print('Sistema Jarvis')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você nã0 digitou nem entrar e nem sair.')

print('FORA DOS BLOCOS')