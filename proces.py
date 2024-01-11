class proces:
    def __init__(self, pid, czes_przybycia, czas_wykonania):
        self.pid= pid
        self.czas_przybycia= czes_przybycia
        self.czas_wykonania= czas_wykonania
        self.czas_ukonczenia=None
        self.czas_oczekiwania=None