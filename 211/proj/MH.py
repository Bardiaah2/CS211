class MH():
    def __init__(self, n_trails: int = 0, n_sw: int = 0, sw_w_n: int = 0, sw_w: list = [], st_w_n: int = 0, st_w: list = []) -> None:
        self.n_doors = 3
        self.n_trails = n_trails
        self.n_sw = n_sw
        self.sw_w_n = sw_w_n
        self.sw_w = sw_w
        self.st_w_n = st_w_n
        self.st_w = st_w


    def __str__(self) -> str:
        return f"""MH problem\n\tn_doors = {self.n_doors}\n\tn_trails = {self.n_trails}\n\tn_sw = {self.n_sw}\n\tsw_w_n = {self.sw_w_n}
        sw_w [{len(self.sw_w)}] = {self.sw_w}\n\tst_w_n = {self.st_w_n}\n\tst_w [{len(self.st_w)}] = {self.st_w}"""


    def trails(self, verbose=False):
        from random import randint
        chosen = randint(1, 3)
        choice = randint(1, 3)
        switch = randint(0, 1)
        reveale = randint(min(set([1, 2, 3]) - set([choice, chosen])), max(set([1, 2, 3]) - set([choice, chosen])))
        if switch:
            pass

        if verbose:
            pass


    def update(self):
        pass


    def expriment(self):
        pass


    def plot(self):
        pass


    def animate_plot(self):
        pass


if __name__ == '__main__':
    MH = MH()
    print(MH)