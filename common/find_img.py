# @Version：
# @Time：2024/12/21 17:16
# @Author：ChuliLin
# @Description：

import aircv as ac
import cv2 # opencv
from common.tools import get_project_path,sep,get_now_date_time_str
from common.report_add_img import add_img_path_2_report

class FindImg:
    def img_imread(self, img_path):
        """
        读取图片
        :param img_path:
        :return:
        """
        return ac.imread(img_path)

    def get_confidence(self,source_path,search_path):
        """
        查找图片
        :param source_path:原图路径
        :param search_path: 需要查找的图片的路径
        :return:
        """
        img_src = self.img_imread(source_path)
        img_sch = self.img_imread(search_path)
        result = ac.find_template(img_src,img_sch)
        print(result)
        cv2.rectangle(
            img_src,
            result["rectangle"][0], # 左上角
            result["rectangle"][3], # 右下角
            # (255,0,0), # 蓝色
            # (0,255,0), # 绿色
            (0,0,255), # 红色
            2 # 矩形线条粗细
        )
        # 保存图片
        diff_img_path = get_project_path() +sep(["img","diff_img",
                                                 get_now_date_time_str()+"-对比的图.png"],
                                                add_sep_before=True)
        cv2.imencode(".png",img_src)[1].tofile(diff_img_path)
        add_img_path_2_report(diff_img_path,"查找到的图")
        return result["confidence"]

if __name__ == '__main__':
    source_path = get_project_path()+sep(["img","source_img","head_img.png"],add_sep_before=True)
    search_path = get_project_path()+sep(["img","assert_img","head_img.png"],add_sep_before=True)
    FindImg().get_confidence(source_path,search_path)