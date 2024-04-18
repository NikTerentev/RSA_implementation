import re
import sys
import os

from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, \
    QFileDialog

from rsa import RSA
from ui_program import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):

        self.path_to_file = None
        self.rsa = RSA(58)
        self.is_generated_keys = False
        self.public_key = None
        self.private_key = None
        self.ext = None

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(1521, 931)
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        self.ui.radio_encode.setChecked(True)
        self.ui.radio_from_line.setChecked(True)

        self.ui.btn_performing.clicked.connect(self.prepare_to_performing)
        self.ui.btn_generate_open_keys.clicked.connect(self.generate_keys)
        self.ui.btn_open_file.clicked.connect(self.file_explorer)
        self.ui.btn_switch_texts.clicked.connect(self.switch_texts)

    def switch_texts(self):
        self.ui.original_text.setText(
            self.ui.converted_text.toPlainText())
        self.ui.converted_text.setText("")

    def file_explorer(self):
        options = QFileDialog.Options()
        self.path_to_file, _ = (QFileDialog.
                                getOpenFileName(self,
                                                "QFileDialog.getOpenFileName()",
                                                "", "All Files (*)",
                                                options=options))
        self.ui.file_path.setText(self.path_to_file)

    def performing_transformations(self, data, type_of_data):
        if not self.ui.text_open_key_n.toPlainText().strip():
            QMessageBox.critical(None, "Ошибка!",
                                 "N ещё не сгенерировано/введено!",
                                 QMessageBox.Ok)

        elif not self.ui.text_open_key_s.toPlainText().strip():
            QMessageBox.critical(None, "Ошибка!",
                                 "s ещё не сгенерировано/введено!",
                                 QMessageBox.Ok)

        elif not re.fullmatch(r"\d+",
                              self.ui.text_open_key_n.toPlainText().
                                      strip()):
            QMessageBox.critical(None, "Ошибка!",
                                 "N должно состоять "
                                 "только из цифр!",
                                 QMessageBox.Ok)

        elif not re.fullmatch(r"\d+",
                              self.ui.text_open_key_s.toPlainText().
                                      strip()):
            QMessageBox.critical(None, "Ошибка!",
                                 "s должно состоять "
                                 "только из цифр!",
                                 QMessageBox.Ok)

        else:
            if self.ui.radio_encode.isChecked():
                result = str(self.rsa.encrypt(
                    data,
                    [
                        int(self.ui.text_open_key_s.toPlainText().strip()),
                        int(self.ui.text_open_key_n.toPlainText().strip())
                    ], type_of_data))

                self.ui.converted_text.setText(result)

                if self.ui.radio_from_file.isChecked():
                    file_path, self.ext = os.path.splitext(self.path_to_file)
                    QMessageBox.information(None, "Успешно!",
                                            f"Зашифрованная информация "
                                            f"записана в файл {file_path + self.ext + '_encrypted.bin'}",
                                            QMessageBox.Ok)
                    self.path_to_file = None
                    self.ui.file_path.setText("")

            elif self.ui.radio_decode.isChecked():

                if not self.ui.text_closed_key_e.toPlainText().strip():
                    QMessageBox.critical(None, "Ошибка!",
                                         "Секретный ключ не введён!",
                                         QMessageBox.Ok)

                elif not re.fullmatch(r"\d+",
                                      self.ui.text_closed_key_e.toPlainText().
                                              strip()):
                    QMessageBox.critical(None, "Ошибка!",
                                         "Секретный ключ должен состоять "
                                         "только из цифр!",
                                         QMessageBox.Ok)
                else:

                    if self.ui.radio_from_line.isChecked() and not re.match(
                            r"^\[\d+(,\s*\d+)*\]$|^\d+$",
                            data):
                        QMessageBox.critical(None, "Ошибка!",
                                             "Текст должен состоять "
                                             "только из цифр!",
                                             QMessageBox.Ok)
                    else:
                        if self.ui.radio_from_file.isChecked():
                            type_of_data = "file"
                        else:
                            data = self.string_to_list(data)
                        is_correct = False

                        try:
                            result = self.rsa.decrypt(
                                data,
                                [
                                    int(self.ui.text_closed_key_e.toPlainText().
                                        strip()),
                                    int(self.ui.text_open_key_n.toPlainText().
                                        strip())], type_of_data)
                            is_correct = True
                        except ValueError:
                            QMessageBox.critical(None, "Ошибка!",
                                                 "Скорее всего, вы ввели"
                                                 " неверные данные!",
                                                 QMessageBox.Ok)

                        if is_correct:
                            self.ui.converted_text.setText(str(result))
                            if self.ui.radio_from_file.isChecked():
                                original_file_path = data.rpartition('_')[0]
                                base, ext = os.path.splitext(original_file_path)
                                new_file_path = base + "_decrypted" + ext
                                QMessageBox.information(None, "Успешно!",
                                                        f"Расшифрованная информация "
                                                        f"записана в файл {new_file_path}",
                                                        QMessageBox.Ok)
                                self.path_to_file = None
                                self.ui.original_text.setText("")
                                self.ui.file_path.setText("")

    def generate_keys(self):
        self.public_key, self.private_key = self.rsa.key_gen()
        self.ui.text_open_key_n.setText(str(self.public_key[1]))
        self.ui.text_open_key_s.setText(str(self.public_key[0]))
        self.ui.text_closed_key_e.setText(str(self.private_key[0]))
        self.is_generated_keys = True

    def string_to_list(self, data):
        data = data.strip("[]").split(", ")
        result = []
        for item in data:
            result.append(item)
        return result

    def prepare_to_performing(self):
        if self.ui.radio_from_line.isChecked():
            if not self.ui.original_text.toPlainText().strip():
                QMessageBox.critical(None, "Ошибка!",
                                     "Поле для текста пусто!",
                                     QMessageBox.Ok)
            else:
                original_text = (self.ui.original_text.toPlainText().
                                 strip())
                if self.ui.radio_decode.isChecked():
                    original_text = original_text.replace(",", ", ")

                self.performing_transformations(original_text, "str")

        elif self.ui.radio_from_file.isChecked():
            if not self.path_to_file:
                QMessageBox.critical(None, "Ошибка!",
                                     "Файл не выбран!",
                                     QMessageBox.Ok)
            else:
                self.performing_transformations(self.path_to_file, "file")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
