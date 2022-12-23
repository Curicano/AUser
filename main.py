import subprocess
import sys
import os
from PyQt5 import QtCore, QtWidgets, QtGui
from ui.ui_main_window import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow):
    cur_user = None

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.res = self.get_resource_path("image")
        self.setupUi()
        self.connections()

    def get_resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def setupUi(self):
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(f"{self.res}\\logo.ico"))
        self.setWindowIcon(icon)
        self.add_users_in_list()

    def get_users_name(self) -> dict:
        users = subprocess.check_output(
            'wmic useraccount get name', shell=True).decode('CP866').split('\r\r\n')
        profiles1 = [i.strip(" ") for i in users if ' ' in i]
        profile1 = {}
        for i in range(profiles1.index(profiles1[-1])):
            profile1[i] = profiles1[i+1]
        return profile1

    def check_user_activity(self, user_name):
        profiles_data = subprocess.check_output(
            f"net user {user_name}", shell=True).decode("CP866").split("\n")
        active = [i.strip('Учетная запись активна \r')
                  for i in profiles_data if 'Учетная запись активна' in i]
        return active[0]

    def add_users_in_list(self):
        for user in self.get_users_name().values():
            item = QtWidgets.QListWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item.setText(user)
            icon = QtGui.QIcon()
            if self.check_user_activity(user) == "No":
                icon.addPixmap(
                    QtGui.QPixmap(f"{self.res}\\img_off.png"))
            else:
                icon.addPixmap(
                    QtGui.QPixmap(f"{self.res}\\img_on.png"))
            item.setIcon(icon)
            self.ui.lW.addItem(item)

    def user_on(self):
        try:
            if self.check_user_activity(self.cur_user) == "No":
                try:
                    subprocess.check_output(
                        f"net user {self.cur_user} /active:YES")
                except:
                    pass
            else:
                self.ui.sB.showMessage("Пользователь уже включен!", 3000)
        except:
            print("Ошибка!")
        self.user_reload()

    def user_off(self):
        try:
            if self.check_user_activity(self.cur_user) == "Yes":
                try:
                    subprocess.check_output(
                        f"net user {self.cur_user} /active:NO")
                except:
                    pass
            else:
                self.ui.sB.showMessage("Пользователь уже выключен!", 3000)
        except:
            print("Ошибка!")
        self.user_reload()

    def user_reload(self):
        try:
            for i in range(100000):
                self.ui.lW.takeItem(i-i)
        except:
            pass
        self.add_users_in_list()

    def setCurrentUser(self, name):
        self.cur_user = name

    def connections(self):
        self.ui.btn_on.clicked.connect(self.user_on)
        self.ui.btn_off.clicked.connect(self.user_off)
        self.ui.lW.currentTextChanged.connect(self.setCurrentUser)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MyWindow()
    ui.show()
    app.exec_()
