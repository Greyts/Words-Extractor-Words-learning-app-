from PySide2 import QtCore, QtWidgets, QtGui
import words_extractor
from datetime import datetime
import json
import random
import sys

class AppWidget(QtWidgets.QWidget):
    def __init__(self, to_translate):
        super().__init__()
        self.to_translate = to_translate
        self.layout = self.initialize_layout()
        self.setLayout(self.layout)
        self.setFont(QtGui.QFont('Sanserif',13))

    def initialize_layout(self):
        row = 0
        grid = QtWidgets.QGridLayout()

        for key, value in self.to_translate.items():
            label = QtWidgets.QLabel(key)
            translation = QtWidgets.QLabel(value)
            grid.addWidget(label, row, 0)
            grid.addWidget(translation, row, 1)
            row += 1

        return grid

if __name__ == '__main__':

    to_translate = words_extractor.main_extractor() #entire dict
    json_translate = f'{to_translate}'
    with open('translate.json', 'w', encoding='utf8') as fp:
        json.dump(json_translate, fp, ensure_ascii=False)

    #with open('translate.json', 'r', encoding='utf8') as fp:
        #translate_dict = json.load(fp)

    translate_dict = words_extractor.main_extractor()
    random_words = (random.sample(translate_dict.items(), 10))
    pairs = {}
    for pair in random_words:
        print(pair)
        pairs.update({pair[0]:pair[1]})
    app = QtWidgets.QApplication([])
    app.setApplicationDisplayName('Nauka słówek')
    appWidget = AppWidget(pairs) #to_translate - for entire dict
    appWidget.resize(800,600)
    appWidget.show()
    sys.exit(app.exec_())