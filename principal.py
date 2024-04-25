from PyQt5 import QtWidgets
from ventana import Ui_MainWindow
import sys

class VentanaJuego(QtWidgets.QMainWindow):
    def __init__(self):
        super(VentanaJuego, self).__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)

        self.preguntas = [
            'un adgetivo que termine en O (Ejemplo: caluroso)',
            'un lugar (Ejemplo: el parque)',
            'un adgetivo que termine en A (Ejemplo: hermosa)',
            'el nombre de una persona del sexo opuesto',
            'el nombre de tu mejor amigo o amiga',
            'un adgetivo que termine en O (Ejemplo: lindo)',
            'un adgetivo que termine en O (Ejemplo: feo)',
            'un lugar (Ejemplo: la cocina)',
            'lo que más te gusta hacer',
            'una frase que digas mucho',
            'lata, piedra o bola'
        ]
        self.paso = 0
        self.resultado = ''
        self.nombre = ''
        self.lugar = ''
        self.ui.label.setText(str(self.paso + 1) + '. Ingrese ' + self.preguntas[self.paso] + ':')
        self.ui.pushButton.clicked.connect(self.clicBoton)
        self.ui.actionReiniciar.triggered.connect(self.reiniciar)
        self.ui.actionCreditos.triggered.connect(self.creditos)

    def creditos(self):
        QtWidgets.QMessageBox.information(
            self,
            'Creditos',
            'Desarrollado por Lerduzz\n\nhttps://youtube.com/@lerduzz',
        )

    def salir(self):
        sys.exit(0)

    def reiniciar(self):
        self.ui.lineEdit.setEnabled(True)
        self.ui.pushButton.setEnabled(True)
        self.paso = 0
        self.resultado = ''
        self.nombre = ''
        self.lugar = ''
        self.ui.label.setText(str(self.paso + 1) + '. Ingrese ' + self.preguntas[self.paso] + ':')
        self.ui.textBrowser.setMarkdown('')
        QtWidgets.QMessageBox.information(
            self,
            'Información',
            'Juego reiniciado, vuelva a responder las preguntas.'
        )

    def resaltar(self, text):
        return '<b style="color: red;">' + str(text) + '</b>'

    def enmarcar(self, text):
        return '<b style="color: blue;">' + str(text) + '</b>'

    def parrafo(self, text):
        return '<p style="font-size: 24px">' + str(text) + '</p>'

    def clicBoton(self):
        if self.paso == 0:
            if self.ui.lineEdit.text() == '':
                self.ui.lineEdit.setText('caluroso')
            self.resultado += 'Un ' + self.enmarcar(self.ui.lineEdit.text()) + ' día de verano en '
        elif self.paso == 1:
            if self.ui.lineEdit.text() == '':
                self.ui.lineEdit.setText('el parque')
            self.resultado += self.enmarcar(self.ui.lineEdit.text()) + ' ves a la más '
        elif self.paso == 2:
            if self.ui.lineEdit.text() == '':
                self.ui.lineEdit.setText('hermosa')
            self.resultado += self.enmarcar(self.ui.lineEdit.text()) + ' criatura que hayas visto jamás, su nombre es '
        elif self.paso == 3:
            if self.ui.lineEdit.text() == '':
                self.ui.lineEdit.setText('Jane')
            self.nombre = self.enmarcar(self.ui.lineEdit.text())
            self.resultado += self.nombre + ' y cada movimiento que hace te enloquece por completo. Te acercas a tu mejor amistad '
        elif self.paso == 4:
            if self.ui.lineEdit.text() == '':
                self.ui.lineEdit.setText('John')
            self.resultado += self.enmarcar(self.ui.lineEdit.text()) + ' y le dices: - WoW! Ese es el cuerpo más '
        elif self.paso == 5:
            if self.ui.lineEdit.text() == '':
                self.ui.lineEdit.setText('lindo')
            self.resultado += self.enmarcar(self.ui.lineEdit.text()) + ' que había visto en mi vida. De repente ' + self.nombre + ' mira en dirección a ti y empieza a caminar justo hacia donde estás tú. ' + self.nombre + ' te dice: - Note que estabas justo frente a mí, tenía que decirte que pienso que eres muy '
        elif self.paso == 6:
            if self.ui.lineEdit.text() == '':
                self.ui.lineEdit.setText('feo')
            self.resultado += self.enmarcar(self.ui.lineEdit.text()) + ' y me preguntaba si te gustaría ir conmigo a '
        elif self.paso == 7:
            if self.ui.lineEdit.text() == '':
                self.ui.lineEdit.setText('la cocina')
            self.lugar = self.enmarcar(self.ui.lineEdit.text())
            self.resultado += self.lugar + ' y '
        elif self.paso == 8:
            if self.ui.lineEdit.text() == '':
                self.ui.lineEdit.setText('hacer el amor')
            self.resultado += self.enmarcar(self.ui.lineEdit.text()) + '. Con cara de idiota le dices: '
        elif self.paso == 9:
            if self.ui.lineEdit.text() == '':
                self.ui.lineEdit.setText('hay que hacerlo')
            self.resultado += self.enmarcar(self.ui.lineEdit.text()) + '; y se van juntos. Cuando finalmente llegan a ' + self.lugar + ', ' + self.nombre + ' se acerca a ti y te da el más grande y rico beso que te hayan dado. Se están besando muy apacionadamente cuando sientes que una '
        elif self.paso == 10:
            if self.ui.lineEdit.text() == '':
                self.ui.lineEdit.setText('lata')
            self.resultado += self.enmarcar(self.ui.lineEdit.text()) + ' te golpea en la cabeza. Abres tus ojos y te das cuenta de que todo fue un sueño, pero hay una pequeña nota al lado de tu cama. La nota dice: ' + self.resaltar('Continuará...')
        if self.paso < 10:
            self.paso += 1
            self.ui.label.setText(str(self.paso + 1) + '. Ingrese ' + self.preguntas[self.paso] + ':')
            self.ui.lineEdit.setText('')
        else:
            self.ui.textBrowser.setMarkdown(self.parrafo(self.resultado))
            self.ui.label.setText('Historia finalizada!')
            self.ui.lineEdit.setText('')
            self.ui.lineEdit.setEnabled(False)
            self.ui.pushButton.setEnabled(False)
            QtWidgets.QMessageBox.warning(
                self,
                'Historia finalizada',
                'Puede leer la historia generada en el recuadro que aparece en la aplicación.',
            )

app = QtWidgets.QApplication([])
application = VentanaJuego()
application.show()
sys.exit(app.exec())