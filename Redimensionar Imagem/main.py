import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap

# Utilizar o comando abaixo para exportar a interface feita
# no Qt Designer como código python
# - pyuic5 nomedoarquivo.ui -o nomedoarquivo.py


class RedImg(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnChoiceFile.clicked.connect(self.abrir_imagem)
        self.btnRedimensionar.clicked.connect(self.redimensionar)
        self.btnSalvar.clicked.connect(self.salvar)

    # Definir função de abrir arquivo

    def abrir_imagem(self):
        # Abre a pasta para escolher uma imagem
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir imagem',
            r'C:\Users\rodri\OneDrive\Imagens',
            # options=QFileDialog.DontUseNativeDialog
        )
        # Insere o caminho da imagem no label
        self.inputOpenFile.setText(imagem)
        # Salva a imagem original para não ser afetada pela modificação
        self.original_img = QPixmap(imagem)
        # Mostra a imagem escolhida no label
        self.labelImg.setPixmap(self.original_img)
        # Insere nas caixas de textos a altura e largura da imagem
        self.inputLargura.setText(str(self.original_img.width()))
        self.inputAltura.setText(str(self.original_img.height()))

    def redimensionar(self):
        # Guarda a largura da imagem
        largura = int(self.inputLargura.text())
        # Faz o cálculo para escalonar a altura à partir da largura
        # da imagem em um nova imagem
        self.nova_imagem = self.original_img.scaledToWidth(largura)
        # Mostra a nova imagem com as novas dimensões na tela
        self.labelImg.setPixmap(self.nova_imagem)
        # Mostra as novas larguras e altura da imagem
        self.inputLargura.setText(str(self.nova_imagem.width()))
        self.inputAltura.setText(str(self.nova_imagem.height()))

    def salvar(self):
        # Abre a pasta para salvar uma imagem
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar imagem',
            r'C:\Users\rodri\OneDrive\Área de Trabalho',
            # options=QFileDialog.DontUseNativeDialog
        )
        # Salva a imagem em formato PNG
        self.nova_imagem.save(imagem, 'PNG')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    img = RedImg()
    img.show()
    qt.exec_()
