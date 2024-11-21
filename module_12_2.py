# import runner_and_tournament as rnt
# import unittest
#
# class TournamentTest(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.all_results = {}
#
#     def setUp(self):
#         vs = {'Усэйн': 10, 'Андрей': 9, 'Ник': 3}
#         self.runners = {n: rnt.Runner(name=n, speed=v) for n, v in vs.items()} #
#
#     @classmethod # обновиться все результаты после проверки?
#     def tearDownClass(cls):
#         for k, v in cls.all_results.items():
#             print(f'{k}: {v}')
#
#     def test_tournament(self):
#         tour = rnt.Tournament(90, self.runners['Усэйн'], self.runners['Ник'])
#         all_results = tour.start()
#         self.assertTrue(all_results[2], self.runners['Ник'])
#
#     def test_tournament_2(self):
#         tour = rnt.Tournament(90, self.runners['Андрей'], self.runners['Ник'])
#         all_results = tour.start() #
#         self.assertTrue(all_results[2], self.runners['Ник']) # индекс 2- это значение? А значение это что и где указано
#
#     def test_tournament_3(self):
#         tour = rnt.Tournament(90, self.runners['Усэйн'], self.runners['Андрей'], self.runners['Ник'])
#         all_results = tour.start()
#         self.assertTrue(all_results[3], self.runners['Ник'])
#
# if __name__ == '__main__':
#     unittest.main()
from runner_and_tournament import Tournament, Runner
import unittest




class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.first = Runner('Усэйн', 10)
        self.second = Runner('Андрей', 9)
        self.third = Runner('Ник', 3)
        # vs = {'Усэйн': 10, 'Андрей': 9, 'Ник': 3}
        # self.runners = {n: Runner(name=n, speed=v) for n, v in vs.items()} #



    def test_tournament(self):
        tour = Tournament(90, self.first, self.third)
        results = tour.start()
        TournamentTest.all_results.append(results)
        self.assertTrue(results[2] =='Ник')

    def test_tournament_2(self):
        tour = Tournament(90, self.second, self.third)
        results = tour.start()
        TournamentTest.all_results.append(results)
        self.assertTrue(results[2]=='Ник') # индекс 2- это значение? А значение это что и где указано

    def test_tournament_3(self):
        tour = Tournament(90, self.first, self.second, self.third)
        results = tour.start()
        TournamentTest.all_results.append(results)
        self.assertTrue(results[3]=='Ник')



    @classmethod # обновиться все результаты после проверки?
    def tearDownClass(cls):
        for k, v in enumerate(cls.all_results):
            print(f'{k+1}: {v}')


