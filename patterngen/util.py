from enum import Enum


class PaperSize(Enum):
    A6 = (105, 148.5)
    A5 = (148.5, 210)
    A4 = (210, 297)
    A3 = (297, 420)
    A2 = (420, 594)
    A1 = (594, 841)
    A0 = (841, 1189)
