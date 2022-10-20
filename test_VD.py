import unittest
from voltage_data import VoltageData
import numpy
from unittest.mock import patch
from matplotlib import pyplot as plt

#python -m unittest test_VD

t, v = numpy.loadtxt('sample_data_file.txt', unpack=True)

v_data = VoltageData(t, v)

class test_voltage_data(unittest.TestCase):

    def test_len(self):

        self.assertEqual(len(v_data), len(t), msg="len(v) != len(t)")

    def test_att(self):

        self.assertTrue((v_data.voltages == v).all())

        self.assertTrue((v_data.timestamps == t).all())

    def test_par(self):

        self.assertEqual(v_data[3,1] , v[3])

        self.assertEqual(v_data[-1,0] , t[-1])

    def test_slice(self):

        self.assertTrue((v_data[1:5,1] == v[1:5]).all())

    def test_con(self):

        v_data_2 = VoltageData.from_file('sample_data_file.txt')

        self.assertTrue((v_data_2[0]==v_data[0]).all())

    def test_iter(self):
        for i, n in enumerate(v_data):
            self.assertEqual(n[0], t[i])
            self.assertEqual(n[1],v[i])

    v_data.plot(fmt='ko', markersize=6, label='normal voltage')
    x_grid = numpy.linspace(min(t), max(t), 200)
    plt.plot(x_grid, v_data(x_grid), 'r-', label='spline')
    plt.legend()
    plt.show()

@patch('builtins.print')
def test_pri(mock_print):
        print(v_data[0])
        mock_print.assert_called_with('Row 0 -> 0.1 s, 0.24 mV')





if __name__=='__main__':
    unittest.main()
