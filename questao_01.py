from decorador import decorador_input


# EXIGÊNCIA DO CÓDIGO N.º 6 - Comentários relevantes.
# Obs.: para nomeação de variáveis foi observada as orientações da PEP 8, que recomenda a utilização do
# símbolo '_' (underscore) para a separação de palavras em código Python.

@decorador_input
def input_loja(descricao: str, retorna_inteiro: bool = False) -> float | int:
    """
    EXIGÊNCIA DO CÓDIGO N.º 1 - input para entrada de dados numéricos.
    :param descricao: Descrição da entrada de dados.
    :param retorna_inteiro: Se verdadeiro, realiza o type casting do valor retornado para inteiro.
    :return: Valor do tipo float ou do tipo inteiro.
    """
    try:
        _entrada: float = float(descricao)

    except ValueError:
        print('Entrada de dados inválida. Apenas valores numéricos são aceitos!')
    else:
        return _entrada if not retorna_inteiro else int(_entrada)


def processar_pedido(valor_do_pedido: float, quantidade_parcelas: int) -> list:
    """
    EXIGÊNCIA DO CÓDIGO N.º 2 - variáveis valor_do_pedido e quantidade_parcelas como parâmetros de função.
    EXIGÊNCIA DO CÓDIGO N.º 3 e 5 - Juros e estrutura if, elif e else.
    EXIGÊNCIA DO CÓDIGO N.º 4 - variáveis valor_da_parcela e valor_total_parcelado.
    :param valor_do_pedido: Valor do pedido.
    :param quantidade_parcelas: Quantidade de parcelas.
    :return: Lista de dados formatados.
    """
    if 4 <= quantidade_parcelas < 6:
        juros = 0.04
    elif 6 <= quantidade_parcelas < 9:
        juros = 0.08
    elif 9 <= quantidade_parcelas < 13:
        juros = 0.16
    elif quantidade_parcelas >= 13:
        juros = 0.32
    else:
        juros = 0
    valor_da_parcela = valor_do_pedido * (1 + juros) / quantidade_parcelas
    valor_total_parcelado = valor_da_parcela * quantidade_parcelas
    return [
        f'R$ {valor_da_parcela:.2f}'.replace('.', ','),
        f'R$ {valor_total_parcelado:.2f}'.replace('.', ',')
    ]


def executar() -> None:
    print('Bem-Vindo a loja de Artur dos Santos Shon')
    mensagem = 'O valor das parcelas é de: {}\nO valor Total Parcelado é de: {}'.format(
        *processar_pedido(
            valor_do_pedido=input_loja('Entre com o valor do pedido: '),
            quantidade_parcelas=input_loja('Entre com a quantidade de parcelas: ', True)
        )
    )
    print(mensagem)


if __name__ == '__main__':
    executar()
