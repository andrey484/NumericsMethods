import wx
import wx.grid as grid
import numpy as np

from utils.Utils import Utils


class MatrixWindowPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.static_text_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.matrix_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.generator_matrix_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.from_gen = wx.TextCtrl(self)
        self.from_gen.Bind(wx.EVT_CHAR, Utils.is_digit)
        self.to_gen = wx.TextCtrl(self)
        self.to_gen.Bind(wx.EVT_CHAR, Utils.is_digit)
        self.generator_matrix_sizer.Add(wx.StaticText(self, wx.ID_ANY, 'From'), 0, wx.ALL, 5)
        self.generator_matrix_sizer.Add(self.from_gen, 0, wx.ALL, 5)
        self.generator_matrix_sizer.Add(wx.StaticText(self, wx.ID_ANY, 'To'), 0, wx.ALL, 5)
        self.generator_matrix_sizer.Add(self.to_gen, 0, wx.ALL, 5)

        generate = wx.Button(self, label='Generate')
        generate.Bind(wx.EVT_BUTTON, self.generate_random_matrix)
        clear = wx.Button(self, label='Clear')
        clear.Bind(wx.EVT_BUTTON, self.clear_matrix)
        self.generator_matrix_sizer.Add(generate, 0, wx.ALL, 5)
        self.generator_matrix_sizer.Add(clear, 0, wx.ALL, 5)

        fadeev = wx.Button(self, label='Fadeev')
        fadeev.Bind(wx.EVT_BUTTON, self.fadeev)
        self.button_sizer.Add(fadeev, 0, wx.ALL, 5)

        self.static_text_sizer.Add(wx.StaticText(self, label='Matrix'), proportion=1, flag=wx.ALL | wx.EXPAND, border=5)

        self.matrix = grid.Grid(self)
        self.matrix.CreateGrid(int(Utils.matrix_order), int(Utils.matrix_order))
        self.matrix.SetColLabelSize(0)
        self.matrix.SetRowLabelSize(0)

        self.matrix_sizer.Add(self.matrix, 1, wx.EXPAND)
        self.matrix_sizer.Add(wx.StaticText(self, label='               '), proportion=1,
                              flag=wx.ALL | wx.EXPAND, border=5)

        self.main_sizer.Add(self.static_text_sizer)
        self.main_sizer.Add(self.matrix_sizer)
        self.main_sizer.Add(self.generator_matrix_sizer)
        self.main_sizer.Add(self.button_sizer)
        self.SetSizer(self.main_sizer)
        self.Layout()

    def fadeev(self, event):
        input_arr = np.zeros((Utils.matrix_order, Utils.matrix_order))
        for i in range(Utils.matrix_order):
            for j in range(Utils.matrix_order):
                input_arr[i][j] = self.matrix.GetCellValue(i, j)
        res = Utils.fadeev(input_arr)
        print(res)
        # print(np.linalg.eig(input_arr))

    def generate_random_matrix(self, event):
        from_gen = int(self.from_gen.GetValue())
        to_gen = int(self.to_gen.GetValue())
        for i in range(Utils.matrix_order):
            for j in range(Utils.matrix_order):
                self.matrix.SetCellValue(i, j, str(np.random.randint(from_gen, to_gen)))

    def clear_matrix(self, event):
        for i in range(Utils.matrix_order):
            for j in range(Utils.matrix_order):
                self.matrix.SetCellValue(i, j, '')


class MatrixWindow(wx.Frame):
    def __init__(self, parent, title):
        super(MatrixWindow, self).__init__(parent=parent, title=title, size=(450, 350))
        MatrixWindowPanel(self)
        self.Show()
