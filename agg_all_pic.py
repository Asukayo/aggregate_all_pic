import os
import sys
import shutil

def aggregate_all_pic(input_path):
    # 计算有几个图集进行合并
    num_dirs = 0
    # 要保存的位置
    output_path = os.path.join(os.getcwd(), input_path)

    for dirname,subdirs,files in os.walk(input_path):
        # 只处理没有子目录的目录（最底层目录）
        if len(subdirs) == 0 and len(files) > 0:
            print(f'正在将{dirname}下的图片转移到{output_path}中')
            copy_pic(dirname, files, output_path, num_dirs)
            num_dirs += 1
            print(f'转移成功！')


def copy_pic(input_path,files,output_path,num_dirs):
    """

    :param input_path:  当前需要被复制的目录
    :param output_path:  需要被粘贴到的目录
    :param files:   是第几个图包
    :return:
    """
    for file in files:
        # 重命名文件
        file_path = os.path.join(input_path,file)

        # 复制文件到out_path
        shutil.copyfile(file_path,os.path.join(output_path,file))

        # 对文件进行重命名
        new_file = str(num_dirs) + file
        file_new_name = os.path.join(output_path,new_file)
        os.rename(os.path.join(output_path,file),file_new_name)



def main():

    # 获取需要被聚合的文件
    input_dir = sys.argv[1]

    print(f"文件夹名称：{input_dir}")

    aggregate_all_pic(input_dir)


if __name__ == '__main__':
    main()

