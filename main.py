import wx

from windows import MatrixRangWindow


def main():
    app = wx.App()
    MatrixRangWindow.MatrixRangWindow(None, 'Порядок матрицы')
    app.MainLoop()


if __name__ == '__main__':
    main()
