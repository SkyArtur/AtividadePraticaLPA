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
