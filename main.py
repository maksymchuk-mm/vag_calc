
# VAG ABS+ESP coding
WIN_NUMBER = "ХХХХХХХХХХХХ57667"
ABS_CODE = "113B401C09XX00XX88XX02XX90XX0041300000"

BIN = {
    13: {
        0: '22',
        1: '23',
        2: '24',
        3: '25',
        4: '26',
        5: '27',
        6: '28',
        7: '29',
        8: '2A',
        9: '2B',
    },
    14: {
        0: 'FA',
        1: 'FB',
        2: 'FC',
        3: 'FD',
        4: 'FE',
        5: 'FF',
        6: '00',
        7: '01',
        8: '02',
        9: '03',
    },
    15: {
        0: '0B',
        1: '0C',
        2: '0D',
        3: '0E',
        4: '0F',
        5: '10',
        6: '11',
        7: '12',
        8: '13',
        9: '14',
    },
    16: {
        0: 'E4',
        1: 'E5',
        2: 'E6',
        3: 'E7',
        4: 'E8',
        5: 'E9',
        6: 'EA',
        7: 'EB',
        8: 'EC',
        9: 'ED',
    },
    17: {
        0: '19',
        1: '1A',
        2: '1B',
        3: '1C',
        4: '1D',
        5: '1E',
        6: '1F',
        7: '20',
        8: '21',
        9: '22',
    }
}


def get_code():
    n = 2
    abs_code = [ABS_CODE[i:i+n] for i in range(0, len(ABS_CODE), n)]
    for i, c in zip(range(12, len(WIN_NUMBER)), [5, 7, 9, 11, 13]):
        if str((WIN_NUMBER[i])).isdigit():
            abs_code[c] = BIN[i+1][int(WIN_NUMBER[i])]
        else:
            print("Invalid number")
            return
    print(f'VIN NUMBER={WIN_NUMBER}')
    print(f'OLD CODE={ABS_CODE}')
    print(f'NEW CODE={"".join(abs_code)}')


if __name__ == '__main__':
    get_code()

