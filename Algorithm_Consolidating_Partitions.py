There is a computer with a hard drive that is partitioned into several partitions. You'd like to move the data around so that the fewest number if partitions are being used. Given how much space is currently being used on each partition, as well as the total capacity if each, what is the minimum number of partition needed to hold all the data if you move it around optimally?

For example, let's say there are n= 5 partitions, where currently used is usedSpace = [3,2,1,3,1] , and total capacity is totalSpace = [3,5,3,5,5], you can move that data around like so:

a) move data from 1st partition to 2nd partition and 1st partition will be empty b) move data of 3rd and 5th partition to 4th partition and 3rd and 5th will be free.

The final result is 2;

function: int minPartition(List usedSpace, List totalSpace){
//code
}
Testcase 1: Input: usedSpace = [3,2,1,3,1]; totalSpace = [3,5,3,5,5]; output: 2

Testcase 2: Input: usedSpace = [3,3,3]; totalSpace = [5,5,5]; output: 3


Code: http://pythontutor.com/live.html#code=def%20min%28used_space,total_space%29%3A%0A%20%20%20%20count%20%3D%20len%28total_space%29%0A%20%20%20%20total_used%20%3D%20sum%28used_space%29%0A%20%20%20%20return%20total_used%20//%20count%0A%20%20%20%20%0Aused%20%3D%20%5B3,3,3%5D%0Atotal%20%3D%20%5B5,5,5%5D%0A%0Amin%28used,total%29&cumulative=false&curInstr=8&heapPrimitives=nevernest&mode=display&origin=opt-live.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

long solution: http://pythontutor.com/live.html#code=def%20min_partitions%28usedSpace,%20totalSpace%29%3A%0A%20%20%20%20%0A%20%20%20%20count%20%3D%20len%28totalSpace%29%0A%20%20%20%20total_used%20%3D%20sum%28usedSpace%29%0A%20%20%20%20my_dict%20%3D%20%7B%7D%0A%20%20%20%20%0A%20%20%20%20for%20i%20in%20range%28count%29%3A%0A%20%20%20%20%20%20%20%20seen%20%3D%20False%0A%20%20%20%20%20%20%20%20if%20usedSpace%5Bi%5D%20in%20my_dict%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20del%20my_dict%5BusedSpace%5Bi%5D%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20count%20-%3D%201%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20for%20j%20in%20my_dict.keys%28%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20j%20%3E%20usedSpace%5Bi%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20del%20my_dict%5Bj%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20my_dict%5B%20j%20-%20usedSpace%5Bi%5D%5D%20%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20count%20-%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20seen%20%3D%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20break%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20seen%20%3D%3D%20False%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20diff%20%3D%20totalSpace%5Bi%5D-usedSpace%5Bi%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20my_dict%5Bdiff%5D%20%3D%201%0A%20%20%20%20return%20count%0A%20%20%20%20%0AusedSpace%20%3D%20%5B3,2,1,3,1%5D%0AtotalSpace%20%3D%20%5B3,5,3,5,5%5D%0AtotalSpace%20%3D%20sorted%28totalSpace,%20reverse%3DTrue%29%0Aval%20%3D%20min_partitions%28usedSpace,totalSpace%29%0Aprint%28val%29&cumulative=false&curInstr=46&heapPrimitives=nevernest&mode=display&origin=opt-live.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

Stackverflow post: https://stackoverflow.com/questions/62438001/algorithm-consolidating-partitions





