## OBJECT DETECTION ALGORITHMS

## Table of Contents
<ul>
<li>

[I. INTRODUCTION](https://github.com/CuteBoiz/neuralnetwork/tree/master/)

</li>
<li>

[II. REGION-COVOLUTIONAL NEURAL NETWORK(R-CNN)](https://github.com/CuteBoiz/neuralnetwork/tree/master/)

</li>
<li>

[III. FAST REGION-COVOLUTIONAL NEURAL NETWORK](https://github.com/CuteBoiz/neuralnetwork/tree/master/)

</li>
<li>

[IV. FASTER REGION-COVOLUTIONAL NEURAL NETWORK](https://github.com/CuteBoiz/neuralnetwork/tree/master/)

</li>
<li>

[V. YOU ONLY LOOK ONCE (YOLO)](https://github.com/CuteBoiz/neuralnetwork/tree/master/)

</li>
<li>

[VI. SOURCE](https://github.com/CuteBoiz/neuralnetwork/tree/master/)

</li>
</ul>


## I. INTRODUCTION

<p>Thị giác máy tính là một lĩnh vực liên ngành có sức hút rất lớn trong những năm gần đây(từ khi có CNN) và một lĩnh vực không thể thiếu của thị giác máy tính đó là <i>Object Detection</i>. <i>Object Detection</i> giúp ích rất nhiều trong giao thông, bảo mật, giám sát, … </p>

<p>Sự khác biệt giữa giải thuật Object Detection và giải thuật phân lớp là trong giải thuật Detection chúng ta sẽ vẽ các <b><i>Bounding Box</i></b> xung quanh các vật thể cần tìm bên trong ảnh. Như vậy, bạn cũng không nhất thiết vẽ chỉ 1 <i>Bounding Box</i>, có thể có nhiều <i>Bounding Box</i> tượng trưng cho những vật khác nhau trong cũng một ảnh.</p>

### IMG 1

## II. REGION-COVOLUTIONAL NEURAL NETWORK(R-CNN)

<p>Để tránh khỏi vấn đề về chọn số lượng lớn các phân vùng, nhóm của <i>Ross Girshick</i> đã dề xuất một phương pháp sử dụng <b><i>Selective Search</i></b> để trích ra 2000 vùng trong ảnh và gọi đó là các <b><i>Proposal Region</i></b> (Vùng trọng điểm). Vì thế thay vì nhận dạng số lượng lớn các phân vùng, thì với giải thuật này ta chỉ cần làm việc với 2000 vùng. Và 2000 vùng này có thể được tạo ra nhờ giải thuật <i>Selective Search</i>:  </p>

<ul>
	<li>Tạo ra số lượng lớn các phân vùng phụ khởi tạo</li>
	<li>Sử dụng giải thuật tham lam (Greedy Algorithm) để kết hợp đệ quy các vùng tương tự nhau thành các vùng lớn hơn</li>
	<li>Sử dụng những phân vùng đã được kết hợp đó để tạo ra các <b><i>Proposal Region</i></b></li>
</ul>



### IMG 2

<p>2000 vùng này sẽ được bao bọc trong các khung để đưa vào CNN và tạo ra<i> Feature Vector</i> có 4096-chiều. CNN có chức năng như một <b><i>Feature Extractor</i></b> và đầu ra sẽ chứa những <i>Feature</i> trích xuất được từ ảnh và được đưa vào các <b><i>SVM</i></b>(Support Vector Machine) để phân loại sự hiện diện của vật thể bên trong các <i>Proposal Regions</i>.</p>

<p>Thuật toán này có thể dự đoán sự hiện diện của con người nhưng khuôn mặt có thể bên trong vùng đó có thể bị cắt đôi. Vì thế, những offset value giúp điều chỉnh những <i>Bounding Box</i> của <i>Proposal Region</i> này.</p>

### IMG 3

<p>Điểm yếu của R-CNN</p>

<ul>
	<li>Vẫn tốn rất nhiều thời gian để train vì cần xác định 2000 vùng cho mỗi ảnh</li>
	<li>Không thể thực hiện reatime vì cần đến 47s cho mỗi ảnh test</li>
	<li>Selective search là một giải thuật cố định. Vì thế sẽ không thể training tại bước này. Điều này sẽ tạo ra những <i><b>Bad</b> Proposal Region</i>.</li>
</ul>


## III. FAST REGION-COVOLUTIONAL NEURAL NETWORK

### IMG 4

<p>Tác giả của <i><b>R-CNN</b></i> đã giải quyết những vấn đề của R-CNN bằng cách tạo ra một thuật toán nhanh hơn được gọi là <b><i>Fast R-CNN</i></b>. Cách tiếp cận tương tự với <i>R-CNN</i>, nhưng thay vì đưa các <i>Proposal Region</i> vào CNN thì ta đưa ảnh input vào trực tiếp CNN để tạo ra các <b><i>Feature map</i></b>. Và từ các <i>Feature Map</i> ta sẽ xác định các <i>Proposal Region</i> và bọc chúng trong các khung và sau đó sử dụng <b><i>RoI Pooling Layer</i></b> ta reshape chúng thành kích cỡ cố định để có thể đưa vào <i>Fully Connected Layer</i>. Từ <i>RoI Feature Vector</i>, chúng ta sẽ dụng <i>Softmax Layer</i> để dự đoán class cho các <i>Proposed Region</i> và các <i>Offset Value</i> cho <i>Bounding Box</i>.</p>

<p>Lý do <i>Fast R-CNN</i> nhanh hơn <i>R-CNN</i> là vì Fast R-CNN không cần phải đưa cả 2000 vùng vào CNN để <i>convolution</i> với mỗi vùng. Mà thay vào đó ta chỉ cần thực hiện <i>covolution</i> với ảnh đầu vào và với <i>Feature Map</i> được tạo ra bởi ảnh đó. </p>

### IMG 5

## IV. FASTER REGION-COVOLUTIONAL NEURAL NETWORK

### IMG 6

<p></p>

<p></p>

### IMG 7

<p></p>

## V. YOU ONLY LOOK ONCE

<p></p>

### IMG 8

<p></p>
<p></p>
<p></p>

## VI. SOURCE

<ul>
<li>

[https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)

</li>
</ul>