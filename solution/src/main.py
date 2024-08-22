# main.py
import argparse
from utilities import setup_logger
from excel_analyzer import ExcelAnalyzer
import json


def main(file_path, sheet_name):
    # Setup logger
    logger = setup_logger('ExcelAnalysisLogger')
    logger.info(f"Analyzing File: {file_path}, Sheet: {sheet_name}")

    analyzer = ExcelAnalyzer(file_path, sheet_name)
    cell_models = analyzer.process_workbook()

    #print list of cell models
    cell_models_json = json.dumps({cell: model.to_dict() for cell, model in cell_models.items()}, indent=4)
    print(cell_models_json)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analyze Excel spreadsheet.')
    parser.add_argument('file_path', type=str, help='Path to the Excel file')
    parser.add_argument('sheet_name', type=str, help='Name of the sheet to analyze')

    args = parser.parse_args()

    main(args.file_path, args.sheet_name)
