def fancy_name_plate(name):
    print('#'*22)
    print('#'*2,'_'*16,'#'*2)
    print('#'*2,name.center(16,'_'),'#'*2)
    print('#' * 2, '_' * 16, '#' * 2)
    print('#' * 22)
fancy_name_plate('vikash'.swapcase())
