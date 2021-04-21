from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(519, 207)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditEmaul = QtWidgets.QLineEdit(Form)
        self.lineEditEmaul.setObjectName("lineEditEmaul")
        self.horizontalLayout.addWidget(self.lineEditEmaul)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEditPass = QtWidgets.QLineEdit(Form)
        self.lineEditPass.setObjectName("lineEditPass")
        self.horizontalLayout_2.addWidget(self.lineEditPass)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        
        #connected clicked signal of button with insert_data method
        self.pushButton.clicked.connect(self.insert_data)
        self.verticalLayout.addWidget(self.pushButton)
        self.labelResult = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelResult.setFont(font)
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.verticalLayout.addWidget(self.labelResult)
 
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
 
 
 
#inserting data to codeloop database in wampserver
    def insert_data(self):
        try:
            mydb = mc.connect(
 
                host="localhost",
                user="root",
                password="2605",
                database="abc"
            )
 
            mycursor = mydb.cursor()
 
            email = self.lineEditEmaul.text()
            password =self.lineEditPass.text()
 
            sql = "INSERT INTO users (email, password) VALUES (%s, %s)"
            val = (email, password)
 
            mycursor.execute(sql, val)
 
            mydb.commit()
            self.labelResult.setText("Data Inserted")
 
        except mc.Error as e:
            self.labelResult.setText("Error Inserting Data")
 
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Email"))
        self.label_2.setText(_translate("Form", "Password:"))
        self.pushButton.setText(_translate("Form", "Insert"))
 
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
