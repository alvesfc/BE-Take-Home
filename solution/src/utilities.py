# utilities.py

import logging
import re
import formulas


def setup_logger(name, level=logging.INFO):
    """
    Set up a logger for the application.

    Args:
        name (str): The name of the logger.
        level (logging.Level): The logging level.

    Returns:
        logging.Logger: Configured logger.
    """
    # Create a custom logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler('logfile.log')
    c_handler.setLevel(logging.INFO)
    f_handler.setLevel(logging.ERROR)

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger


def convert_to_float(data):
    """
    Convert data to float, handling errors and non-convertible types.

    Args:
        data (any): Data to be converted to float.

    Returns:
        float or None: Converted float value or None if conversion fails.
    """
    try:
        return float(data)
    except ValueError:
        return None


def get_referenced_cells(formula):
    cell_references = re.findall(r'\$?([A-Z]+)\$?(\d+)(:\$?([A-Z]+)\$?(\d+))?', formula)
    references = []
    for ref in cell_references:
        if ref[2]:
            start_col, start_row, _, end_col, end_row = ref
            start_row, end_row = int(start_row), int(end_row)
            for col in range(ord(start_col), ord(end_col) + 1):
                for row in range(start_row, end_row + 1):
                    references.append(f"{chr(col)}{row}")
        else:
            col, row = ref[0], ref[1]
            references.append(f"{col}{row}")
    return references


def expand_formula_ranges(range_formula):
    if ':' not in range_formula:
        return range_formula

    def expand_range(match):
        start, end = match.group(1), match.group(2)
        start_col, start_row = re.match(r'([A-Z]+)(\d+)', start).groups()
        end_col, end_row = re.match(r'([A-Z]+)(\d+)', end).groups()
        start_row, end_row = int(start_row), int(end_row)
        expanded_cells = [f"{start_col}{row}" for row in range(start_row, end_row + 1)]
        return ','.join(expanded_cells)

    range_pattern = re.compile(r'([A-Z]+\d+):([A-Z]+\d+)')
    return range_pattern.sub(expand_range, range_formula)


def parse_formula(excel_formula, context):
    parser = formulas.Parser()
    expanded_formula = expand_formula_ranges(excel_formula)
    ast_nodes = parser.ast(expanded_formula, context=context)
    for ast_node in ast_nodes:
        if hasattr(ast_node, 'compile'):
            compiled_formula = ast_node.compile(context=context)
            return compiled_formula(**context)
    return None
