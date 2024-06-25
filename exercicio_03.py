from decorador import entrada
from typing import Literal, List


@entrada
def entrada_fabrica(descricao: str, tipo: Literal['int', 'str'], **kwargs) -> str | int:
    """
    EXIGÊNCIA DO CÓDIGO N.º 6 e 7 - implementar try/except e comentários relevantes.
    Função para entrada de dados.
    kwargs = {
        minmax = Lista de valores inteiros mínimos e máximos aceitos para inputs numéricos.
        opcao = Lista de valores do tipo string com as opções de camisas para menu.
    }
    :param descricao: Descrição dos dados solicitados.
    :param tipo: Tipo de dado retornado.
    :param kwargs: {minmax: list = [int, int], opcao: list = [str, str, ...]
    :return: Valor inteiro ou do tipo string.
    """
    try:
        _entrada = int(descricao) if tipo in 'int' else descricao
        if isinstance(_entrada, int) and kwargs.get('minmax') is not None:
            if _entrada < kwargs.get('minmax')[0] or _entrada > kwargs.get('minmax')[1]:
                _entrada = None
        else:
            if _entrada.upper() not in kwargs.get('opcao'):
                _entrada = None
        if _entrada is None:
            raise ValueError(kwargs.get('msg_erro'))
        return _entrada
    except ValueError as erro:
        print(erro)


def escolha_modelo() -> int | float:
    # EXIGÊNCIA DO CÓDIGO N.º 2 - implementar a função escolha_modelo().
    msg_erro = str('Escolha inválida, entre com o modelo novamente.\n')
    modelos = {'MCS': 1.8, 'MLS': 2.1, 'MCE': 2.9, 'MLE': 3.2}
    opcoes = [i for i in modelos.keys()]
    menu = str('Entre com o modelo desejado:\n'
               '{} - Manga Curta Simples;\n'
               '{} - Manga Longa Simples;\n'
               '{} - Manga Curta Com Estampa;\n'
               '{} - Manga Longa Com Estampa;\n>> ')
    escolha = entrada_fabrica(menu.format(*opcoes), tipo='str', msg_erro=msg_erro, opcao=opcoes)
    return modelos.get(escolha.upper())


def num_camisetas() -> dict:
    # EXIGÊNCIA DO CÓDIGO N.º 3 - implementar a função num_camisetas().
    msg_erro = 'Não aceitamos tantas camisetas de uma vez.'
    paginas = entrada_fabrica(
        'Entre com o número de camisetas: ',
        tipo='int',
        minmax=[1, 20000 - 1],
        msg_erro=msg_erro
    )
    desconto = 0
    if 20 <= paginas < 200:
        desconto = 0.05
    elif 200 <= paginas < 2000:
        desconto = 0.07
    elif 2000 <= paginas <= 20000:
        desconto = 0.12
    return {'paginas': paginas, 'desconto': desconto}


def frete() -> int:
    # EXIGÊNCIA DO CÓDIGO N.º 4 - implementar a função frete().
    msg_erro = 'Opção extra inválida.'
    valores = {1: 100, 2: 200}
    menu = str(f'Escolha o tipo de frete:\n'
               f'1 - Frete por transportadora - R$ {valores.get(1):.2f}\n'
               f'2 - Frete por Sedex - R$ {valores.get(2):.2f}\n'
               f'0 - Retirar pedido na fábrica - R$ 0,00\n>> ')
    extra = entrada_fabrica(menu, tipo='int', minmax=[0, 2], msg_erro=msg_erro)
    return valores.get(extra) if extra else extra


if __name__ == '__main__':
    # EXIGÊNCIA DO CÓDIGO N.º 5 - implementar o total a pagar no código principal (main).
    print('Bem vindos a Fábrica de Camisetas do Artur dos Santos Shon\n')
    mensagem = 'Total: R$ %.2f ((serviço: R$ %.2f - desconto: %s) *  páginas: %d + extra: R$ %.2f)'
    servico = escolha_modelo()
    qtd = num_camisetas()
    extras = frete()
    total = (servico - (servico * qtd.get('desconto'))) * qtd.get('paginas') + extras
    total = mensagem % (total, servico, f'{int(qtd.get('desconto') * 100)}%', qtd.get('paginas'), extras)
    print(total.replace('.', ','))
