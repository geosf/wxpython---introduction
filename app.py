import wx

class WindowClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(WindowClass, self).__init__(*args, **kwargs)

        self.basic_gui()
    def basic_gui(self):
        self.CreateStatusBar()
        self.SetStatusText('rodando normalmente!')

        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.ID_EXIT, "Sair", "Sair da Aplicação")

        menuBar.Append(fileMenu, '&File')
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.onQuit, exitItem)

        self.SetSize((300, 200))
        self.SetTitle('Epic Window')
        
        self.Centre()
        self.Show(True)

    def onQuit(self, e):
        self.Close()

def main():
        app = wx.App()
        WindowClass(None)
        app.MainLoop()

main()