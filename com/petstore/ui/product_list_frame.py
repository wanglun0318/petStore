# coding=utf-8

"""商品列表窗口"""
import wx
import wx.grid

from com.petstore.dao.product_dao import ProductDao
from com.petstore.ui.my_frame import MyFrame


# 商品类别
CATEGORYS = ['鱼类', '狗类', '爬行类', '猫类', '鸟类']


class ProductListFrame(MyFrame):
    def __init__(self):
        super().__init__(title='商品列表', size=(1000, 700))

        # 购物车，键是选择商品的ID，值是商品的数量
        self.cart = {}
        # 选中商品
        self.selecteddata = {}

        # 创建DAO对象
        dao = ProductDao()
        # 查询所有数据
        self.data = dao.findall()
        # 创建分隔窗口
        splitter = wx.SplitterWindow(self.contentpanel, style=wx.SP_3DBORDER)
        # 创建分隔窗口中的左侧面板
        self.leftpanel = self.createleftpanel(splitter)
        # 创建分隔窗口中的右侧面板
        self.rightpanel = self.createrightpanel(splitter)

        # 设置分隔窗口左右布局
        splitter.SplitVertically(self.leftpanel, self.rightpanel, 630)

        # 设置最小窗口尺寸
        splitter.SetMinimumPaneSize(630)

        # 设置整个窗口布局是垂直Box布局
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.contentpanel.SetSizer(vbox)

        # 添加顶部对象（topbox）到vbox
        vbox.Add(self.createtopbox(), 1, flag=wx.EXPAND | wx.ALL, border=20)
        # 添加顶部对象（splitter）到vbox
        vbox.Add(splitter, 1, flag=wx.EXPAND | wx.ALL, border=10)

        # 在当前创建（Frame对象）创建并添加默认状态栏
        self.CreateStatusBar()
        self.SetStatusText('装备就绪')


