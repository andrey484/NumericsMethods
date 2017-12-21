import wx

from utils.Utils import Utils
from windows.MatrixWindows import MatrixWindow


class MatrixRangPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)

        self.text_sizer = wx.BoxSizer(wx.VERTICAL)
        self.input_rang_matrix = wx.BoxSizer(wx.VERTICAL)
        self.apply_btn_sizer = wx.BoxSizer(wx.VERTICAL)

        txt = wx.StaticText(self, wx.ID_ANY, 'Введите порядок матрицы')
        self.text_sizer.Add(txt, 0, wx.ALL, 5)

        self.apply_btn = wx.Button(self, label='Далее')
        self.apply_btn.Bind(wx.EVT_BUTTON, self.apply)
        self.apply_btn_sizer.Add(self.apply_btn, 0, wx.ALL, 5)

        self.input_rang = wx.TextCtrl(self)
        self.input_rang.Bind(wx.EVT_CHAR, Utils.is_digit)
        self.input_rang_matrix.Add(self.input_rang, 0, wx.ALL, 5)

        self.main_sizer.Add(self.text_sizer, 0, wx.ALIGN_CENTRE_HORIZONTAL)
        self.main_sizer.Add(self.input_rang_matrix, 0, wx.ALIGN_CENTRE_HORIZONTAL)
        self.main_sizer.Add(self.apply_btn_sizer, 0, wx.ALIGN_CENTRE_HORIZONTAL)
        self.main_sizer.SetSizeHints(self)
        self.SetSizer(self.main_sizer)

    def apply(self, event):
        if int(self.input_rang.GetValue()) < 0:
            self.input_rang.Clear()
            wx.MessageBox('Otricatrlnaya', 'Info', wx.OK | wx.ICON_INFORMATION)
            return
        else:
            Utils.matrix_order = int(self.input_rang.GetValue())
        MatrixWindow(self, 'Методы')


class MatrixRangWindow(wx.Frame):
    def __init__(self, parent, title):
        super(MatrixRangWindow, self).__init__(parent=parent, title=title, size=(200, 200))
        MatrixRangPanel(self)
        self.Show()
