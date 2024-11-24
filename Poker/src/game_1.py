import io
import sys

from PyQt6 import uic
from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QPixmap, QImage, QColor, QTransform
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog


ui = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>474</width>
    <height>451</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>PIL 2.0</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout_2">
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout">
      <item>
       <layout class="QVBoxLayout" name="verticalLayout">
        <item>
         <widget class="QPushButton" name="pushButton">
          <property name="text">
           <string>R</string>
          </property>
          <attribute name="buttonGroup">
           <string notr="true">channelButtons</string>
          </attribute>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="pushButton_2">
          <property name="text">
           <string>G</string>
          </property>
          <attribute name="buttonGroup">
           <string notr="true">channelButtons</string>
          </attribute>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="pushButton_3">
          <property name="text">
           <string>B</string>
          </property>
          <attribute name="buttonGroup">
           <string notr="true">channelButtons</string>
          </attribute>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="pushButton_4">
          <property name="text">
           <string>ALL</string>
          </property>
          <attribute name="buttonGroup">
           <string notr="true">channelButtons</string>
          </attribute>
         </widget>
        </item>
       </layout>
      </item>
      <item>
       <widget class="QLabel" name="image">
        <property name="minimumSize">
         <size>
          <width>250</width>
          <height>250</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>260</width>
          <height>260</height>
         </size>
        </property>
        <property name="text">
         <string>TextLabel</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout_2">
      <item>
       <widget class="QPushButton" name="pushButton_5">
        <property name="text">
         <string>Против часовой стрелки</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">rotateButtons</string>
        </attribute>
       </widget>
      </item>
      <item>
       <widget class="QPushButton" name="pushButton_6">
        <property name="text">
         <string>По часовой стрелке</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">rotateButtons</string>
        </attribute>
       </widget>
      </item>
     </layout>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>474</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
 <buttongroups>
  <buttongroup name="channelButtons"/>
  <buttongroup name="rotateButtons"/>
 </buttongroups>
</ui>"""


class MyPillow(QMainWindow):
    def __init__(self):
        super(MyPillow, self).__init__()

        f = io.StringIO(ui)
        uic.loadUi(f, self)

        self.filename = \
            QFileDialog.getOpenFileName(self,
                                        'Выберите картинку',
                                        '',
                                        'Картинки (*.jpg)')[0]
        self.degree = 0
        # python 3.8 garbage collection issue
        self.orig_image = QImage(self.filename)
        self.curr_image = self.orig_image.copy()
        self.pixmap = QPixmap.fromImage(self.curr_image)
        self.image.setPixmap(self.pixmap)
        for button in self.channelButtons.buttons():
            button.clicked.connect(self.set_channel)
        for button in self.rotateButtons.buttons():
            button.clicked.connect(self.rotate)

    def set_channel(self):
        self.curr_image = self.orig_image.copy()
        x, y = self.curr_image.size().width(), self.curr_image.size().height()

        for i in range(x):
            for j in range(y):
                r, g, b, _ = self.curr_image.pixelColor(i, j).getRgb()
                if (self.sender().text() == 'R'):
                    self.curr_image.setPixelColor(QPoint(i, j),
                                                  QColor(r, 0, 0))
                elif (self.sender().text() == 'G'):
                    self.curr_image.setPixelColor(QPoint(i, j),
                                                  QColor(0, g, 0))
                elif (self.sender().text() == 'B'):
                    self.curr_image.setPixelColor(QPoint(i, j),
                                                  QColor(0, 0, b))
                else:
                    pass

        t = QTransform().rotate(self.degree)
        self.curr_image = self.curr_image.transformed(t)
        # python 3.8 garbage collection issue
        self.pixmap = QPixmap.fromImage(self.curr_image)
        self.image.setPixmap(self.pixmap)

    def rotate(self):

        if self.sender() is self.pushButton_6:
            self.degree += 90
            degree = 90
        else:
            self.degree -= 90
            degree = -90
        self.degree %= 360

        t = QTransform().rotate(degree)
        self.curr_image = self.curr_image.transformed(t)

        self.pixmap = QPixmap.fromImage(self.curr_image)
        self.image.setPixmap(self.pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()

    sys.exit(app.exec())