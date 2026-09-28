# configDialog.py

from db.schema_sqlalchemy import Camera
from db.configDialog_ui import Ui_ConfigDialog
from qtpy.QtCore import Signal, Slot
from qtpy.QtWidgets import QDialog, QDialogButtonBox, QMessageBox

from db.schema_sqlalchemy import *

class ConfigDialog(QDialog):

    quitting = Signal()

    def __init__(self, bento):
        super().__init__()
        self.bento = bento
        self.ui = Ui_ConfigDialog()
        self.ui.setupUi(self)
        self.ui.usePrivateDBCheckBox.stateChanged.connect(self.usePrivateDBSettingChanged)
        self.usePrivateDBSettingChanged(True)
        self.quitting.connect(self.bento.quit)

        self.populate()

    def populate(self):
        self.ui.usernameLineEdit.setText(self.bento.config.username())
        self.ui.passwordLineEdit.setText(self.bento.config.password())
        self.ui.hostLineEdit.setText(self.bento.config.host())
        self.ui.portLineEdit.setText(self.bento.config.port())
        self.ui.usePrivateDBCheckBox.setChecked((self.bento.config.usePrivateDB()))

    @Slot()
    def accept(self):
        if not self.ui.usePrivateDBCheckBox.isChecked():
            # a shared (MySQL) database needs a host and a numeric port
            if not self.ui.hostLineEdit.text().strip() or not self.ui.portLineEdit.text().strip().isdigit():
                QMessageBox.warning(self, "Host Config",
                    "To use a shared database, enter its Host and a numeric Port.\n\n"
                    "To keep your data in a local file (bento.db in the BENTO folder), "
                    "tick \"Use private database\".")
                return
        self.bento.config.setUsePrivateDB(self.ui.usePrivateDBCheckBox.isChecked())
        self.bento.config.setUsername(self.ui.usernameLineEdit.text())
        self.bento.config.setPassword(self.ui.passwordLineEdit.text())
        self.bento.config.setHost(self.ui.hostLineEdit.text())
        self.bento.config.setPort(self.ui.portLineEdit.text())
        self.bento.config.write()
        super().accept()

    @Slot()
    def reject(self):
        super().reject()

    @Slot(int)
    def usePrivateDBSettingChanged(self, isChecked):
        self.ui.usernameLineEdit.setEnabled(not isChecked)
        self.ui.usernameLabel.setEnabled(not isChecked)
        self.ui.passwordLineEdit.setEnabled(not isChecked)
        self.ui.passwordLabel.setEnabled(not isChecked)
        self.ui.hostLineEdit.setEnabled(not isChecked)
        self.ui.hostLabel.setEnabled(not isChecked)
        self.ui.portLineEdit.setEnabled(not isChecked)
        self.ui.portLabel.setEnabled(not isChecked)
