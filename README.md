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

### Código
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
