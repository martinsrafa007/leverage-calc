# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculadoraCTGyvl.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QFrame,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 447)
        icon = QIcon()
        icon.addFile(u"img/coin-tower-with-green-arrow-uptrend-3d-illustration-financial-icon-for-stock-market-png.webp", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_EntradaStop = QPushButton(self.frame)
        self.btn_EntradaStop.setObjectName(u"btn_EntradaStop")

        self.horizontalLayout.addWidget(self.btn_EntradaStop)

        self.btn_percent = QPushButton(self.frame)
        self.btn_percent.setObjectName(u"btn_percent")

        self.horizontalLayout.addWidget(self.btn_percent)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.btn_contato = QPushButton(self.frame)
        self.btn_contato.setObjectName(u"btn_contato")

        self.horizontalLayout.addWidget(self.btn_contato)


        self.verticalLayout.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFrameShape(QFrame.Shape.StyledPanel)
        self.pg_entrada_saida = QWidget()
        self.pg_entrada_saida.setObjectName(u"pg_entrada_saida")
        self.verticalLayout_4 = QVBoxLayout(self.pg_entrada_saida)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_5 = QFrame(self.pg_entrada_saida)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.txt_max_lev = QSpinBox(self.frame_4)
        self.txt_max_lev.setObjectName(u"txt_max_lev")
        self.txt_max_lev.setMinimum(1)
        self.txt_max_lev.setMaximum(999)
        self.txt_max_lev.setValue(50)

        self.horizontalLayout_4.addWidget(self.txt_max_lev)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.txt_Entrada = QDoubleSpinBox(self.frame_4)
        self.txt_Entrada.setObjectName(u"txt_Entrada")
        self.txt_Entrada.setWrapping(False)
        self.txt_Entrada.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.txt_Entrada.setAccelerated(True)
        self.txt_Entrada.setDecimals(10)
        self.txt_Entrada.setMaximum(999999999.000000000000000)

        self.horizontalLayout_4.addWidget(self.txt_Entrada)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.txt_Stop = QDoubleSpinBox(self.frame_4)
        self.txt_Stop.setObjectName(u"txt_Stop")
        self.txt_Stop.setWrapping(False)
        self.txt_Stop.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.txt_Stop.setAccelerated(True)
        self.txt_Stop.setDecimals(10)
        self.txt_Stop.setMaximum(999999999.000000000000000)

        self.horizontalLayout_4.addWidget(self.txt_Stop)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_margem = QLabel(self.frame_6)
        self.lbl_margem.setObjectName(u"lbl_margem")

        self.horizontalLayout_5.addWidget(self.lbl_margem)

        self.lbl_leverage = QLabel(self.frame_6)
        self.lbl_leverage.setObjectName(u"lbl_leverage")

        self.horizontalLayout_5.addWidget(self.lbl_leverage)

        self.btn_calc_in_out = QPushButton(self.frame_6)
        self.btn_calc_in_out.setObjectName(u"btn_calc_in_out")

        self.horizontalLayout_5.addWidget(self.btn_calc_in_out)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.pg_entrada_saida)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.horizontalLayout_3 = QHBoxLayout(self.pg_sobre)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_3 = QFrame(self.pg_sobre)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"")
        self.label_3.setTextFormat(Qt.TextFormat.RichText)
        self.label_3.setScaledContents(False)

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setOpenExternalLinks(True)

        self.verticalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.label_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer)


        self.horizontalLayout_3.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.pg_sobre)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.verticalLayout_2 = QVBoxLayout(self.pg_contatos)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.pg_contatos)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(0, 268))

        self.verticalLayout_2.addWidget(self.label_2)

        self.frame_2 = QFrame(self.pg_contatos)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_telegram = QPushButton(self.frame_2)
        self.btn_telegram.setObjectName(u"btn_telegram")
        self.btn_telegram.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u"img/telegram.webp", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_telegram.setIcon(icon1)
        self.btn_telegram.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.btn_telegram)

        self.btn_x = QPushButton(self.frame_2)
        self.btn_x.setObjectName(u"btn_x")
        self.btn_x.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u"img/x.webp", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_x.setIcon(icon2)
        self.btn_x.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.btn_x)

        self.btn_github = QPushButton(self.frame_2)
        self.btn_github.setObjectName(u"btn_github")
        self.btn_github.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u"img/github.webp", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_github.setIcon(icon3)
        self.btn_github.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.btn_github)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.pg_contatos)
        self.pg_tamanho = QWidget()
        self.pg_tamanho.setObjectName(u"pg_tamanho")
        self.verticalLayout_7 = QVBoxLayout(self.pg_tamanho)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_7 = QFrame(self.pg_tamanho)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy2.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy2)
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_11 = QLabel(self.frame_8)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_6.addWidget(self.label_11)

        self.txt_Alavancagem = QSpinBox(self.frame_8)
        self.txt_Alavancagem.setObjectName(u"txt_Alavancagem")
        self.txt_Alavancagem.setMinimum(1)
        self.txt_Alavancagem.setMaximum(999)
        self.txt_Alavancagem.setValue(50)

        self.horizontalLayout_6.addWidget(self.txt_Alavancagem)

        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_6.addWidget(self.label_12)

        self.txt_Percentual = QDoubleSpinBox(self.frame_8)
        self.txt_Percentual.setObjectName(u"txt_Percentual")
        self.txt_Percentual.setMinimum(0.010000000000000)
        self.txt_Percentual.setMaximum(100.000000000000000)
        self.txt_Percentual.setValue(10.000000000000000)

        self.horizontalLayout_6.addWidget(self.txt_Percentual)

        self.btn_Calc_Stop = QPushButton(self.frame_8)
        self.btn_Calc_Stop.setObjectName(u"btn_Calc_Stop")

        self.horizontalLayout_6.addWidget(self.btn_Calc_Stop)


        self.verticalLayout_6.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lbl_comp_margem = QLabel(self.frame_9)
        self.lbl_comp_margem.setObjectName(u"lbl_comp_margem")

        self.horizontalLayout_7.addWidget(self.lbl_comp_margem)

        self.lbl_alavancagem = QLabel(self.frame_9)
        self.lbl_alavancagem.setObjectName(u"lbl_alavancagem")

        self.horizontalLayout_7.addWidget(self.lbl_alavancagem)

        self.horizontalSpacer_2 = QSpacerItem(220, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addWidget(self.frame_9)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.verticalLayout_7.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.pg_tamanho)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.verticalLayout.setStretch(1, 10)
        QWidget.setTabOrder(self.btn_EntradaStop, self.btn_percent)
        QWidget.setTabOrder(self.btn_percent, self.btn_sobre)
        QWidget.setTabOrder(self.btn_sobre, self.btn_contato)
        QWidget.setTabOrder(self.btn_contato, self.btn_telegram)
        QWidget.setTabOrder(self.btn_telegram, self.btn_x)
        QWidget.setTabOrder(self.btn_x, self.btn_github)
        QWidget.setTabOrder(self.btn_github, self.btn_calc_in_out)
        QWidget.setTabOrder(self.btn_calc_in_out, self.txt_max_lev)
        QWidget.setTabOrder(self.txt_max_lev, self.txt_Alavancagem)
        QWidget.setTabOrder(self.txt_Alavancagem, self.btn_Calc_Stop)

        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Leverage Calculator", None))
        self.label.setText(QCoreApplication.translate("Form", u"M\u00e9todo:", None))
        self.btn_EntradaStop.setText(QCoreApplication.translate("Form", u"Posi\u00e7\u00e3o Entrada / Stop", None))
        self.btn_percent.setText(QCoreApplication.translate("Form", u"Tamanho do Stop", None))
        self.btn_sobre.setText(QCoreApplication.translate("Form", u"Sobre", None))
        self.btn_contato.setText(QCoreApplication.translate("Form", u"Contato", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Alvancagem m\u00e1xima permitida:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Valor de entrada:", None))
        self.txt_Entrada.setPrefix(QCoreApplication.translate("Form", u"$ ", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Valor do Stop:", None))
        self.txt_Stop.setPrefix(QCoreApplication.translate("Form", u"$ ", None))
        self.lbl_margem.setText(QCoreApplication.translate("Form", u"Compensa\u00e7\u00e3o de margem:", None))
        self.lbl_leverage.setText(QCoreApplication.translate("Form", u"Alavancagem: 00x", None))
        self.btn_calc_in_out.setText(QCoreApplication.translate("Form", u"Calcular", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">O aplicativo foi desenvolvido com o intuito de calcular a alancagem m\u00e1xima e/ou <br/>compensa\u00e7\u00e3o de margem para um determinado ativo em mercados futuros.</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">T\u00e9cnica divulgada em v\u00eddeo do canal NoobSharks no youtube. Pode ser acessado </span><a href=\"https://youtu.be/0la6WfJ_ciU\"><span style=\" font-size:11pt; text-decoration: underline; color:#99ebff;\">aqui</span></a><span style=\" font-size:11pt;\"> para <br/>mais entendimentos.</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Como utilizar</span></p><p align=\"center\"><span style=\" font-size:11pt;\">Quando se conhece o valor de entrada e stop: Quando se tem esses dois valores, o aplicativo<br/>calcula e lhe devolve o valor da alavancagem.</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:11pt;\">Quando se conhece o percentual do stop: Ele calcula atrav\u00e9s do valor do percentual e lhe devolve <br/>o valor da alavancagem</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Fa\u00e7a contato comigo atrav\u00e9s das minhas redes sociais.</span></p><p align=\"center\"><br/></p><p align=\"justify\"><span style=\" font-size:12pt;\">- D\u00favidas</span></p><p align=\"justify\"><span style=\" font-size:12pt;\">- Sugest\u00f5es</span></p><p align=\"justify\"><span style=\" font-size:12pt;\">- Papo furado</span></p></body></html>", None))
        self.btn_telegram.setText(QCoreApplication.translate("Form", u"Telegram", None))
        self.btn_x.setText(QCoreApplication.translate("Form", u"X / Twitter", None))
        self.btn_github.setText(QCoreApplication.translate("Form", u"GitHub", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Alavancagem m\u00e1xima permitida:", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Percentual do Stop:", None))
        self.txt_Percentual.setSuffix(QCoreApplication.translate("Form", u" %", None))
        self.btn_Calc_Stop.setText(QCoreApplication.translate("Form", u"Calcular", None))
        self.lbl_comp_margem.setText(QCoreApplication.translate("Form", u"Compensa\u00e7\u00e3o de margem:", None))
        self.lbl_alavancagem.setText(QCoreApplication.translate("Form", u"Alavancagem: 00x", None))
    # retranslateUi

