from hwp5.proc import xml


class Arguments:
    def __init__(self, hwp5file, output):
        self.embedbin = False
        self.format = None
        self.hwp5file = hwp5file
        self.logfile = 'u./test.log'  # 'sample.hwp'
        self.loglevel = 0
        self.no_validate_wellformed = False
        self.no_xml_decl = False
        self.output = output   # '/Users/seongjungkim/PycharmProjects/pyhwp/src/test.txt'


args = Arguments(hwp5file='sample.hwp', output='test.txt')
xml.main(args)
