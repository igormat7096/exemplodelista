#cadastrar nomes na lista = [] 
nomes = []

#loop

while True:
    
    #tratamento de execesão

    try:
 
        #insere novo nome 
 
        novo_nome = input("Informe o novo nome ou 'Enter' para exibir a lista: ")
 
        #verificar se possui valor ou não 
 
        if novo_nome:
 
        #insere novo nome na lista
            nomes.append(novo_nome)
            print(f"{novo_nome} Cadastrado com sucesso!")
            continue
        else:
            break
    except Exception as e:
        print(f"Não foi possível cadastrar o nome. {e}.")


nomes.sort
for nome in nomes:
    print(nome)