import sys
import webbrowser 

from PySide6 import QtWidgets

from calculadora import Ui_Form

class MainWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self) -> None:
        super(MainWindow,self).__init__()
        self.setupUi(self)

        # Navegar nos menus
        self.btn_contato.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.btn_sobre.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.btn_percent.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.btn_EntradaStop.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        
        self.btn_telegram.clicked.connect(lambda: webbrowser.open_new_tab("http://t.me/rafaelmartinsz"))
        self.btn_x.clicked.connect(lambda: webbrowser.open_new_tab("http://x.com/rafbel"))
        self.btn_github.clicked.connect(lambda: webbrowser.open_new_tab("https://github.com/martinsrafa007"))

        self.btn_calc_in_out.clicked.connect(self.calc_entrada_saida)
        self.btn_Calc_Stop.clicked.connect(self.calc_stop)


    # Calcular com Entrada + Saída
    def calc_entrada_saida(self):
        entrada = float(self.txt_Entrada.text().replace("$ ","").replace(",","."))
        saida = float(self.txt_Stop.text().replace("$ ","").replace(",","."))
        if (saida == 0) or  (entrada ==0) or (saida == entrada):
            QtWidgets.QMessageBox.warning(self,"Atenção","Os valores de entrada e saída não podem ser iguais ou nulos")
            return
        alavancagem_permitida = int(self.txt_max_lev.text())
        alavancagem = int(abs(1/ ((entrada-saida)/max(entrada,saida))))
        compensacao = float(abs((1- (alavancagem/alavancagem_permitida))))
        self.lbl_leverage.setText(f"Alavancagem: {alavancagem}x")
        if alavancagem_permitida >= alavancagem:
            self.lbl_margem.setText(f"Compensação de margem: --")
        else:
            self.lbl_margem.setText(f"Compensação de margem: {compensacao:.2%}")
    
    #Calcular conhecendo o % do Stop
    def calc_stop(self):
        stop = float(self.txt_Percentual.text().replace(" %","").replace(",","."))
        alavancagem_max = int(self.txt_Alavancagem.text())
        alavancagem = int(100 / stop)
        if alavancagem_max < alavancagem:
            compensacao = float(abs((1- (alavancagem/alavancagem_max))))
            self.lbl_comp_margem.setText(f"Compensação de margem: {compensacao:.2%}")
        else:
            self.lbl_comp_margem.setText(f"Compensação de margem: --")
        self.lbl_alavancagem.setText(f"Alavancagem : {alavancagem}x")



    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()