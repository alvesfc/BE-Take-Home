import cell_model as cell_model


@staticmethod
def create_cell_model(excel_cell):
    if excel_cell.data_type == 'f' or (isinstance(excel_cell.value, str) and excel_cell.value.startswith('=')):
        return cell_model.CellModel(excel_cell.coordinate, None, excel_cell.value)
    return cell_model.CellModel(excel_cell.coordinate, excel_cell.value)
