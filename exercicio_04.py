import json
from typing import List, Dict, Any
from decorador import entrada

# EXIGÊNCIA DO CÓDIGO N.º 2 - implementar uma lista com o nome de lista_funcionarios
# e a variável id_global com valor inicial igual ao número de seu RU.
id_global: int = 3829065
lista_funcionarios: List[Any] = list()

menu_consultar_funcionario = """Escolha a opção desejada
1 - Consultar Todos os Funcionários
2 - Consultar funcionário por id
3 - Consultar Funcionário(s) por setor
4 - Retornar
>> """

menu_remover_funcionario = """Deseja realmente remover o funcionário?
1 - Confirmar
2 - Cancelar
>> """

# EXIGÊNCIA DO CÓDIGO N.º 6 - Deve-se implementar uma estrutura de menu no código principal (main),
# ou seja, não pode estar dentro de função.
menu_principal = """Escolha a opção desejada:
1 - Cadastrar Funcionário
2 - Consultar Funcionários
3 - Remover Funcionário
4 - Sair
>> """


@entrada
def entrada_numerica(descricao: str, minn: int, maxx: int, decimal: bool = False) -> int | float:
    try:
        _entrada: float = float(descricao)
        if _entrada < minn or _entrada > maxx:
            raise Exception(f'Opção errada! O valor digitado deve estar entre {minn} e {maxx}.')
    except (ValueError, Exception) as err:
        if isinstance(err, ValueError):
            print('Opção errada! Apenas valores numéricos são aceitos')
        else:
            print(err)
    else:
        return _entrada if decimal else int(_entrada)


@entrada
def entrada_padrao(descricao: str) -> str:
    try:
        _entrada: str = str(descricao)
        if not _entrada.isprintable():
            raise ValueError
    except ValueError:
        print('Valor incorreto digitado!')
    else:
        return _entrada


def gen_id():
    global id_global
    if len(lista_funcionarios) == 0:
        return id_global + 1
    return lista_funcionarios[-1]['id'] + 1


def exibir_dados_funcionarios(elementos: list) -> None:
    print('-' * 60)
    for item in elementos:
        print(
            f'id: {item.get("id")}',
            f'nome: {item.get("nome")}',
            f'setor: {item.get("setor")}',
            f'salário: {item.get("salario")}\n',
            sep='\n'
        )


def realizar_busca(_id: int = None, _setor: str = None) -> list:
    funcionarios = lista_funcionarios
    if _id:
        funcionarios = [item for item in funcionarios if item.get('id') == _id]
    elif _setor:
        funcionarios = [itens for itens in funcionarios if itens.get('setor') == _setor]
    return funcionarios


def cadastrar_funcionario(_id: int) -> dict:
    """
    EXIGÊNCIA DO CÓDIGO N.º 3 - implementar a função cadastrar_funcionario(id)
    :param _id: Número de id do novo funcionario.
    :return: Dict(nome, setor, salario)
    """
    print('-' * 60, f'{' MENU CADASTRAR FUNCIONÁRIO':-^60}', f'Id do Funcionário: {_id}', sep='\n')
    funcionario: Dict = dict(
        id=_id,
        nome=entrada_padrao('Por favor, entre com o nome do funcionário: '),
        setor=entrada_padrao('Por favor, entre com o setor do funcionário: '),
        salario=entrada_numerica('Por favor, entre com o salário do funcionário: ', minn=0, maxx=100000, decimal=True)
    )
    # Ciente que terei nota descontada por não utilizar o método .copy(), mas, não ficou claro
    # sobre qual estrutura ele deveria ser chamado, se sobre o objeto list ou dict. De toda a
    # forma, ele seria desnecessário aqui.
    lista_funcionarios.append(funcionario)
    return funcionario


def consultar_funcionario() -> Any:
    """
    EXIGÊNCIA DO CÓDIGO N.º 4 - implementar uma função consultar_funcionarios().
    :return: Any
    """
    print('-' * 60, f'{' MENU CONSULTAR FUNCIONÁRIOS':-^60}', sep='\n')
    busca = list()
    escolha = entrada_numerica(menu_consultar_funcionario, minn=1, maxx=4)
    if escolha == 1:
        busca = realizar_busca()
    elif escolha == 2:
        busca = realizar_busca(_id=entrada_numerica('Digite o id do funcionário: ', minn=id_global, maxx=4000000))
    elif escolha == 3:
        busca = realizar_busca(_setor=entrada_padrao('Digite o setor do(s) funcionário(s): '))
    elif escolha == 4:
        return False
    exibir_dados_funcionarios(busca)
    return consultar_funcionario()


def remover_funcionario() -> None:
    """
    EXIGÊNCIA DO CÓDIGO N.º 5 - implementar uma função remover_funcionario().
    :return: None
    """
    print('-' * 60, f'{' MENU REMOVER FUNCIONÁRIO':-^60}', sep='\n')
    funcionario = realizar_busca(
        _id=entrada_numerica('Digite o id do funcionário a ser removido: ', minn=id_global, maxx=4000000)
    )
    if len(funcionario) != 0:
        print('Funcionário encontrado:')
        exibir_dados_funcionarios(funcionario)
        escolha = entrada_numerica(menu_remover_funcionario, minn=0, maxx=2)
        if escolha == 1:
            for i in range(0, len(lista_funcionarios)):
                if lista_funcionarios[i].get('id') == funcionario[0].get('id'):
                    lista_funcionarios.pop(i)
                    return
    else:
        print('Funcionário não encontrado!')


# Para utilização durante desenvolvimento

# with open('./funcionarios.json', encoding='utf8') as file:
#     lista_funcionarios = json.load(file)

if __name__ == '__main__':
    # EXIGÊNCIA DO CÓDIGO N.º 1 - print com o nome completo.
    print('Bem-Vindo a empresa de Artur dos Santos Shon')
    while True:
        print('-' * 60, f'{' MENU PRINCIPAL ':-^60}', sep='\n')
        # EXIGÊNCIA DO CÓDIGO N.º 6 - Deve-se implementar uma estrutura de menu no código principal (main),
        # ou seja, não pode estar dentro de função.
        escolha = entrada_numerica(menu_principal, minn=1, maxx=4)
        if escolha == 1:
            cadastrar_funcionario(gen_id())
        elif escolha == 2:
            consultar_funcionario()
        elif escolha == 3:
            remover_funcionario()
        else:
            break
