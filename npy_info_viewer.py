import numpy as np
import os

def read_npy_file(file_path):
    """
    读取.npy文件并显示其信息
    
    参数:
        file_path (str): .npy文件的路径
    """
    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"错误: 文件 '{file_path}' 不存在!")
        return
    
    # 检查文件扩展名是否为.npy
    if not file_path.endswith('.npy'):
        print(f"警告: 文件 '{file_path}' 可能不是.npy文件，尝试读取...")
    
    try:
        # 读取.npy文件
        data = np.load(file_path)
        
        # 显示文件基本信息
        print(f"成功读取文件: {file_path}")
        print(f"文件大小: {os.path.getsize(file_path) / (1024 * 1024):.2f} MB")
        print(f"数据类型: {data.dtype}")
        print(f"数组形状: {data.shape}")
        print(f"数组维度: {data.ndim}")
        print(f"数组元素总数: {data.size}")
        
        # 显示部分数据（避免数据过大）
        print("\n部分数据预览:")
        # 根据数据大小决定显示多少
        if data.size <= 100:
            print(data)
        else:
            # 对于大型数组，只显示角落的元素
            print(np.array_str(data, precision=4, suppress_small=True))
            
        return data
        
    except Exception as e:
        print(f"读取文件时发生错误: {str(e)}")
        return None

if __name__ == "__main__":
    import sys
    
    # 检查是否提供了文件路径参数
    if len(sys.argv) != 2:
        sys.exit(1)
    
    # 获取文件路径并读取
    npy_file_path = sys.argv[1]
    read_npy_file(npy_file_path)
