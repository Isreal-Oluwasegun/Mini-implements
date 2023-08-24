import sys
from functools import partial
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication,
                             QWidget,
                             QMainWindow,
                             QGridLayout,
                             QLineEdit,
                             QPushButton,
                             QVBoxLayout,
                             )

class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Mini Calc")
        self.setFixedSize(255, 255)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        centralWidget.setLayout(self.generalLayout)
        self._createDisplay()
        self._createButtons()

        
    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)
        
    def _createButtons(self):
        self.buttonMap ={}
        buttonLayout = QGridLayout()
        keyboard = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="]
        ]
        for row, keys in enumerate(keyboard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(40, 40)
                buttonLayout.addWidget(self.buttonMap[key], row, col)
        self.generalLayout.addLayout(buttonLayout)
    
    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()
        
    def displayText(self):
        return self.display.text()
    
    def clearDisplay(self):
        self.setDisplayText("")
        
def evaluateExpre(expression):
    try:
        result = str(eval(expression, {}, {}))
        return result
    except Exception:
        result = "Error"
    return result
        
    
class Controller:
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignalsAndSlot()
        
    def _calculateResult(self):
        result = self._evaluate(expression = self._view.displayText())
        self._view.setDisplayText(result)
        
    def _buildExpression(self, subExpression):
        if self._view.displayText == "Error":
            self._view.clearDisplay()
        expression = self._view.displayText() + "" + subExpression
        self._view.setDisplayText(expression)
        
    def _connectSignalsAndSlot(self):
        for keySymbol, button in self._view.buttonMap.items():
            if keySymbol not in {"=", "C"}:
                button.clicked.connect(
                    partial(self._buildExpression, keySymbol)
                )
        self._view.buttonMap["="].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)
    

def main():
    miniCalc = QApplication([])
    window = Window()
    window.show()
    Controller(model=evaluateExpre, view=window)
    sys.exit(miniCalc.exec())
        
if __name__ == "__main__":
    main()
