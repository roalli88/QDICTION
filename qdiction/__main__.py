from .dict_project import dict_ui

import sys
from PyQt5.QtWidgets import (
    QApplication
)


from os import path
import nltk


def main():
    curr_dir = path.dirname(__file__)
    path_to_nltk = path.join(curr_dir, 'nltk_data')
    nltk.data.path.append(path_to_nltk)
    app = QApplication(sys.argv)
    f = dict_ui()
    f.show()
    sys.setswitchinterval(0.006)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
