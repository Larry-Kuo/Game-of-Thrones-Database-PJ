# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UIdbIbAY.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1500, 900)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_20 = QWidget(self.centralwidget)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_52 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.widget_19 = QWidget(self.widget_20)
        self.widget_19.setObjectName(u"widget_19")
        self.verticalLayout_12 = QVBoxLayout(self.widget_19)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.groupBox = QGroupBox(self.widget_19)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 15)
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.chracter_insert_pushButton = QPushButton(self.widget)
        self.chracter_insert_pushButton.setObjectName(u"chracter_insert_pushButton")
        self.chracter_insert_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: \"Rockwell\";\n"
"background-color: rgb(60, 60, 60);\n"
"\n"
"font: bold; \n"
"border: 1px solid silver;\n"
"border-radius: 5px;\n"
"subcontrol-origin:  margin;\n"
"padding: 2 2px 2 2px;")

        self.horizontalLayout_2.addWidget(self.chracter_insert_pushButton)

        self.chracter_delete_pushButton = QPushButton(self.widget)
        self.chracter_delete_pushButton.setObjectName(u"chracter_delete_pushButton")
        self.chracter_delete_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: \"Rockwell\";\n"
"background-color: rgb(60, 60, 60);\n"
"\n"
"font: bold; \n"
"border: 1px solid silver;\n"
"border-radius: 5px;\n"
"subcontrol-origin:  margin;\n"
"padding: 2 2px 2 2px;")

        self.horizontalLayout_2.addWidget(self.chracter_delete_pushButton)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.groupBox)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.groupBox_17 = QGroupBox(self.widget_2)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_17.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_26 = QHBoxLayout(self.groupBox_17)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.chracter_name_lineEdit = QLineEdit(self.groupBox_17)
        self.chracter_name_lineEdit.setObjectName(u"chracter_name_lineEdit")
        font = QFont()
        font.setFamily(u"Rockwell")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.chracter_name_lineEdit.setFont(font)
        self.chracter_name_lineEdit.setStyleSheet(u"font: 14pt \"Rockwell\"; ")

        self.horizontalLayout_26.addWidget(self.chracter_name_lineEdit)


        self.horizontalLayout.addWidget(self.groupBox_17)

        self.horizontalSpacer_32 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_32)

        self.groupBox_11 = QGroupBox(self.widget_2)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_11.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_23 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.chracter_marriage_lineEdit = QLineEdit(self.groupBox_11)
        self.chracter_marriage_lineEdit.setObjectName(u"chracter_marriage_lineEdit")
        self.chracter_marriage_lineEdit.setStyleSheet(u"font: 14pt \"Rockwell\"; ")

        self.horizontalLayout_23.addWidget(self.chracter_marriage_lineEdit)


        self.horizontalLayout.addWidget(self.groupBox_11)

        self.horizontalSpacer_33 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_33)

        self.groupBox_16 = QGroupBox(self.widget_2)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_16.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_25 = QHBoxLayout(self.groupBox_16)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.chracter_status_lineEdit = QLineEdit(self.groupBox_16)
        self.chracter_status_lineEdit.setObjectName(u"chracter_status_lineEdit")
        self.chracter_status_lineEdit.setStyleSheet(u"font: 14pt \"Rockwell\"; ")

        self.horizontalLayout_25.addWidget(self.chracter_status_lineEdit)


        self.horizontalLayout.addWidget(self.groupBox_16)

        self.horizontalSpacer_34 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_34)

        self.groupBox_15 = QGroupBox(self.widget_2)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_15.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_24 = QHBoxLayout(self.groupBox_15)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.chracter_actor_lineEdit = QLineEdit(self.groupBox_15)
        self.chracter_actor_lineEdit.setObjectName(u"chracter_actor_lineEdit")
        self.chracter_actor_lineEdit.setStyleSheet(u"font: 14pt \"Rockwell\"; ")

        self.horizontalLayout_24.addWidget(self.chracter_actor_lineEdit)


        self.horizontalLayout.addWidget(self.groupBox_15)

        self.horizontalSpacer_35 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_35)

        self.groupBox_18 = QGroupBox(self.widget_2)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_18.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_27 = QHBoxLayout(self.groupBox_18)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.chracter_house_lineEdit = QLineEdit(self.groupBox_18)
        self.chracter_house_lineEdit.setObjectName(u"chracter_house_lineEdit")
        self.chracter_house_lineEdit.setStyleSheet(u"font: 14pt \"Rockwell\"; ")

        self.horizontalLayout_27.addWidget(self.chracter_house_lineEdit)


        self.horizontalLayout.addWidget(self.groupBox_18)


        self.verticalLayout.addWidget(self.widget_2)


        self.verticalLayout_12.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.widget_19)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 15)
        self.widget_11 = QWidget(self.groupBox_2)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_16 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_16)

        self.player_insert_pushButton = QPushButton(self.widget_11)
        self.player_insert_pushButton.setObjectName(u"player_insert_pushButton")
        self.player_insert_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: \"Rockwell\";\n"
"background-color: rgb(60, 60, 60);\n"
"\n"
"font: bold; \n"
"border: 1px solid silver;\n"
"border-radius: 5px;\n"
"subcontrol-origin:  margin;\n"
"padding: 2 2px 2 2px;")

        self.horizontalLayout_17.addWidget(self.player_insert_pushButton)

        self.player_delete_pushButton = QPushButton(self.widget_11)
        self.player_delete_pushButton.setObjectName(u"player_delete_pushButton")
        self.player_delete_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: \"Rockwell\";\n"
"background-color: rgb(60, 60, 60);\n"
"\n"
"font: bold; \n"
"border: 1px solid silver;\n"
"border-radius: 5px;\n"
"subcontrol-origin:  margin;\n"
"padding: 2 2px 2 2px;")

        self.horizontalLayout_17.addWidget(self.player_delete_pushButton)

        self.horizontalSpacer_18 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_18)


        self.verticalLayout_6.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.groupBox_2)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_18.setSpacing(3)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(3, 3, 3, 3)
        self.groupBox_36 = QGroupBox(self.widget_12)
        self.groupBox_36.setObjectName(u"groupBox_36")
        self.groupBox_36.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_36.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_48 = QHBoxLayout(self.groupBox_36)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.player_name_lineEdit = QLineEdit(self.groupBox_36)
        self.player_name_lineEdit.setObjectName(u"player_name_lineEdit")
        self.player_name_lineEdit.setStyleSheet(u"font: 14pt \"Rockwell\"; ")

        self.horizontalLayout_48.addWidget(self.player_name_lineEdit)


        self.horizontalLayout_18.addWidget(self.groupBox_36)

        self.horizontalSpacer_29 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_29)

        self.groupBox_37 = QGroupBox(self.widget_12)
        self.groupBox_37.setObjectName(u"groupBox_37")
        self.groupBox_37.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_37.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_49 = QHBoxLayout(self.groupBox_37)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.player_character_lineEdit = QLineEdit(self.groupBox_37)
        self.player_character_lineEdit.setObjectName(u"player_character_lineEdit")
        self.player_character_lineEdit.setStyleSheet(u"font: 14pt \"Rockwell\"; ")

        self.horizontalLayout_49.addWidget(self.player_character_lineEdit)


        self.horizontalLayout_18.addWidget(self.groupBox_37)

        self.horizontalSpacer_30 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_30)

        self.groupBox_38 = QGroupBox(self.widget_12)
        self.groupBox_38.setObjectName(u"groupBox_38")
        self.groupBox_38.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_38.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_50 = QHBoxLayout(self.groupBox_38)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.player_country_lineEdit = QLineEdit(self.groupBox_38)
        self.player_country_lineEdit.setObjectName(u"player_country_lineEdit")
        self.player_country_lineEdit.setStyleSheet(u"font: 14pt \"Rockwell\"; ")

        self.horizontalLayout_50.addWidget(self.player_country_lineEdit)


        self.horizontalLayout_18.addWidget(self.groupBox_38)

        self.horizontalSpacer_31 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_31)

        self.groupBox_39 = QGroupBox(self.widget_12)
        self.groupBox_39.setObjectName(u"groupBox_39")
        self.groupBox_39.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_39.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_51 = QHBoxLayout(self.groupBox_39)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.player_gender_lineEdit = QLineEdit(self.groupBox_39)
        self.player_gender_lineEdit.setObjectName(u"player_gender_lineEdit")
        self.player_gender_lineEdit.setStyleSheet(u"font: 14pt \"Rockwell\"; ")

        self.horizontalLayout_51.addWidget(self.player_gender_lineEdit)


        self.horizontalLayout_18.addWidget(self.groupBox_39)


        self.verticalLayout_6.addWidget(self.widget_12)


        self.verticalLayout_12.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.widget_19)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(3, 3, 3, 15)
        self.widget_13 = QWidget(self.groupBox_3)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_53 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalSpacer_19 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_19)

        self.war_insert_pushButton = QPushButton(self.widget_13)
        self.war_insert_pushButton.setObjectName(u"war_insert_pushButton")
        self.war_insert_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: \"Rockwell\";\n"
"background-color: rgb(60, 60, 60);\n"
"\n"
"font: bold; \n"
"border: 1px solid silver;\n"
"border-radius: 5px;\n"
"subcontrol-origin:  margin;\n"
"padding: 2 2px 2 2px;")

        self.horizontalLayout_53.addWidget(self.war_insert_pushButton)

        self.war_delete_pushButton = QPushButton(self.widget_13)
        self.war_delete_pushButton.setObjectName(u"war_delete_pushButton")
        self.war_delete_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: \"Rockwell\";\n"
"background-color: rgb(60, 60, 60);\n"
"\n"
"font: bold; \n"
"border: 1px solid silver;\n"
"border-radius: 5px;\n"
"subcontrol-origin:  margin;\n"
"padding: 2 2px 2 2px;")

        self.horizontalLayout_53.addWidget(self.war_delete_pushButton)

        self.horizontalSpacer_21 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_21)


        self.verticalLayout_7.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.groupBox_3)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_54 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_54.setSpacing(3)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(3, 3, 3, 3)
        self.groupBox_41 = QGroupBox(self.widget_14)
        self.groupBox_41.setObjectName(u"groupBox_41")
        self.groupBox_41.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_41.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_55 = QHBoxLayout(self.groupBox_41)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.war_name_lineEdit = QLineEdit(self.groupBox_41)
        self.war_name_lineEdit.setObjectName(u"war_name_lineEdit")
        self.war_name_lineEdit.setStyleSheet(u"font: 14pt \"Rockwell\"; ")

        self.horizontalLayout_55.addWidget(self.war_name_lineEdit)


        self.horizontalLayout_54.addWidget(self.groupBox_41)

        self.horizontalSpacer_26 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_26)

        self.groupBox_42 = QGroupBox(self.widget_14)
        self.groupBox_42.setObjectName(u"groupBox_42")
        self.groupBox_42.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_42.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_56 = QHBoxLayout(self.groupBox_42)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.war_participants_lineEdit_1 = QLineEdit(self.groupBox_42)
        self.war_participants_lineEdit_1.setObjectName(u"war_participants_lineEdit_1")

        self.horizontalLayout_56.addWidget(self.war_participants_lineEdit_1)

        self.war_participants_lineEdit_2 = QLineEdit(self.groupBox_42)
        self.war_participants_lineEdit_2.setObjectName(u"war_participants_lineEdit_2")

        self.horizontalLayout_56.addWidget(self.war_participants_lineEdit_2)

        self.war_participants_lineEdit_3 = QLineEdit(self.groupBox_42)
        self.war_participants_lineEdit_3.setObjectName(u"war_participants_lineEdit_3")

        self.horizontalLayout_56.addWidget(self.war_participants_lineEdit_3)

        self.war_participants_lineEdit_4 = QLineEdit(self.groupBox_42)
        self.war_participants_lineEdit_4.setObjectName(u"war_participants_lineEdit_4")

        self.horizontalLayout_56.addWidget(self.war_participants_lineEdit_4)


        self.horizontalLayout_54.addWidget(self.groupBox_42)

        self.horizontalSpacer_28 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_28)

        self.groupBox_45 = QGroupBox(self.widget_14)
        self.groupBox_45.setObjectName(u"groupBox_45")
        self.groupBox_45.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_45.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_59 = QHBoxLayout(self.groupBox_45)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.war_place_lineEdit = QLineEdit(self.groupBox_45)
        self.war_place_lineEdit.setObjectName(u"war_place_lineEdit")
        self.war_place_lineEdit.setStyleSheet(u"font: 14pt \"Rockwell\"; ")

        self.horizontalLayout_59.addWidget(self.war_place_lineEdit)


        self.horizontalLayout_54.addWidget(self.groupBox_45)


        self.verticalLayout_7.addWidget(self.widget_14)


        self.verticalLayout_12.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.widget_19)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(3, 3, 3, 15)
        self.widget_15 = QWidget(self.groupBox_4)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_60 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalSpacer_22 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_22)

        self.house_insert_pushButton = QPushButton(self.widget_15)
        self.house_insert_pushButton.setObjectName(u"house_insert_pushButton")
        self.house_insert_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: \"Rockwell\";\n"
"background-color: rgb(60, 60, 60);\n"
"\n"
"font: bold; \n"
"border: 1px solid silver;\n"
"border-radius: 5px;\n"
"subcontrol-origin:  margin;\n"
"padding: 2 2px 2 2px;")

        self.horizontalLayout_60.addWidget(self.house_insert_pushButton)

        self.house_delete_pushButton = QPushButton(self.widget_15)
        self.house_delete_pushButton.setObjectName(u"house_delete_pushButton")
        self.house_delete_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: \"Rockwell\";\n"
"background-color: rgb(60, 60, 60);\n"
"\n"
"font: bold; \n"
"border: 1px solid silver;\n"
"border-radius: 5px;\n"
"subcontrol-origin:  margin;\n"
"padding: 2 2px 2 2px;")

        self.horizontalLayout_60.addWidget(self.house_delete_pushButton)

        self.horizontalSpacer_24 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_24)


        self.verticalLayout_8.addWidget(self.widget_15)

        self.widget_16 = QWidget(self.groupBox_4)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_61 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_61.setSpacing(3)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(3, 3, 3, 3)
        self.groupBox_46 = QGroupBox(self.widget_16)
        self.groupBox_46.setObjectName(u"groupBox_46")
        self.groupBox_46.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_46.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_62 = QHBoxLayout(self.groupBox_46)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.house_name_lineEdit = QLineEdit(self.groupBox_46)
        self.house_name_lineEdit.setObjectName(u"house_name_lineEdit")
        self.house_name_lineEdit.setStyleSheet(u"font: 14pt \"Rockwell\"; ")

        self.horizontalLayout_62.addWidget(self.house_name_lineEdit)


        self.horizontalLayout_61.addWidget(self.groupBox_46)

        self.horizontalSpacer_20 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_20)

        self.groupBox_47 = QGroupBox(self.widget_16)
        self.groupBox_47.setObjectName(u"groupBox_47")
        self.groupBox_47.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_47.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_63 = QHBoxLayout(self.groupBox_47)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.house_ruler_lineEdit = QLineEdit(self.groupBox_47)
        self.house_ruler_lineEdit.setObjectName(u"house_ruler_lineEdit")
        self.house_ruler_lineEdit.setStyleSheet(u"font: 14pt \"Rockwell\"; ")

        self.horizontalLayout_63.addWidget(self.house_ruler_lineEdit)


        self.horizontalLayout_61.addWidget(self.groupBox_47)

        self.horizontalSpacer_23 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_23)

        self.groupBox_48 = QGroupBox(self.widget_16)
        self.groupBox_48.setObjectName(u"groupBox_48")
        self.groupBox_48.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_48.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_64 = QHBoxLayout(self.groupBox_48)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.house_alliance_lineEdit = QLineEdit(self.groupBox_48)
        self.house_alliance_lineEdit.setObjectName(u"house_alliance_lineEdit")
        self.house_alliance_lineEdit.setStyleSheet(u"font: 14pt \"Rockwell\"; ")

        self.horizontalLayout_64.addWidget(self.house_alliance_lineEdit)


        self.horizontalLayout_61.addWidget(self.groupBox_48)


        self.verticalLayout_8.addWidget(self.widget_16)


        self.verticalLayout_12.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.widget_19)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_5.setAlignment(Qt.AlignCenter)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(3, 3, 3, 15)
        self.widget_17 = QWidget(self.groupBox_5)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_67 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalSpacer_25 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_67.addItem(self.horizontalSpacer_25)

        self.territory_insert_pushButton = QPushButton(self.widget_17)
        self.territory_insert_pushButton.setObjectName(u"territory_insert_pushButton")
        self.territory_insert_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: \"Rockwell\";\n"
"background-color: rgb(60, 60, 60);\n"
"\n"
"font: bold; \n"
"border: 1px solid silver;\n"
"border-radius: 5px;\n"
"subcontrol-origin:  margin;\n"
"padding: 2 2px 2 2px;")

        self.horizontalLayout_67.addWidget(self.territory_insert_pushButton)

        self.territory_delete_pushButton = QPushButton(self.widget_17)
        self.territory_delete_pushButton.setObjectName(u"territory_delete_pushButton")
        self.territory_delete_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: \"Rockwell\";\n"
"background-color: rgb(60, 60, 60);\n"
"\n"
"font: bold; \n"
"border: 1px solid silver;\n"
"border-radius: 5px;\n"
"subcontrol-origin:  margin;\n"
"padding: 2 2px 2 2px;")

        self.horizontalLayout_67.addWidget(self.territory_delete_pushButton)

        self.horizontalSpacer_27 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_67.addItem(self.horizontalSpacer_27)


        self.verticalLayout_9.addWidget(self.widget_17)

        self.widget_18 = QWidget(self.groupBox_5)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_68 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_68.setSpacing(3)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(3, 3, 3, 3)
        self.groupBox_51 = QGroupBox(self.widget_18)
        self.groupBox_51.setObjectName(u"groupBox_51")
        self.groupBox_51.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_51.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_69 = QHBoxLayout(self.groupBox_51)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.territory_name_lineEdit = QLineEdit(self.groupBox_51)
        self.territory_name_lineEdit.setObjectName(u"territory_name_lineEdit")
        self.territory_name_lineEdit.setStyleSheet(u"font: 14pt \"Rockwell\"; ")

        self.horizontalLayout_69.addWidget(self.territory_name_lineEdit)


        self.horizontalLayout_68.addWidget(self.groupBox_51)

        self.horizontalSpacer_36 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_68.addItem(self.horizontalSpacer_36)

        self.groupBox_52 = QGroupBox(self.widget_18)
        self.groupBox_52.setObjectName(u"groupBox_52")
        self.groupBox_52.setStyleSheet(u" color:rgb(255, 255, 255);")
        self.groupBox_52.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_70 = QHBoxLayout(self.groupBox_52)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.territory_ruler_lineEdit = QLineEdit(self.groupBox_52)
        self.territory_ruler_lineEdit.setObjectName(u"territory_ruler_lineEdit")
        self.territory_ruler_lineEdit.setStyleSheet(u"font: 14pt \"Rockwell\"; ")

        self.horizontalLayout_70.addWidget(self.territory_ruler_lineEdit)


        self.horizontalLayout_68.addWidget(self.groupBox_52)

        self.horizontalSpacer_37 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_68.addItem(self.horizontalSpacer_37)

        self.groupBox_53 = QGroupBox(self.widget_18)
        self.groupBox_53.setObjectName(u"groupBox_53")
        self.groupBox_53.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_53.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_71 = QHBoxLayout(self.groupBox_53)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.territory_house_lineEdit = QLineEdit(self.groupBox_53)
        self.territory_house_lineEdit.setObjectName(u"territory_house_lineEdit")
        self.territory_house_lineEdit.setStyleSheet(u"font: 14pt \"Rockwell\"; \n"
"font: 14pt \"Rockwell\"; ")

        self.horizontalLayout_71.addWidget(self.territory_house_lineEdit)


        self.horizontalLayout_68.addWidget(self.groupBox_53)


        self.verticalLayout_9.addWidget(self.widget_18)


        self.verticalLayout_12.addWidget(self.groupBox_5)


        self.horizontalLayout_52.addWidget(self.widget_19)

        self.widget_3 = QWidget(self.widget_20)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_6 = QGroupBox(self.widget_3)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_6.setAlignment(Qt.AlignCenter)
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.comboBox = QComboBox(self.groupBox_6)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 60, 60);")

        self.verticalLayout_10.addWidget(self.comboBox)

        self.groupBox_7 = QGroupBox(self.groupBox_6)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_7.setAlignment(Qt.AlignCenter)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.start_sql_button = QPushButton(self.groupBox_7)
        self.start_sql_button.setObjectName(u"start_sql_button")
        self.start_sql_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: \"Rockwell\";\n"
"background-color: rgb(60, 60, 60);\n"
"\n"
"font: bold; \n"
"border: 1px solid silver;\n"
"border-radius: 5px;\n"
"subcontrol-origin:  margin;\n"
"padding: 2 2px 2 2px;")

        self.verticalLayout_11.addWidget(self.start_sql_button)

        self.groupBox_8 = QGroupBox(self.groupBox_7)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_8.setAlignment(Qt.AlignCenter)
        self.gridLayout = QGridLayout(self.groupBox_8)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.sql_command_plainTextEdit = QPlainTextEdit(self.groupBox_8)
        self.sql_command_plainTextEdit.setObjectName(u"sql_command_plainTextEdit")
        font1 = QFont()
        font1.setFamily(u"Rockwell")
        font1.setPointSize(14)
        self.sql_command_plainTextEdit.setFont(font1)

        self.gridLayout.addWidget(self.sql_command_plainTextEdit, 0, 0, 1, 1)


        self.verticalLayout_11.addWidget(self.groupBox_8)

        self.groupBox_10 = QGroupBox(self.groupBox_7)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.groupBox_10.setAlignment(Qt.AlignCenter)
        self.gridLayout_3 = QGridLayout(self.groupBox_10)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(3, 3, 3, 3)
        self.sql_output_label = QLabel(self.groupBox_10)
        self.sql_output_label.setObjectName(u"sql_output_label")
        font2 = QFont()
        font2.setFamily(u"Rockwell")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setWeight(50)
        self.sql_output_label.setFont(font2)

        self.gridLayout_3.addWidget(self.sql_output_label, 0, 0, 1, 1)


        self.verticalLayout_11.addWidget(self.groupBox_10)

        self.verticalLayout_11.setStretch(0, 1)
        self.verticalLayout_11.setStretch(1, 2)
        self.verticalLayout_11.setStretch(2, 3)

        self.verticalLayout_10.addWidget(self.groupBox_7)


        self.horizontalLayout_3.addWidget(self.groupBox_6)


        self.horizontalLayout_52.addWidget(self.widget_3)

        self.horizontalLayout_52.setStretch(0, 3)
        self.horizontalLayout_52.setStretch(1, 2)

        self.gridLayout_2.addWidget(self.widget_20, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"CHARACTER", None))
        self.chracter_insert_pushButton.setText(QCoreApplication.translate("MainWindow", u"INSERT", None))
        self.chracter_delete_pushButton.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"Name", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Marriage", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"Status", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Actor", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"House", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"PLAYER", None))
        self.player_insert_pushButton.setText(QCoreApplication.translate("MainWindow", u"INSERT", None))
        self.player_delete_pushButton.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.groupBox_36.setTitle(QCoreApplication.translate("MainWindow", u"Name", None))
        self.groupBox_37.setTitle(QCoreApplication.translate("MainWindow", u"Character", None))
        self.groupBox_38.setTitle(QCoreApplication.translate("MainWindow", u"Country", None))
        self.groupBox_39.setTitle(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"WAR", None))
        self.war_insert_pushButton.setText(QCoreApplication.translate("MainWindow", u"INSERT", None))
        self.war_delete_pushButton.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.groupBox_41.setTitle(QCoreApplication.translate("MainWindow", u"Name", None))
        self.groupBox_42.setTitle(QCoreApplication.translate("MainWindow", u"Participants", None))
        self.groupBox_45.setTitle(QCoreApplication.translate("MainWindow", u"Place", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"HOUSE", None))
        self.house_insert_pushButton.setText(QCoreApplication.translate("MainWindow", u"INSERT", None))
        self.house_delete_pushButton.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.groupBox_46.setTitle(QCoreApplication.translate("MainWindow", u"Name", None))
        self.groupBox_47.setTitle(QCoreApplication.translate("MainWindow", u"Words", None))
        self.groupBox_48.setTitle(QCoreApplication.translate("MainWindow", u"Alliance", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"TERRITORY", None))
        self.territory_insert_pushButton.setText(QCoreApplication.translate("MainWindow", u"INSERT", None))
        self.territory_delete_pushButton.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.groupBox_51.setTitle(QCoreApplication.translate("MainWindow", u"Name", None))
        self.groupBox_52.setTitle(QCoreApplication.translate("MainWindow", u"Ruler", None))
        self.groupBox_53.setTitle(QCoreApplication.translate("MainWindow", u"House", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u67e5\u8a62\u5de5\u5177", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"SQL", None))
        self.start_sql_button.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"COMMAND", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"OUTPUT", None))
        self.sql_output_label.setText("")
    # retranslateUi

