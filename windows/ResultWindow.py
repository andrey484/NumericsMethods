import wx


class ResultWindowPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent



class ResultWindow(wx.Frame):
    def __init__(self, parent, tittle):
        super(ResultWindow, self).__init__(parent=parent, tittle=tittle, size=(450, 350))
        ResultWindowPanel(self)
        self.Show()