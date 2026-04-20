
"""Modul utilitas untuk perhitungan nilai mahasiswa."""

def hitung_rata_rata(nilai_list):
    """Menghitung rata-rata dari list nilai."""
    if not nilai_list:
        return 0
    return sum(nilai_list) / len(nilai_list)

def konversi_huruf(nilai):
    """Mengkonversi nilai angka ke huruf."""
    if nilai >= 85:  return "A"
    elif nilai >= 75: return "B"
    elif nilai >= 65: return "C"
    elif nilai >= 55: return "D"
    else:             return "E"

PASSING_GRADE = 65
