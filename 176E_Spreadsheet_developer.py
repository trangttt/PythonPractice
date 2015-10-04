import unittest
import sys
import re


def get_col(col):
    _COL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ret = 0
    for i in range(len(col)):
        ret = ret*len(_COL) + _COL.index(col[i])
    return ret


def parse_element(text):
    if ':' in text:
        begin, end = text.split(':')
        res_begin = re.match('(?P<col>[A-Z]+)(?P<row>[0-9]+)', begin)
        res_end = re.match('(?P<col>[A-Z]+)(?P<row>[0-9]+)', end)
        begin_col = get_col(res_begin.group('col'))
        end_col = get_col(res_end.group('col'))
        begin_row = int(res_begin.group('row')) - 1
        end_row = int(res_end.group('row')) - 1
        return set([(c, r) for c in range(begin_col, end_col+1)
                        for r in range(begin_row, end_row+1)])
    else:
        res = re.match('(?P<col>[A-Z]+)(?P<row>[1-9]+)', text)
        col = get_col(res.group('col'))
        row = int(res.group('row')) - 1
        return set([(col, row)])


def select_cell(text):
    selected = text.split('~')
    result = set()
    for r in selected[0].split('&'):
        result = result | parse_element(r)

    if len(selected) > 1:
        for r in selected[1].split('&'):
            result = result - parse_element(r)
    return result

class TestSpreadsheetDeveloper(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(select_cell('B1'), set([(1, 0)]))
    def test_complex(self):
        result = select_cell('B1:B3&B4:E10&F1:G1&F4~C5:C8&B2')
        print(len(result))
        for i in sorted(result):
            print(i)
        answer = set([ (1,0), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9),
                      (2, 3), (2, 8), (2, 9), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
                      (3, 9), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (5, 0),
                      (5, 3), (6, 0)])
        self.assertEqual(result, answer)


if __name__ == "__main__":
        # unittest.main()
        select_cell('B1')
