import unittest
import exec


class TestAll(unittest.TestCase):
    def test_space(self):
        parola = exec.Stringa()
        self.assertTrue((parola.add(" ") == 0))

    def test_sum_un_numero(self):
        parola = exec.Stringa()
        self.assertTrue((parola.add("3") == 3))

    def test_sum_due_numeri(self):
        parola = exec.Stringa()
        self.assertTrue((parola.add("3,2") == 5))

    def test_tanti_numeri(self):
        parola = exec.Stringa()
        self.assertTrue((parola.add("4,6,7,1,10,21") == 49))

    def test_con_a_capo(self):
        parola = exec.Stringa()
        self.assertTrue((parola.add("4,6,7\n1,10,21") == 49))

    def test_a_capo_alla_fine(self):
        parola = exec.Stringa()
        self.assertFalse(parola.add("4,6,7,1,10,21,\n"))
