# Kompatibilitätsschicht: QR-Codes über ReportLab (qrencoder, BSD) – API wie die Bibliothek "qrcode" (nur die genutzten Teile)
from reportlab.graphics.barcode import qrencoder as _Q
from . import constants
class QRCode:
    def __init__(self, error_correction=constants.ERROR_CORRECT_M, border=1, box_size=10, **kw):
        self.level = error_correction; self.border = border; self.data = ""
    def add_data(self, d): self.data += d
    def make(self, fit=True):
        q = _Q.QRCode(None, getattr(_Q.QRErrorCorrectLevel, self.level)); q.addData(self.data); q.make(); self.q = q
    def get_matrix(self):
        n = self.q.getModuleCount(); b = self.border
        m = [[bool(self.q.isDark(r, c)) for c in range(n)] for r in range(n)]
        pad = [[False] * (n + 2 * b) for _ in range(b)]
        return pad + [[False] * b + row + [False] * b for row in m] + [r[:] for r in pad]
