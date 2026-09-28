import unittest
import pandas as pd
from qtp_genome.summary import createHTML


class TestSummary(unittest.TestCase):

    def test_createHTML(self):
        # Cria DataFrames de teste
        df_assembly = pd.DataFrame({'Stat': ['Contigs'], 'Value': [2]})
        df_contig = pd.DataFrame({'length': [12, 8]})

        # Gera o HTML
        html = createHTML(df_assembly, df_contig)

        # Valida se a estrutura básica do HTML foi produzida
        self.assertIn("<html", html.lower())
        self.assertIn("</html>", html.lower())
        self.assertIn("contigs", html.lower())


if __name__ == '__main__':
    unittest.main()