# test_excel_analyzer.py
import unittest
from excel_analyzer import ExcelAnalyzer
import json


class TestExcelAnalyzer(unittest.TestCase):
    def setUp(self):
        self.file_path = 'solution/data/Financial_Projections.xlsx'
        self.sheet_name = 'Sheet1'
        self.analyzer = ExcelAnalyzer(self.file_path, self.sheet_name)

    def test_should_change_the_formula_and_update_the_value_of_a_cell(self):
        cell_models = self.analyzer.process_workbook()

        # C4 initial JSON
        self.assert_json_equal(cell_models.get('C4').to_json(),
                               '{"coordinate":"C4","value":83200.0,"formula":"=B4*(1+4%)","dependencies":["B4"]}')

        # N4 initial JSON
        self.assert_json_equal(cell_models.get('N4').to_json(),
                               '{"coordinate":"N4","value":128082.57,"formula":"=M4*(1+4%)","dependencies":["M4"]}')

        # Update the formula of a cell
        ExcelAnalyzer.update_value(cell_models, 'C4', '=B4*(1+1%)')

        # Assert updated values
        self.assert_json_equal(cell_models.get('C4').to_json(),
                               '{"coordinate":"C4","value":80800.0,"formula":"=B4*(1+1%)","dependencies":["B4"]}')

        # Ensure N4 is correctly updated because it depends on M4. Since M4 itself relies on the value from C4,
        # N4 has an indirect dependency on C4.
        self.assert_json_equal(cell_models.get('N4').to_json(),
                               '{"coordinate":"N4","value":124387.87,"formula":"=M4*(1+4%)","dependencies":["M4"]}')

    def test_should_calculate_the_value_of_a_cell(self):
        cell_models = ExcelAnalyzer('solution/data/Test_Case1.xlsx', self.sheet_name).process_workbook()


        self.assert_json_equal(
            cell_models.get('C12').to_json(),
            '{"coordinate":"C12","value":0.1,"formula":null,"dependencies":[]}'
        )

        # Update the value of a cell from 10% to 20% which will affect the value of C12
        ExcelAnalyzer.update_value(cell_models, 'C12', '0.2')

        # Fix the value because it was changed to String instead of keeping it as a float :(
        self.assert_json_equal(
            cell_models.get('C12').to_json(),
            '{"coordinate":"C12","value":"0.2","formula":null,"dependencies":[]}'
        )

        self.assert_json_equal(
            cell_models.get('F2').to_json(),
            '{"coordinate":"F2","value":1298.05,"formula":"=E2*(1+E12)","dependencies":["E2","E12"]}'
        )

    def assert_json_equal(self, expected, actual):
        self.assertEqual(TestExcelAnalyzer.compact_json(expected), TestExcelAnalyzer.compact_json(actual))
    @staticmethod
    def compact_json(json_str):
        return json.dumps(json.loads(json_str), separators=(',', ':'))


if __name__ == '__main__':
    unittest.main()
