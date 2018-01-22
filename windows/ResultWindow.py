import wx
import wx.grid as grid


class ResultWindowPanel(wx.Panel):
    def __init__(self, parent, size, result_matrix):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.matrix_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.matrix = grid.Grid(self)
        self.matrix.CreateGrid(int(size), 1)
        self.matrix.SetColLabelSize(0)
        self.matrix.SetRowLabelSize(0)

        self.matrix_sizer.Add(self.matrix, 1, wx.EXPAND)

        # self.apply_btn = wx.Button(self, label='Далее')
        # self.apply_btn.Bind(wx.EVT_BUTTON, self.apply)
        # self.main_sizer.Add(self.apply_btn, 0, wx.ALL, 5)

        for j in range(int(size)):
            self.matrix.SetCellValue(j, 0, str(result_matrix[j]))

        self.main_sizer.Add(self.matrix)
        self.SetSizer(self.main_sizer)
        self.Layout()

    def apply(self, event):
        self.Close()


class ResultWindow(wx.Frame):
    def __init__(self, parent, tittle, size_of_matrix, result):
        super(ResultWindow, self).__init__(parent=parent, title=tittle, size=(150, 120))
        ResultWindowPanel(self, size_of_matrix, result)
        self.Show()
