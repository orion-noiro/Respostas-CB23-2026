"""
Módulo contendo a implementação de PilhaEncadeada.
"""

class PilhaEncadeada:
    """Implementação de pilha sobre lista encadeada."""

    class _No:
        """Classe nó auxiliar para a estrutura encadeada."""

        def __init__(self, valor, proximo=None):
            self.valor = valor
            self.proximo = proximo

    def __init__(self):
        """
        Inicializa uma pilha vazia.
        Complexidade é O(1)
        """
        self._topo = None
        self._tamanho = 0

    def push(self, item):
        """
        Insere o item no topo da pilha.
        Complexidade: O(1)
        """
        novo_no = self._No(item, proximo=self._topo)
        self._topo = novo_no
        self._tamanho += 1

    def pop(self):
        """
        Remove e retorna o item do topo; levanta IndexError se vazia.
        Complexidade: O(1)
        """
        if self.esta_vazia():
            raise IndexError("A pilha está vazia.")

        item = self._topo.valor
        self._topo = self._topo.proximo
        self._tamanho -= 1
        return item

    def topo(self):
        """
        Retorna o item do topo sem removê-lo; levanta IndexError se vazia.
        Complexidade: O(1)
        """
        if self.esta_vazia():
            raise IndexError("A pilha está vazia.")

        return self._topo.valor

    def esta_vazia(self):
        """
        Retorna True quando não há elementos armazenados.
        Complexidade: O(1)
        """
        return self._tamanho == 0

    def __len__(self):
        """
        Retorna a quantidade de elementos armazenados.
        Complexidade: O(1)
        """
        return self._tamanho

    def __repr__(self):
        """
        Representação textual legível, do topo para a base.
        Complexidade: O(N)
        """
        if self.esta_vazia():
            raise IndexError("A pilha está vazia.")

        representacao = []
        atual = self._topo
        while atual is not None:
            representacao.append(repr(atual.valor))
            atual = atual.proximo
        representacao.append("None")
        return " -> ".join(representacao)

      