'''

현재 imgaug-doc-master의 bbox_jw를 통해 bounding box를 읽어오는 것까지!!
폴더안에 choco songi  (인식시킬 object class name list로 변경)
jpg이면 selected_jpg_list에 붙이고
아니면 selected_extension_list에 붙이고

'''

import imageio
import imgaug as ia
import pdb
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
import os
import cv2
from PIL import Image
ia.seed(1)

#가져올 파일들이 있는 directory path
'''
절대경로로 적어준다. 이때 \\로 구분시켜서 넣어주면 됨.
'''
path_dir = 'D:\\Yolo_mark-master\\x64\\Release\\data\\img'


file_list = os.listdir(path_dir)
#selected_file_list_length = len(file_list)/2
#선택받은 file list들을 selected_file_list
selected_jpg_list = []
selected_extension_list = []
#문자열순으로 list정렬되어서 1, 10, 11...19, 2, 20, 3, 4....
file_list.sort()
for i in file_list:
    if('choco_songi' in i):
        if('jpg' in i ):
            selected_jpg_list.append(i)
        else:
            selected_extension_list.append(i)
#path에 존재하는 파일 목록가져오기 - choco_songi에해당할
bbox = []
lines = []
bbox_saved = []
bbox_image = []
for i in range(0, len(selected_jpg_list)):
    count = 0
    image = imageio.imread(path_dir + '\\'+selected_jpg_list[i])
    image_cv = cv2.imread(path_dir + '\\'+selected_jpg_list[i])
    image_PIL = Image.open(path_dir + '\\'+selected_jpg_list[i])
    height, width, channels = image_cv.shape
    f = open(path_dir + '\\' + selected_extension_list[i])
    lines = f.readlines()
    #이미지하나다마 txt에서 추출한 bbox좌표들을 담아놓은 list를 가진다.

    for line in lines:
        #center point x,y 와 width, height 순으로
        bbox_saved.append(line.strip().split())
        count += 1
    for bbox_index in range(0,count):
        bbox_center_x = float(bbox_saved[bbox_index][1]) * width
        bbox_center_y = float(bbox_saved[bbox_index][2])* height
        bbox_width = float(bbox_saved[bbox_index][3]) * width
        bbox_height = float(bbox_saved[bbox_index][4]) * height
        bbox_top_left_x = bbox_center_x - bbox_width/2
        bbox_top_left_y = bbox_center_y - bbox_height/2
        bbox_bottom_right_x = bbox_center_x + bbox_width/2
        bbox_bottom_right_y = bbox_center_y + bbox_height/2
        bbox.append(BoundingBox(bbox_top_left_x, bbox_top_left_y, bbox_bottom_right_x, bbox_bottom_right_y))
    bbs = BoundingBoxesOnImage(bbox, shape = image.shape)
    ia.imshow(bbs.draw_on_image(image, size=2))
    del lines[:]
    del bbox_saved[:]
    del bbox_image[:]
    del bbox[:]
    #bbox 좌푣ㄹ
    '''
       bbox_top_left_x = line[1]*height
    bbox_top_left_y = line[2]*width
    bbox_bottom_right_x = line[3]*height
    bbox_bottom_right_y = line[4]*width
    bbs = BoundingBoxesOnImage([BoundingBox(bbox_top_left_x, bbox_top_left_y, bbox_bottom_right_x, bbox_bottom_right_y)], shape = image.shape)
    ia.imshow(bbs.draw_on_image(image, size=1)) 
    '''

#resize는 생략할것

