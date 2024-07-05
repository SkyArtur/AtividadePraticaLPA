from decorador import decorador_input
from typing import Literal, List


@decorador_input
def input_marmitas(descricao: str, tipo: Literal['sabor', 'tamanho', 'continuar']) -> str:
    """
    EXIGÊNCIA DO CÓDIGO N.º 2, 3 e 8 - input para tamanho, sabores e continuar.
    EXIGÊNCIA DO CÓDIGO N.º 4 - estrutura 'if else' aninhada descontinuada pelo operador 'not in' aplicado
    sobre uma estrutura de dados iterável (opcoes).
    :param descricao: Descrição dos dados requeridos pelo input.
    :param tipo: Parâmetro utilizado na mensagem de erro do input.
    :param opcoes: Lista de opções a serem verificadas como válidas
    :return: Retorna uma string correspondente a opção válida
    """
    try:
        opcoes = {
            'sabor': ['ba', 'ff'],
            'tamanho': ['p', 'm', 'g'],
            'continuar': ['s', 'n'],
        }
        msg_erro = "{} inválido. Tente Novamente.\n"
        _input = descricao
        if _input not in opcoes.get(tipo):
            raise ValueError(msg_erro.format(tipo.title() if tipo not in 'continuar' else 'Opção'))
    except ValueError as erro:
        print(erro)
    else:
        return _input.lower()


def cardapio() -> dict:
    item_1 = {'nome': 'Bife Acebolado', 'tamanhos': {'p': 16, 'm': 18, 'g': 22}}
    item_2 = {'nome': 'Filé de Frango', 'tamanhos': {'p': 15, 'm': 17, 'g': 21}}
    preco_item_1 = [f'R$ {i:.2f}' for i in item_1['tamanhos'].values()]
    preco_item_2 = [f'R$ {i:.2f}' for i in item_2['tamanhos'].values()]
    print(
        f'{" Bem-vindo a loja de Marmitas do Artur dos Santos Shon ":-^60}',
        f'{"Cardápio":-^60}',
        '-' * 60,
        f'{f"|{'Tamanho':^10}|{'Bife Acebolado(BA)':^20}|{'Filé de Frango(FF)':^20}|":-^60}',
        f'{f"|{'P':^10}|{preco_item_1[0]:^20}|{preco_item_2[0]:^20}|":-^60}',
        f'{f"|{'M':^10}|{preco_item_1[1]:^20}|{preco_item_2[1]:^20}|":-^60}',
        f'{f"|{'G':^10}|{preco_item_1[2]:^20}|{preco_item_2[2]:^20}|":-^60}',
        '-' * 60,
        sep='\n'
    )
    return dict(ba=item_1, ff=item_2)


def executar() -> None:
    # EXIGÊNCIA DO CÓDIGO N.º 5 - como acumulador foi escolhida uma estrutura de dados do tipo lista.
    total, itens = list(), cardapio()
    # EXIGÊNCIA DO CÓDIGO N.º 7 - Estrutura while, continue e break.
    while True:
        sabor = input_marmitas('Entre com o sabor desejado (BA / FF): ', tipo='sabor')
        tamanho = input_marmitas('Entre com o tamanho desejado (P / M / G): ', tipo='tamanho')
        pedido = [itens[sabor]['nome'], itens[sabor]['tamanhos'][tamanho]]
        total.append(pedido[1])
        print(f'Você pediu um {pedido[0]} no tamanho {tamanho.upper()}: R$ {pedido[1]:.2f}')
        if input_marmitas('\nDeseja mais alguma coisa? (S / N): ', tipo='continuar') in 's':
            continue
        else:
            break
    # EXIGÊNCIA DO CÓDIGO N.º 6 - exibir a soma dos valores acumulados.
    print(f'\nO valor total a ser pago: R$ {sum(total):.2f}'.replace('.', ','))


if __name__ == '__main__':
    executar()
