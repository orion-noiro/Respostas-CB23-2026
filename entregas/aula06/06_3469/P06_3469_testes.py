"""
Módulo de testes automatizados com unittest para PilhaEncadeada e FilaEncadeada.
"""

import unittest
from P06_3469_pilha_encadeada import PilhaEncadeada
from P06_3469_fila_encadeada import FilaEncadeada


class TestPilhaEncadeada(unittest.TestCase):
    """Testes unitários da PilhaEncadeada."""

    def setUp(self):
        self.pilha = PilhaEncadeada()

    def test_ordem_lifo(self):
        """Verifica se os elementos saem na ordem LIFO (Last In, First Out)."""
        self.pilha.push(10)
        self.pilha.push(20)
        self.pilha.push(30)
        self.assertEqual(self.pilha.pop(), 30)
        self.assertEqual(self.pilha.pop(), 20)
        self.assertEqual(self.pilha.pop(), 10)

    def test_excecoes_pilha_vazia(self):
        """Verifica se pop(), topo() e repr() levantam IndexError em pilha vazia."""
        with self.assertRaises(IndexError):
            self.pilha.pop()
        with self.assertRaises(IndexError):
            self.pilha.topo()
        with self.assertRaises(IndexError):
            repr(self.pilha)

    def test_coerencia_len(self):
        """Verifica se len() reflete o número exato de itens após inserções e remoções."""
        self.assertEqual(len(self.pilha), 0)
        self.pilha.push("a")
        self.assertEqual(len(self.pilha), 1)
        self.pilha.push("b")
        self.assertEqual(len(self.pilha), 2)
        self.pilha.pop()
        self.assertEqual(len(self.pilha), 1)
        self.pilha.pop()
        self.assertEqual(len(self.pilha), 0)

    def test_alternancia_operacoes(self):
        """Testa push e pop intercalados sucessivamente."""
        self.pilha.push(1)
        self.assertEqual(self.pilha.topo(), 1)
        self.pilha.push(2)
        self.assertEqual(self.pilha.pop(), 2)
        self.pilha.push(3)
        self.assertEqual(self.pilha.pop(), 3)
        self.assertEqual(self.pilha.pop(), 1)
        self.assertTrue(self.pilha.esta_vazia())

    def test_tipos_diferentes_repetidos_e_none(self):
        """Testa inserção de tipos variados, repetidos e None."""
        itens = [None, 42, "texto", 3.14, None, 42]
        for item in itens:
            self.pilha.push(item)

        self.assertEqual(len(self.pilha), len(itens))
        for item in reversed(itens):
            self.assertEqual(self.pilha.pop(), item)

    def test___repr__(self):
        """Testa a representação textual do topo para a base."""
        self.pilha.push(1)
        self.pilha.push(2)
        self.assertEqual(self.pilha.__repr__(), "2 -> 1 -> None")


class TestFilaEncadeada(unittest.TestCase):
    """Testes unitários da FilaEncadeada."""

    def setUp(self):
        self.fila = FilaEncadeada()

    def test_ordem_fifo(self):
        """Verifica se os elementos saem na ordem FIFO (First In, First Out)."""
        self.fila.enfileirar(1)
        self.fila.enfileirar(2)
        self.fila.enfileirar(3)
        self.assertEqual(self.fila.desenfileirar(), 1)
        self.assertEqual(self.fila.desenfileirar(), 2)
        self.assertEqual(self.fila.desenfileirar(), 3)

    def test_intercalacao_operacoes(self):
        """Testa intercalar enfileirar e desenfileirar."""
        self.fila.enfileirar("A")
        self.fila.enfileirar("B")
        self.assertEqual(self.fila.desenfileirar(), "A")
        self.fila.enfileirar("C")
        self.assertEqual(self.fila.frente(), "B")
        self.assertEqual(self.fila.desenfileirar(), "B")
        self.assertEqual(self.fila.desenfileirar(), "C")
        self.assertTrue(self.fila.esta_vazia())

    def test_esvaziar_e_reutilizar(self):
        """Testa esvaziar totalmente a fila e reutilizar a mesma instância."""
        for i in range(5):
            self.fila.enfileirar(i)
        for i in range(5):
            self.assertEqual(self.fila.desenfileirar(), i)

        self.assertTrue(self.fila.esta_vazia())

        # Reutilizando
        self.fila.enfileirar("novo1")
        self.fila.enfileirar("novo2")
        self.assertEqual(len(self.fila), 2)
        self.assertEqual(self.fila.desenfileirar(), "novo1")
        self.assertEqual(self.fila.desenfileirar(), "novo2")

    def test_excecoes_fila_vazia(self):
        """Verifica se desenfileirar(), frente(), e repr() levantam IndexError em fila vazia."""
        with self.assertRaises(IndexError):
            self.fila.desenfileirar()
        with self.assertRaises(IndexError):
            self.fila.frente()
        with self.assertRaises(IndexError):
            repr(self.fila)

    def test_coerencia_len(self):
        """Verifica se len() se mantém coerente com itens nas duas pilhas internas."""
        self.assertEqual(len(self.fila), 0)
        self.fila.enfileirar(100)
        self.fila.enfileirar(200)
        self.assertEqual(len(self.fila), 2)
        # Força transferência para pilha de saída
        _ = self.fila.frente()
        self.assertEqual(len(self.fila), 2)
        self.fila.enfileirar(300)
        self.assertEqual(len(self.fila), 3)
        self.fila.desenfileirar()
        self.assertEqual(len(self.fila), 2)

    def test___repr__(self):
        """Testa se __repr__() preserva a ordem FIFO e mantém os dados intactos."""
        self.fila.enfileirar(10)
        self.fila.enfileirar(20)
        _ = self.fila.frente()  # move para pilha de saída
        self.fila.enfileirar(30)
        # Elementos na saída: [10, 20]. Elemento na entrada: [30]
        self.assertEqual(repr(self.fila), "10 -> 20 -> 30 -> None")
        # Confirma que a fila não foi corrompida pelo repr
        self.assertEqual(self.fila.desenfileirar(), 10)
        self.assertEqual(self.fila.desenfileirar(), 20)
        self.assertEqual(self.fila.desenfileirar(), 30)


if __name__ == "__main__":
    unittest.main()
