from .scan_qr_code import scan_qr_code


def run(img_path: str) -> str:
    return scan_qr_code.scan_qr_code(img_path)
