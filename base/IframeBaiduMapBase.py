# @Version：
# @Time：2024/12/15 17:54
# @Author：ChuliLin
# @Description：
class IframeBaiduMapBase:
    def search_button(self):
        """
        百度地图中的搜索按钮
        :return:
        """
        return "//button[@id='search-button']"

    def baidu_map_iframe(self):
        return "//iframe[@src='https://map.baidu.com/']"