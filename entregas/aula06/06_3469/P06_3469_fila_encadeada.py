"""
Módulo contendo a implementação de FilaEncadeada sobre PilhaEncadeada.
"""

from P06_3469_pilha_encadeada import PilhaEncadeada


class FilaEncadeada:
    """Implementação de uma fila FIFO usando duas pilhas LIFO por composição."""

    def __init__(self):
        """Inicializa a fila com duas pilhas.
        Complexidade: O(1)
        """
        self._pilha_entrada = PilhaEncadeada()
        self._pilha_saida = PilhaEncadeada()

    def enfileirar(self, item):
        """
        Insere o item no fim da fila.
        Complexidade: O(1)
        """
        self._pilha_entrada.push(item)

    def desenfileirar(self):
        """
        Remove e retorna o item da frente da fila; levanta IndexError se vazia.
        Complexidade: O(1) amortizada
        """
        if self.esta_vazia():
            raise IndexError("A fila está vazia.")

        if self._pilha_saida.esta_vazia():
            while not self._pilha_entrada.esta_vazia():
                self._pilha_saida.push(self._pilha_entrada.pop())

        return self._pilha_saida.pop()

    def frente(self):
        """
        Retorna o item da frente sem removê-lo; levanta IndexError se vazia.
        Complexidade: O(1) amortizada
        """
        if self.esta_vazia():
            raise IndexError("A fila está vazia.")

        if self._pilha_saida.esta_vazia():
            while not self._pilha_entrada.esta_vazia():
                self._pilha_saida.push(self._pilha_entrada.pop())

        return self._pilha_saida.topo()

    def esta_vazia(self):
        """
        Retorna True quando não há elementos armazenados.
        Complexidade: O(1)
        """
        return self._pilha_entrada.esta_vazia() and self._pilha_saida.esta_vazia()

    def __len__(self):
        """
        Retorna a quantidade total de elementos na fila.
        Complexidade: O(1)
        """
        return len(self._pilha_entrada) + len(self._pilha_saida)

    def __repr__(self, escolha="lista"):
        """
        Representação textual legível da fila (FIFO), da frente para o fim.
        Complexidade: O(N) 
        """
        if self.esta_vazia():
            raise IndexError("A fila está vazia.")

        elementos = []
        pilha_aux = PilhaEncadeada()

        while not self._pilha_saida.esta_vazia():
            item = self._pilha_saida.pop()
            elementos.append(repr(item))
            pilha_aux.push(item)

        while not pilha_aux.esta_vazia():
            self._pilha_saida.push(pilha_aux.pop())

        while not self._pilha_entrada.esta_vazia():
            pilha_aux.push(self._pilha_entrada.pop())

        while not pilha_aux.esta_vazia():
            item = pilha_aux.pop()
            elementos.append(repr(item))
            self._pilha_entrada.push(item)

        elementos.append("None")
        return " -> ".join(elementos)
