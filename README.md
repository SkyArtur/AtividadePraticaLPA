# Atividade Prática de Lógica de Programação e Algoritmos

### Função Decoradora Para Inputs
Esta função realiza chamadas recursivas quando dados inválidos são inseridos pelo usuário, evitando a interrupção
do programa, a menos que o número máximo de chamadas recursivas seja atingido.
```python
from typing import Any


def decorador_input(funcao):
    def __envolucro(rotulo: str = '\n=> ', chamadas: int = 5, *args, **kwargs) -> Any:
        """
        Função de decoradora para 'inputs'.
        :param rotulo: Descrição da entrada de dados.
        :param chamadas: Número máximo de chamadas recursivas.
        :return: Valor de entrada validado.
        """
        _entrada = funcao(input(rotulo), *args, **kwargs)
        if _entrada is None:
            if chamadas > 0:
                return __envolucro(rotulo, chamadas - 1, *args, **kwargs)
            else:
                raise RuntimeError('<function: entrada> - Limite de chamadas recursivas atingido.')
        return _entrada

    return __envolucro

```

## Questão 01

Desenvolver um app para uma determinada estratégia de venda a prazo, onde juros serão determinados pelo número
de parcelas requeridas, obedecendo a seguinte orientação:

- Número de parcelas **menor** que 4, juros = 0%
- Número de parcelas **igual ou maior** a 4 e **menor** que 6, juros = 4%
- Número de parcelas **igual ou maior** a 6 e **menor** que 9, juros = 8%
- Número de parcelas **igual ou maior** a 9 e **menor** que 13, juros = 16%
- Número de parcelas **igual ou maior** a 13, juros = 32%

### Exigências:
1. Implementar exibição do nome completo do acadêmico.
2. Implementar a entrada de dados para valor do pedido e quantidade de parcelas.
3. Implementar estrutura condicional para os juros utilizando os operadores (menor que, maior que, igual ou maior que).
4. Implementar o valor da parcela e o valor total parcelado.
5. Implementar estrutura condicional *if, elif e else*.
6. Inserir comentários relevantes.
7. Implementar uma saída de console apresentando o valor da parcela e o total parcelado.

### Código:
```python
from decorador import decorador_input


@decorador_input
def input_loja(descricao: str, retorna_inteiro: bool = False) -> float | int:
    """
    EXIGÊNCIA DO CÓDIGO N.º 1 - input para entrada de dados numéricos.
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
    print('Bem-Vindo a question_01 de Artur dos Santos Shon')
    mensagem = 'O valor das parcelas é de: {}\nO valor Total Parcelado é de: {}'.format(
        *processar_pedido(
            valor_do_pedido=input_loja('Entre com o valor do pedido: '),
            quantidade_parcelas=input_loja('Entre com a quantidade de parcelas: ', True)
        )
    )
    print(mensagem)


if __name__ == '__main__':
    executar()

```

### Saída do console
<div style="width: 100%; margin: 0 auto;">
    <img src="images/questao01.png" alt="imagem da saída de console da questão número 1">
</div>

## Questão 02

Desenvolver uma aplicação para a venda de marmitas com as opções de Bife Acebolado ou Filé de Frango. 
A observar seguinte relação:

- Tamanho P de Bife Acebolado (BA) custa 16 reais e o Filé de Frango (FF) custa 15 reais;
- Tamanho M de Bife Acebolado (BA) custa 18 reais e o Filé de Frango (FF) custa 17 reais;
- Tamanho G de Bife Acebolado (BA) custa 22 reais e o Filé de Frango (FF) custa 21 reais;

### Exigências:
1. Implementar o print com o seu nome completo e um menu para o cliente. 
2. Implementar o input do sabor (BA/FF) com mensagem para escolhas incorretas.
3. Implementar o input do tamanho (P/M/G) com mensagem para escolhas incorretas.
4. Implementar *if, elif e/ou else*, utilizando o modelo aninhado (Substituído deliberadamente pela a 
utilização do operador **in** sobre uma estrutura iterável (*list*)).
5. Implementar um acumulador para somar os valores dos pedidos.
6. Implementar o input com a pergunta: “Deseja pedir mais alguma coisa?”. Se sim repetir a partir do item 2, 
senão encerrar o programa exibir o resultado do acumulador.
7. Implementar as estruturas de *while, break, continue* (todas elas).
8. Inserir comentários relevantes no código.

### Código:
```python
from decorador import decorador_input
from typing import Literal, List


@decorador_input
def input_marmitas(descricao: str, tipo: Literal['sabor', 'tamanho', 'continuar']) -> str:
    """
    EXIGÊNCIA DO CÓDIGO N.º 2, 3 e 8 - input para tamanho, sabores e continuar.
    EXIGÊNCIA DO CÓDIGO N.º 4 - estrutura 'if else' aninhada descontinuada pelo operador 'not in' aplicado
    sobre uma estrutura de dados iterável (opcoes).
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
        f'{" Bem-vindo a question_01 de Marmitas do Artur dos Santos Shon ":-^60}',
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

```

### Saída do console
<div style="width: 100%; margin: 0 auto;">
    <img src="images/questao02.png" alt="imagem da saída de console da questão número 2">
</div>