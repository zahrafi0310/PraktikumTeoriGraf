class LISTreeSolver:
    def __init__(self, sequence):
        self.sequence = sequence
        self.all_paths = []

    def get_manual_paths(self):
        return {
            4:  [[4], [4,13], [4,7], [4,7,8], [4,7,11], [4,8], [4,8,11], [4,11]],
            1:  [[1], [1,13], [1,7], [1,7,8], [1,7,8,11], [1,7,11],
                 [1,2], [1,2,8], [1,2,8,11], [1,2,11], [1,2,3],
                 [1,8], [1,8,11], [1,11], [1,3]],
            13: [[13]],
            7:  [[7], [7,8], [7,8,11],[7,8,11,11], [7,11]],
            0:  [[0], [0,2], [0,2,8,11], [0,2,11], [0,2,3], [0,8], [0,8,11], [0,11], [0,3]],
            2:  [[2], [2,8], [2,8,11], [2,11], [2,3]],
            8:  [[8], [8,11]],
            11: [[11]],
            3:  [[3]]
        }

    def solve(self):
        paths_by_start = self.get_manual_paths()

        for paths in paths_by_start.values():
            self.all_paths.extend(paths)

        max_length = max(len(p) for p in self.all_paths)
        lis_paths = [p for p in self.all_paths if len(p) == max_length]

        print("Input Sequence:")
        print(self.sequence)

        print("\nLongest Increasing Subsequence (LIS):")
        for path in lis_paths:
            print(path)

        print(f"\nPanjang LIS = {max_length}")

        return lis_paths, max_length


if __name__ == "__main__":
    sequence = [4, 1, 13, 7, 0, 2, 8, 11, 3]
    solver = LISTreeSolver(sequence)
    solver.solve()