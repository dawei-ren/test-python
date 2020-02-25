### 序列类型

内置序列类型

1.  容器序列

    *   list、tuple、collections.deque

    *   这些序列能存放不同类型的数据
    *   容器序列存放的是她们所包含的任意类型的对象的引用

2.  扁平序列

    *   str，bytes, bytearray, memoryview, array.array
    *   这些序列只能容纳一种类型
    *   扁平序列里存放的是值，而不是引用。
    *   扁平序列其实是一段连续的内存空间
    *   扁平序列其实更加紧凑，但是它里面只能存放诸如字符，字节和数值这种基础类型

按照能否被修改来分类

1.  可变序列：list、bytearray、array.array、collections.deque和memoryview
2.  不可变序列：tuple、str、和bytes。



