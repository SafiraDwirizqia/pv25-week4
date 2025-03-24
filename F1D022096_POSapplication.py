# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F1D022096_POSapplication.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 700)
        self.pos_app = QtWidgets.QWidget(MainWindow)
        self.pos_app.setObjectName("pos_app")

        # Label
        self.productLabel = QtWidgets.QLabel("Product", self.pos_app)
        self.productLabel.setGeometry(QtCore.QRect(50, 50, 100, 30))

        self.quantityLabel = QtWidgets.QLabel("Quantity", self.pos_app)
        self.quantityLabel.setGeometry(QtCore.QRect(50, 110, 100, 30))

        self.discountLabel = QtWidgets.QLabel("Discount", self.pos_app)
        self.discountLabel.setGeometry(QtCore.QRect(50, 170, 100, 30))

        # Dropdown Produk
        self.product = QtWidgets.QComboBox(self.pos_app)
        self.product.setGeometry(QtCore.QRect(160, 50, 400, 35))
        self.product.addItems(["", "Bimoli (Rp. 20,000)", "Beras 5 Kg (Rp. 75,000)", "Kecap ABC (Rp. 7,000)", "Saos Saset (Rp. 2,500)"])

        # Input Quantity
        self.quantity = QtWidgets.QLineEdit(self.pos_app)
        self.quantity.setGeometry(QtCore.QRect(160, 110, 250, 35))
        self.quantity.setValidator(QtGui.QIntValidator(1, 100))

        # Dropdown Diskon
        self.discount = QtWidgets.QComboBox(self.pos_app)
        self.discount.setGeometry(QtCore.QRect(160, 170, 100, 35))
        self.discount.addItems(["0%", "5%", "10%", "15%"])

        # Tombol
        self.addButton = QtWidgets.QPushButton("Add to Cart", self.pos_app)
        self.addButton.setGeometry(QtCore.QRect(180, 230, 160, 50))
        self.clearButton = QtWidgets.QPushButton("Clear", self.pos_app)
        self.clearButton.setGeometry(QtCore.QRect(400, 230, 160, 50))

        # List Keranjang
        self.cartList = QtWidgets.QListWidget(self.pos_app)
        self.cartList.setGeometry(QtCore.QRect(40, 300, 650, 250))

        # Label Total
        self.totalLabel = QtWidgets.QLabel("Total: Rp. 0", self.pos_app)
        self.totalLabel.setGeometry(QtCore.QRect(40, 570, 300, 40))

        # Nama & NIM
        self.nimLabel = QtWidgets.QLabel("F1D022096", self.pos_app)
        self.nimLabel.setGeometry(QtCore.QRect(590, 630, 170, 50))
        self.nimLabel.setStyleSheet("color: gray;")

        MainWindow.setCentralWidget(self.pos_app)

        # Event Handlers
        self.addButton.clicked.connect(self.add_to_cart)
        self.clearButton.clicked.connect(self.clear_cart)

        # Data Harga Produk
        self.product_prices = {
            "Bimoli (Rp. 20,000)": 20000,
            "Beras 5 Kg (Rp. 75,000)": 75000,
            "Kecap ABC (Rp. 7,000)": 7000,
            "Saos Saset (Rp. 2,500)": 2500,
        }
        self.total_price = 0
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "POS Application"))

    def add_to_cart(self):
        product = self.product.currentText()
        quantity = self.quantity.text()
        discount = self.discount.currentText()

         # Validasi input kosong
        if not product or product == "" or product not in self.product_prices:
            self.totalLabel.setText("Invalid Input")
            return

        if not quantity:
            self.totalLabel.setText("Invalid Input")
            return

        try:
            quantity = int(quantity)
            if quantity <= 0:
                self.totalLabel.setText("Invalid Input")
                return
        except ValueError:
            self.totalLabel.setText("Invalid Input")
            return

        price = self.product_prices.get(product, 0)
        discount_value = int(discount.replace("%", "")) / 100
        total_item_price = price * quantity * (1 - discount_value)
        self.total_price += total_item_price

        item_text = f"{product} - {quantity} x Rp. {price:,.0f} (disc {discount})"
        self.cartList.addItem(item_text)

        self.totalLabel.setText(f"Total: Rp. {self.total_price:,.0f}")
        self.reset_fields()

    def clear_cart(self):
        self.cartList.clear()
        self.total_price = 0
        self.totalLabel.setText("Total: Rp. 0")
        self.reset_fields()

    def reset_fields(self):
        self.product.setCurrentIndex(0)
        self.quantity.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())