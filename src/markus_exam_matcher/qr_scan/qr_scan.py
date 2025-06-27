from .read_qr_code import read_qr


def run(qr_file_location) -> str:
    return read_img(qr_file_location)
