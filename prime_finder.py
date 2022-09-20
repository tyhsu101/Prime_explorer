
class Prime_Explore():
    def __init__(self) -> None:
        self.known = [2,3,5,7]
        self.unknow_edge = max(self.known)+1
    def explore(self,steps:int):
        probe = self.unknow_edge
        for _ in range(steps):
            flag = 0
            probe += 1
            for test in [t for t in self.known if t < probe/2]:
                if probe%test == 0:
                    flag = 1
                    break
            if flag == 0:
                print('Explore find a new prime: {} !'.format(probe))
                self.known.append(probe)
        self.unknow_edge = probe
    def __str__(self):
        return f'On the edge of {self.unknow_edge}, we have already find: {self.known}'
def main():
    E = Prime_Explore()
    print(f'Welcome to Prime Universe. We are goint to explore new prime!')
    print(f'The known edge is {E.unknow_edge}.')
    print(f'And we already find {E.known}.')
    while True:
        t = input('How many units are you going to explore?:')
        while t.isdigit() == False:
            t = input('Please type an integer:')
        E.explore(int(t))
        print(E)

if __name__=="__main__":
    main()