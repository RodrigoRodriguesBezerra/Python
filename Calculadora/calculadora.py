# Calculadora

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Altera o título da interface
        self.setWindowTitle('Calculadora do Rodrigo')
        # Fixa o tamanho da interface
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        # Cria um display para mostrar os valores e resultados
        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        # Desabilita a inserção de caracteres no display
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            # Fundo branco, cor preta e tamanho 30 pixels
            '* {background: white; color: #000; font-size: 30px;}'
        )
        # Expandir de acordo com o espaço da janela
        self.display.setSizePolicy(QSizePolicy.Preferred,
                                   QSizePolicy.Expanding)

        # Adicionar botões
        self.add_button(QPushButton('7'), 1, 0, 1, 1)
        self.add_button(QPushButton('8'), 1, 1, 1, 1)
        self.add_button(QPushButton('9'), 1, 2, 1, 1)
        self.add_button(QPushButton('+'), 1, 3, 1, 1)
        # Função de zerar o display
        self.add_button(
            QPushButton('C'), 1, 4, 1, 1,
            lambda: self.display.setText(''),
            'background: #d5580d; color: #fff; font-weight: 700'
        )

        self.add_button(QPushButton('4'), 2, 0, 1, 1)
        self.add_button(QPushButton('5'), 2, 1, 1, 1)
        self.add_button(QPushButton('6'), 2, 2, 1, 1)
        self.add_button(QPushButton('-'), 2, 3, 1, 1)
        self.add_button(
            # Função de apagar algum valor
            QPushButton('<-'), 2, 4, 1, 1,
            lambda: self.display.setText(
                self.display.text()[:-1]
            ),
            'background: orange; color: #fff; font-weight: 700'
        )

        self.add_button(QPushButton('1'), 3, 0, 1, 1)
        self.add_button(QPushButton('2'), 3, 1, 1, 1)
        self.add_button(QPushButton('3'), 3, 2, 1, 1)
        self.add_button(QPushButton('/'), 3, 3, 1, 1)
        self.add_button(QPushButton(''), 3, 4, 1, 1)

        self.add_button(QPushButton(''), 4, 0, 1, 1)
        self.add_button(QPushButton('0'), 4, 1, 1, 1)
        self.add_button(QPushButton(''), 4, 2, 1, 1)
        self.add_button(QPushButton('*'), 4, 3, 1, 1)
        self.add_button(
            QPushButton('='), 4, 4, 1, 1,
            self.eval_equal,
            'background: green; color: #fff; font-weight: 700'
        )

        self.setCentralWidget(self.cw)

    # Função para adicionar os botões do display
    def add_button(self, button, row, col, rowspan, colspan, funcao=None,
                   style=None):
        self.grid.addWidget(button, row, col, rowspan, colspan)
        # Se o botão não tem uma função específica,
        # apenas insere o valor na tela
        # se não, é aplicado a função
        if not funcao:
            button.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + button.text()
                )
            )
        else:
            button.clicked.connect(funcao)

        # Defina a cor do botão
        if style:
            button.setStyleSheet(style)

        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    # Função do botão =
    def eval_equal(self):
        # Avalia se a conta no display é correta
        # Se não, informa o erro
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception:
            self.display.setText('Conta inválida.')


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
