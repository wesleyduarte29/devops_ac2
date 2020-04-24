from unittest import TestCase

from devops_ac2.com.wesley.operacoes import Operacoes


class TestOperacoes(TestCase):
    def setUp(self):
        self.operacoes = Operacoes()

    def test_soma(self):
        self.assertEqual(self.operacoes.soma([1, 5]), 6, "Deveria ser 6")

    def test_subtracao(self):
        self.assertEqual(self.operacoes.subtracao([5, 1]), -6, "Deveria ser 4")

    def test_multiplicacao(self):
        self.assertEqual(self.operacoes.mult([6, 3]), 36, "Deveria ser 36")
