from PyQt5 import QtCore
from PyQt5.QtWidgets import  (QSlider,  QFrame, QApplication, QMainWindow, QTableWidget, QTableWidgetItem, 
                          QHeaderView, QLabel, QSpinBox, QDoubleSpinBox, QAbstractSpinBox, QPushButton, QTextBrowser)
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
# import serial
import time
import sys

# Класс одной позиции
class Pose:
    def __init__(self, angles, gripper, delay):
        self.joints = angles
        self.gripper = gripper
        self.delay = delay

    def __str__(self):
        ret = ['Приводы:']
        for i in range(5):
            ret.append(str(self.joints[i]))
        ret.append(f'| Захват: {self.gripper}')
        ret.append(f'| Задержка: {self.delay}')
        ret = ' '.join(ret)
        return ret

    def set_joint(self, index, angle):
        self.joints[index] = angle

    def get_joint(self, index):
        return self.joints[index]

    def set_gripper(self, gripper):
        self.gripper = gripper

    def get_gripper(self):
        return self.gripper

    def set_delay(self, delay):
        self.delay = delay

    def get_delay(self):
        return self.delay


# Класс одной траектории, состоящей из нескольких позиций
class Pathway:
    def __init__(self, poses = None):
        if poses is None:
            poses = list()
        self.poses = poses

    def __str__(self):
        r = []
        for i in range(len(self.poses)):
            r.append(str(self.poses[i]))
        r = '\n'.join(r)
        return r

    def add_pose(self, newpose, index):
        if not isinstance(newpose, Pose):
            raise ValueError

        self.poses.insert(index, newpose)

    def get_pose(self, index):
        joints = self.poses[index].joints
        gripper = self.poses[index].gripper
        delay = self.poses[index].delay

        ret = [joints, gripper, delay]

        return joints, gripper, delay

    def del_pose(self, index = None):
        if index is None:
            return
        self.poses.pop(index)

    def clear(self):
        self.poses.clear()


# Класс самого приложения
class _mainApp(QMainWindow):
    # Главное окно приложения
    def __init__(self):
        super(_mainApp, self).__init__()
        # self.my_serial = serial.Serial('COM5', 115200)

        self.setWindowTitle('Prototype')
        self.setWindowIcon(QtGui.QIcon('robotic-arm.png'))
        self.setGeometry(600, 150, 480, 640) #1600x900
        # window.setGeometry(760, 240, 400, 600) #1920x1080
        self.setFixedWidth(480)
        self.setFixedHeight(640)
        

        self.mainPath = Pathway()
        self.headers = ['', '']
        self.flag = 0

        # Фреймы
        self.frame1()
        self.frame2()
        self.frame3()
    

    # ПЕРВЫЙ ФРЕЙМ С ТАБЛИЦЕЙ
    def frame1(self):
        self.frame1 = QFrame(self)
        self.frame1.setGeometry(0, 0, 480, 220)
        self.frame1.setStyleSheet('background-color: #22272E')

        # Таблица
        self.pathwayTable = QTableWidget(self.frame1)
        self.pathwayTable.setRowCount(2)
        self.pathwayTable.setColumnCount(7)
        self.pathwayTable.setGeometry(0, 0, 480, 220)
        self.pathwayTable.setStyleSheet('gridline-color: #444C56; color: #ADBAC7; font: 9pt "Open Sans"')

        # Параметры хедеров
        horHeader = self.pathwayTable.horizontalHeader()
        horHeader.setVisible(False)
        horHeader.setSectionResizeMode(QHeaderView.Stretch)

        self.pathwayTable.setVerticalHeaderLabels(self.headers)
        self.pathwayTable.verticalHeader().setStyleSheet('::section {background-color: #1C2128; font: bold; color: #E9E9EC; border: 1px solid #444C56;}')

        self.pathwayTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        
        # Объединение ячеек
        self.pathwayTable.setSpan(0, 0, 1, 5)
        self.pathwayTable.setSpan(0, 5, 2, 1)
        self.pathwayTable.setSpan(0, 6, 2, 1)

        # Названия основных заголовков
        items_labels = ['Сервоприводы', '1', '2', '3', '4', '5', 'Захват', 'Задержка']
        items_pos = [[0, 0], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [0, 5], [0, 6]]
        items = {}
        for i in range(8):
            items[i] = QTableWidgetItem(items_labels[i])
            items[i].setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            items[i].setFlags(QtCore.Qt.ItemIsEnabled)
            self.pathwayTable.setItem(items_pos[i][0], items_pos[i][1], items[i])



    # ВТОРОЙ ФРЕЙМ С ОСНОВНЫМ УПРАВЛЕНИЕМ
    def frame2(self):
        self.frame2 = QFrame(self)
        self.frame2.setGeometry(0, 220, 480, 260) # (0, 220, 480, 260)
        self.frame2.setStyleSheet('background-color: #22272E')

        # Название блока "Сервоприводы"
        self.drivesLabel = QLabel(self.frame2)
        self.drivesLabel.setText('СЕРВОПРИВОДЫ')
        self.drivesLabel.setStyleSheet('color: #ADBAC7; font: 18pt "Open Sans"')
        self.drivesLabel.move(20, 15)

        # Название блока "Захват"
        self.gripperLabel = QLabel(self.frame2)
        self.gripperLabel.setText('ЗАХВАТ')
        self.gripperLabel.setStyleSheet('color: #ADBAC7; font: 18pt "Open Sans"')
        self.gripperLabel.move(280, 15)

        # Названия, слайдеры и показатели углов для 5 сервоприводов
        self.jntLabels = {}
        self.jntSliders = {}
        self.jntAngles = {}
        for i in range(1, 6):
            self.jntLabels[i] = QLabel(self.frame2)
            self.jntLabels[i].setText(str(i))
            self.jntLabels[i].setStyleSheet('color: #ADBAC7; font: 14pt "Open Sans"')
            self.jntLabels[i].move(20, (15 + 40*i))

            self.jntSliders[i] = QSlider(Qt.Horizontal, self.frame2)
            self.jntSliders[i].setGeometry(40, 20 + 40*i, 140, 20)
            self.jntSliders[i].setRange(0, 180)
            self.jntSliders[i].setValue(90)
            self.jntSliders[i].valueChanged.connect(self.changeValue(i))

            self.jntAngles[i] = QLabel(self.frame2)
            self.jntAngles[i].setText('90')
            self.jntAngles[i].setStyleSheet('color: #ADBAC7; font: 14pt "Open Sans"')
            self.jntAngles[i].move(190, (15 + 40*i))

        # Захват
        self.gripAngle = QLabel(self.frame2)
        self.gripAngle.setText('0')
        self.gripAngle.setStyleSheet('color: #ADBAC7; font: 14pt "Open Sans"')
        self.gripAngle.move(430, 55)

        self.gripSlider = QSlider(Qt.Horizontal, self.frame2)
        self.gripSlider.setGeometry(280, 60, 140, 20)
        self.gripSlider.setRange(0, 90)
        self.gripSlider.setValue(0)
        self.gripSlider.valueChanged.connect(self.changeValue('grip'))

        # Задержка
        self.delayLable = QLabel(self.frame2)
        self.delayLable.setText('ЗАДЕРЖКА')
        self.delayLable.setStyleSheet('color: #ADBAC7; font: 14pt "Open Sans"')
        self.delayLable.move(280, 96)

        self.delaySpinbox = QDoubleSpinBox(self.frame2)
        self.delaySpinbox.setGeometry(390, 93, 58, 30)
        self.delaySpinbox.setStyleSheet('color: #ADBAC7; font: 14pt "Open Sans"; gridline-color: #ADBAC7; border: 1px solid #ADBAC7; border-radius: 4px;')
        self.delaySpinbox.setDecimals(1)
        self.delaySpinbox.setButtonSymbols(QAbstractSpinBox.NoButtons)

        # Кнопка "Создать"
        self.btnNew = QPushButton(self.frame2)
        self.btnNew.setGeometry(280, 140, 40, 40)
        self.btnNew.setStyleSheet('background-color: #22272E; border: 1px solid #ADBAC7; border-radius: 8px; color: #ADBAC7; font: 600 9pt "Open Sans"')
        self.btnNew.setText('NEW')
        self.btnNew.clicked.connect(self.newPushed)

        # Кнопка "Удалить"
        self.btnDelete = QPushButton(self.frame2)
        self.btnDelete.setGeometry(330, 140, 40, 40)
        self.btnDelete.setStyleSheet('background-color: #22272E; border: 1px solid #ADBAC7; border-radius: 8px; color: #ADBAC7; font: 600 9pt "Open Sans"')
        self.btnDelete.setText('DEL')
        self.btnDelete.clicked.connect(self.deletePushed)

        # Кнопка "Отправить"
        self.btnSend = QPushButton(self.frame2)
        self.btnSend.setGeometry(380, 140, 40, 40)
        self.btnSend.setStyleSheet('background-color: #22272E; border: 1px solid #ADBAC7; border-radius: 8px; color: #ADBAC7; font: 600 9pt "Open Sans"')
        self.btnSend.setText('SEND')


    # ТРЕТИЙ ФРЕЙМ С КОНСОЛЬЮ
    def frame3(self):
        self.frame3 = QFrame(self)
        self.frame3.setGeometry(0, 480, 480, 180)
        self.frame3.setStyleSheet('background-color:grey')

        self.dbConsole = QTextBrowser(self.frame3)
        self.dbConsole.setGeometry(0, 0, 480, 160)
        self.dbConsole.setAcceptRichText(True)
        self.dbConsole.setOpenExternalLinks(True) 
        self.dbConsole.setStyleSheet('background-color: #15181D; color: #F0A45D; font: 10pt "Consolas"')

    # Изменение значения при взаимодействии со слайдером
    def changeValue(self, n):
        if n == 'grip':
            def grip(value):
                self.gripAngle.setText(str(value))
                self.gripAngle.adjustSize()
                # self.sentPose(self.getCurrSliderPose())
            return grip

        def jnt(value):
            self.jntAngles[n].setText(str(value))
            self.jntAngles[n].adjustSize()
            # self.sentPose(self.getCurrSliderPose())
        return jnt
        
    # Свойства кнопки 'Создать'
    def newPushed(self):
        # Создание новой позиции
        curPose = Pose([self.jntSliders[1].value(), 
                        self.jntSliders[2].value(), 
                        self.jntSliders[3].value(), 
                        self.jntSliders[4].value(), 
                        self.jntSliders[5].value()], 
                        self.gripSlider.value(), 
                        self.delaySpinbox.value())
        
        numRows = self.pathwayTable.rowCount()

        # Добавление новой позиции в траекторию
        self.mainPath.add_pose(curPose, numRows + 1)

        # Создание новой строки в таблице
        self.pathwayTable.setRowCount(numRows + 1)

        self.flag = 'newTriggered'

        # Изменение имён заголовков
        self.headers.append(str(numRows - 1))
        self.pathwayTable.setVerticalHeaderLabels(self.headers)

        # Вставка значений в ячейки в виде спинбокса
        self.items = {}
        for i in range(5):
            self.items[i] = QSpinBox(parent = self.pathwayTable)
            self.items[i].setButtonSymbols(QAbstractSpinBox.NoButtons)
            self.items[i].wheelEvent = lambda event: None
            self.items[i].setMaximum(360)
            self.items[i].setValue(curPose.get_joint(i))
            self.items[i].setStyleSheet('border: 0')
            self.pathwayTable.setCellWidget(numRows , i, self.items[i])
            self.items[i].editingFinished.connect(self.onStateChanged)

        self.gripperCell = QSpinBox()
        self.gripperCell.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.gripperCell.wheelEvent = lambda event: None
        self.gripperCell.setMaximum(360)
        self.gripperCell.setValue(curPose.get_gripper())
        self.gripperCell.setStyleSheet('border: 0')
        self.pathwayTable.setCellWidget(numRows , 5, self.gripperCell)
        self.gripperCell.editingFinished.connect(self.onStateChanged)   

        self.delayCell = QDoubleSpinBox()
        self.delayCell.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.delayCell.wheelEvent = lambda event: None
        self.delayCell.setMaximum(360.0)
        self.delayCell.setDecimals(1)
        self.delayCell.setValue(curPose.get_delay())        
        self.delayCell.setStyleSheet('border: 0')
        self.pathwayTable.setCellWidget(numRows , 6, self.delayCell)
        self.delayCell.editingFinished.connect(self.onStateChanged)

        self.flag = 0

        self.dbConsole.append(f'================================================================\nТекущая траектория:\n{self.mainPath}')  

    def onStateChanged(self):
        sender = self.sender()
        value = sender.value()

        row = self.pathwayTable.indexAt(sender.pos()).row()
        column = self.pathwayTable.indexAt(sender.pos()).column()


        if value and self.flag != 'newTriggered':
            match column:
                case 5:
                    if self.mainPath.poses[row - 2].get_gripper() != value:
                        self.mainPath.poses[row - 2].set_gripper(value)
                        self.dbConsole.append(f'----------------------------------------------------------------\nТекущая траектория:\n{self.mainPath}')

                case 6:
                    if self.mainPath.poses[row - 2].get_delay() != value:
                        self.mainPath.poses[row - 2].set_delay(value)
                        self.dbConsole.append(f'----------------------------------------------------------------\nТекущая траектория:\n{self.mainPath}')

                case _:
                    if self.mainPath.poses[row - 2].get_joint(column) != value:
                        self.mainPath.poses[row - 2].set_joint(column, value)
                        self.dbConsole.append(f'----------------------------------------------------------------\nТекущая траектория:\n{self.mainPath}')
                        
            self.flag = 0
                

    # Параметры кнопки "Удалить"
    def deletePushed(self):
        numRows = self.pathwayTable.rowCount()
        if numRows > 2:
            self.pathwayTable.setRowCount(numRows - 1)
            self.mainPath.del_pose((len(self.mainPath.poses) - 1))
            self.headers.pop(len(self.headers) - 1)
            if numRows == 3:
                self.dbConsole.append('----------------------------------------------------------------')
            else:
                self.dbConsole.append(f'----------------------------------------------------------------\nТекущая траектория:\n{self.mainPath}')
            

    # # Текущая позиция слайдера
    # def getCurrSliderPose(self):
    #     curPose = Pose([self.jntSliders[1].value(), 
    #                     self.jntSliders[2].value(), 
    #                     self.jntSliders[3].value(), 
    #                     self.jntSliders[4].value(), 
    #                     self.jntSliders[5].value()], 
    #                     self.gripSlider.value(), 
    #                     self.delaySpinbox.value())
    #     return curPose

    # # Отправка траектории
    # def sendPath(self):
    #     lpose = self.mainPath.get_poses()
    #     for i in range(0, len(lpose)):
    #         self.sentPose(lpose[i])
    #         time.sleep(int(lpose[i].get_delay()))


    # def sentPose(self, pose: Pose):
    #     msg = ""
    #     gripper = pose.get_gripper()
    #     angles = pose.get_joints()
    #     for i in range(5):
    #         msg += str(angles[i]) + ';'
    #     msg += str(gripper) + "\n"
    #     self.my_serial.write(msg.encode()) 
    #     time.sleep(0.1)

# Стили для слайдера
QSS = """
QSlider::groove:horizontal {
    border-radius: 1px;       
    height: 8px;              
    margin: -1px 0;           
}
QSlider::handle:horizontal {
    background-color: #ADBAC7;
    height: 26px;     
    width: 10px;
    margin: -14px 0;     
    padding: -14px 0;  
}
QSlider::add-page:horizontal {
    background: #444C56;
}
QSlider::sub-page:horizontal {
    background: #F0A45D;
}
"""

def _main():
    application = QApplication(sys.argv)
    application.setStyleSheet(QSS)
    window = _mainApp()
    window.show()
    sys.exit(application.exec())

# Точка входа
if __name__ == '__main__':
    _main()